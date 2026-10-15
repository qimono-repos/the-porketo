#!/usr/bin/env python3
"""Qimono Trading 50% harvest calculator.

Pre-trade calculator only. It never places an order.
Execution truth remains the live Binance conversion receipt.

Example:
    ./harvest.py --harvest --to ETH --current 12345 --position 0.250 --anchor 3055.3875

The material anchor is required because current price and position alone
are insufficient to calculate the harvest quantity.
"""

from __future__ import annotations
import argparse
from decimal import Decimal, InvalidOperation, ROUND_DOWN

BINANCE_CONVERT_BASE = "https://www.binance.com/en/convert"

def D(value: str) -> Decimal:
    try:
        return Decimal(value)
    except InvalidOperation as exc:
        raise argparse.ArgumentTypeError(f"invalid decimal: {value}") from exc

def round_down_to_step(quantity: Decimal, step: Decimal) -> Decimal:
    if step <= 0:
        raise ValueError("Binance step must be > 0")
    return (quantity / step).to_integral_value(rounding=ROUND_DOWN) * step

def calculate_harvest(current: Decimal, position: Decimal, anchor: Decimal,
                      target_profit: Decimal, step: Decimal):
    market_value = position * current
    threshold = anchor + target_profit
    if market_value < threshold:
        return False, market_value, Decimal("0"), Decimal("0")
    excess_value = market_value - anchor
    calculated_quantity = excess_value / current
    half_quantity = calculated_quantity / Decimal("2")
    target_quantity = round_down_to_step(half_quantity, step)
    return True, market_value, calculated_quantity, target_quantity

def fmt(x: Decimal) -> str:
    return format(x, "f").rstrip("0").rstrip(".") or "0"

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Calculate the Qimono 50% partial-harvest target."
    )
    parser.add_argument("--harvest", "-harvest", action="store_true",
                        help="calculate a harvest")
    parser.add_argument("--to", required=True, help="asset symbol, e.g. ETH")
    parser.add_argument("--current", required=True, type=D,
                        help="current asset price in quote currency")
    parser.add_argument("--position", required=True, type=D,
                        help="units currently held in the selected strategy lot")
    parser.add_argument("--anchor", required=True, type=D,
                        help="material anchor of the selected strategy lot")
    parser.add_argument("--target-profit", type=D, default=Decimal("0.01"))
    parser.add_argument("--step", type=D, default=Decimal("0.000001"),
                        help="Binance executable quantity step; verify live")
    args = parser.parse_args()

    if not args.harvest:
        parser.error("use --harvest or -harvest")
    if args.current <= 0 or args.position <= 0 or args.anchor < 0:
        parser.error("current and position must be > 0; anchor must be >= 0")

    eligible, market_value, calculated, target = calculate_harvest(
        args.current, args.position, args.anchor, args.target_profit, args.step
    )
    symbol = args.to.upper()
    url = f"{BINANCE_CONVERT_BASE}/{symbol}/USDT"

    if not eligible:
        print(f"WAIT: {symbol} lot has not crossed the harvest criterion.")
        print(f"market value = {fmt(market_value)}")
        print(f"threshold    = {fmt(args.anchor + args.target_profit)}")
        return 0

    if target <= 0:
        print(f"WAIT: calculated 50% harvest is below the executable step ({fmt(args.step)} {symbol}).")
        return 0

    expected_usdt = target * args.current
    print(f"GO TO {url}")
    print(f"sell {fmt(target)} {symbol}")
    print(f"expected proceeds ≈ {fmt(expected_usdt)} USDT")
    print()
    print(f"market value       = {fmt(market_value)}")
    print(f"excess value       = {fmt(market_value - args.anchor)}")
    print(f"calculated harvest = {fmt(calculated)} {symbol}")
    print(f"50% target         = {fmt(calculated / Decimal('2'))} {symbol}")
    print(f"rounded target     = {fmt(target)} {symbol}")
    print("VERIFY Binance live conversion constraints before execution.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
