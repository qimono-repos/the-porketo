"""CLI for the Qimono 50% harvest calculator."""

from __future__ import annotations

import argparse
from decimal import Decimal

from .calculator import calculate


def main() -> int:
    parser = argparse.ArgumentParser(description="Qimono 50% harvest calculator")
    parser.add_argument("--harvest", "-harvest", action="store_true")
    parser.add_argument("--to", required=True)
    parser.add_argument("--current", required=True, type=Decimal)
    parser.add_argument("--position", required=True, type=Decimal)
    parser.add_argument("--anchor", required=True, type=Decimal)
    parser.add_argument("--target-profit", type=Decimal, default=Decimal("0.01"))
    parser.add_argument("--step", type=Decimal, default=Decimal("0.000001"))
    args = parser.parse_args()

    if not args.harvest:
        parser.error("use --harvest or -harvest")

    result = calculate(
        current=args.current,
        position=args.position,
        anchor=args.anchor,
        target_profit=args.target_profit,
        step=args.step,
    )

    symbol = args.to.upper()
    url = f"https://www.binance.com/en/convert/{symbol}/USDT"

    if not result.eligible:
        print(f"WAIT: {symbol} lot has not crossed the harvest criterion.")
        print(f"market value = {result.market_value}")
        print(f"threshold    = {result.threshold}")
        return 0

    if result.target_quantity <= 0:
        print("WAIT: calculated harvest is below the executable step.")
        return 0

    proceeds = result.target_quantity * args.current
    print(f"GO TO {url}")
    print(f"sell {result.target_quantity} {symbol}")
    print(f"expected proceeds ≈ {proceeds} USDT")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
