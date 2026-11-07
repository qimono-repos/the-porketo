#!/usr/bin/env python3
"""Lot geometry: one lot as a line, its harvest threshold as another line.

Numbers go in as text formulas ("2.25", "3/4*2", "sqrt(2)", "pi/6") and stay
exact (sympy) until they are printed, at whatever precision you ask for.

    pip install sympy
    python3 SCRIPTS/lot_geometry.py --anchor 2.25 --units 0.00491341 \
        --price 421.736 --target 0.10 [--digits 34] [--width 60 --height 18]

Geometry, normalised so every lot looks the same:
    x = price / entry price          (1 = bought price)
    y = market value / anchor        (1 = break-even)
    every lot lives on the line y = x (45 degrees, pi/4 rad)
    harvest threshold is the horizontal line y = 1 + target
    -> harvest when the lot's point is on or above that line

Angle of profit (radians): theta = atan(return). 0 = break-even,
atan(target) = threshold, pi/4 = +100 %. Bounded and comparable across lots.
Exponential form: value = anchor * e^g, with g = ln(value/anchor) (log return).

Calculator only. Never places an order. The receipt remains the truth.
"""
from __future__ import annotations

import argparse

from sympy import Rational, atan, log, nsimplify, pi
from sympy.parsing.sympy_parser import parse_expr, standard_transformations

ALLOWED = {"sqrt", "pi", "E", "exp", "log", "sin", "cos", "tan", "atan", "Rational"}


def exact(text: str):
    """Parse a book formula into an exact sympy number. Decimals become fractions."""
    import sympy

    local = {name: getattr(sympy, name) for name in ALLOWED}
    expr = parse_expr(text, local_dict=local, global_dict={"__builtins__": {}, "Integer": sympy.Integer,
                      "Float": sympy.Float, "Symbol": sympy.Symbol}, transformations=standard_transformations)
    expr = nsimplify(expr, rational=True) if expr.has(sympy.Float) else expr
    if expr.free_symbols:
        raise ValueError(f"formula has unknown names: {expr.free_symbols}")
    return expr


def show(expr, digits: int) -> str:
    return f"{expr}  ≈ {expr.evalf(digits)}"


def chart(x_now: float, threshold: float, width: int, height: int) -> str:
    x_max = max(2.0, x_now * 1.2, threshold * 1.2)
    y_max = x_max
    rows = []
    for r in range(height, -1, -1):
        y = y_max * r / height
        line = []
        for c in range(width + 1):
            x = x_max * c / width
            cell = " "
            if abs(y - threshold) <= y_max / height / 2:
                cell = "-"
            if abs(y - x) <= y_max / height / 2:
                cell = "/"
            if abs(x - 1) <= x_max / width / 2 and abs(y - 1) <= y_max / height / 2:
                cell = "o"  # entry / break-even
            if abs(x - x_now) <= x_max / width / 2 and abs(y - x_now) <= y_max / height / 2:
                cell = "@"  # the lot now
            line.append(cell)
        rows.append(f"{y:5.2f} |" + "".join(line))
    rows.append("      +" + "-" * (width + 1))
    rows.append(f"       x = price/entry, 0 … {x_max:.2f}   o entry  @ now  - harvest line  / lot line")
    return "\n".join(rows)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--anchor", required=True, help="USDC put into the lot (formula ok)")
    ap.add_argument("--units", required=True, help="units held (formula ok)")
    ap.add_argument("--price", required=True, help="current price (formula ok)")
    ap.add_argument("--target", default="1/10", help="target return before harvest, e.g. 1/10 = 10%%")
    ap.add_argument("--digits", type=int, default=12)
    ap.add_argument("--width", type=int, default=60)
    ap.add_argument("--height", type=int, default=16)
    a = ap.parse_args()

    anchor, units, price, target = (exact(v) for v in (a.anchor, a.units, a.price, a.target))
    entry = anchor / units
    value = units * price
    ret = value / anchor - 1
    theta = atan(ret)
    g = log(value / anchor)
    harvest_price = entry * (1 + target)
    d = a.digits

    print(f"entry price      {show(entry, d)}")
    print(f"market value     {show(value, d)}")
    print(f"excess           {show(value - anchor, d)}")
    print(f"return           {show(ret, d)}")
    print(f"profit angle     {show(theta, d)} rad  (threshold {show(atan(target), d)})")
    print(f"log return g     {show(g, d)}   value = anchor·e^g")
    print(f"harvest price    {show(harvest_price, d)}")
    print("signal           " + ("HARVEST (on/above the line)" if ret >= target else "WAIT"))
    print()
    print(chart(float(price / entry), float(1 + target), a.width, a.height))


if __name__ == "__main__":
    main()
