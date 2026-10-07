#!/usr/bin/env python3
"""
Qimono Trading harvest calculator.

Canonical rule:

    V = U * P
    E = V - A
    H = E / P
    H50 = floor_to_binance_step(H / 2)

This script calculates a PRE-TRADE TARGET only.
It does not query Binance, place orders, or treat its result as execution truth.
"""

from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation, ROUND_DOWN
from urllib.parse import quote


def D(value: str) -> Decimal:
    try:
        return Decimal(value)
    except InvalidOperation as exc:
        raise argparse.ArgumentTypeError(f"invalid decimal: {value}") from exc


def round_down_to_step(quantity: Decimal, step: Decimal) -> Decimal:
    if step <= 0:
        raise ValueError("Binance step must be greater than zero")
    if quantity <= 0:
        return Decimal("0")
    return (quantity / step).to_integral_value(rounding=ROUND_DOWN) * step


def harvest_target(
    position: Decimal,
    current_price: Decimal,
    material_anchor: Decimal,
    binance_step: Decimal,
) -> tuple[Decimal, Decimal, Decimal, Decimal]:
    if position <= 0 or current_price <= 0:
        raise ValueError("position and current price must be greater than zero")
    if material_anchor < 0:
        raise ValueError("material anchor cannot be negative")

    market_value = position * current_price
    excess_value = market_value - material_anchor

    if excess_value <= 0:
        return market_value, excess_value, Decimal("0"), Decimal("0")

    calculated_excess_units = excess_value / current_price
    half_target = calculated_excess_units / Decimal("2")
    executable_target = round_down_to_step(half_target, binance_step)

    return market_value, excess_value, calculated_excess_units, executable_target


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Calculate the Qimono 50%% partial-harvest target."
    )
    parser.add_argument("--to", required=True, help="Asset symbol, e.g. ETH")
    parser.add_argument("--current", required=True, type=D, help="Current asset price")
    parser.add_argument("--position", required=True, type=D, help="Units currently held")
    parser.add_argument(
        "--anchor",
        required=True,
        type=D,
        help="Material strategy anchor in quote currency",
    )
    parser.add_argument(
        "--step",
        required=True,
        type=D,
        help="Verified Binance executable quantity step for this asset",
    )
    parser.add_argument(
        "--no-link",
        action="store_true",
        help="Print the instruction without the Binance URL",
    )

    args = parser.parse_args()

    symbol = args.to.upper()
    market_value, excess_value, calculated, target = harvest_target(
        args.position,
        args.current,
        args.anchor,
        args.step,
    )

    print(f"asset:             {symbol}")
    print(f"position:          {args.position}")
    print(f"current price:     {args.current}")
    print(f"material anchor:   {args.anchor}")
    print(f"market value:      {market_value}")
    print(f"excess value:      {excess_value}")
    print(f"calculated excess: {calculated} {symbol}")
    print(f"50% target:        {target} {symbol}")

    if target <= 0:
        print("WAIT: no executable harvest target.")
        return

    url = f"https://www.binance.com/en/convert/{quote(symbol)}/USDT"
    instruction = f"sell {target} {symbol} for USDT"

    if args.no_link:
        print(f"GO TO Binance Convert; {instruction}")
    else:
        print(f"GO TO {url} ; {instruction}")


if __name__ == "__main__":
    main()
