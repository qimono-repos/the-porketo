"""Core 50% harvest calculation.

Formula:

    H50 = RoundDown_Binance(((U * P) - A) / (2 * P))

U = selected strategy-lot units
P = verified current price
A = material anchor
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, ROUND_DOWN


@dataclass(frozen=True)
class HarvestResult:
    eligible: bool
    market_value: Decimal
    threshold: Decimal
    excess_value: Decimal
    calculated_quantity: Decimal
    target_quantity: Decimal


def round_down_to_step(quantity: Decimal, step: Decimal) -> Decimal:
    if step <= 0:
        raise ValueError("step must be positive")
    return (quantity / step).to_integral_value(rounding=ROUND_DOWN) * step


def calculate(
    *,
    current: Decimal,
    position: Decimal,
    anchor: Decimal,
    target_profit: Decimal = Decimal("0.01"),
    step: Decimal = Decimal("0.000001"),
) -> HarvestResult:
    if current <= 0 or position <= 0 or anchor < 0:
        raise ValueError("current and position must be > 0; anchor must be >= 0")

    market_value = position * current
    threshold = anchor + target_profit

    if market_value < threshold:
        return HarvestResult(
            False, market_value, threshold,
            Decimal("0"), Decimal("0"), Decimal("0")
        )

    excess_value = market_value - anchor
    calculated_quantity = excess_value / current
    half_quantity = calculated_quantity / Decimal("2")
    target_quantity = round_down_to_step(half_quantity, step)

    return HarvestResult(
        True, market_value, threshold,
        excess_value, calculated_quantity, target_quantity
    )
