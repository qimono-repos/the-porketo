package com.qimono.harvest.wear

import java.math.BigDecimal
import java.math.RoundingMode

data class HarvestPreview(
    val eligible: Boolean,
    val marketValue: BigDecimal,
    val threshold: BigDecimal,
    val target: BigDecimal = BigDecimal.ZERO,
)

fun calculateHarvest(
    current: BigDecimal,
    position: BigDecimal,
    anchor: BigDecimal,
    targetProfit: BigDecimal = BigDecimal("0.01"),
    step: BigDecimal = BigDecimal("0.000001"),
): HarvestPreview {
    require(current > BigDecimal.ZERO)
    require(position > BigDecimal.ZERO)
    require(anchor >= BigDecimal.ZERO)
    require(step > BigDecimal.ZERO)

    val marketValue = position * current
    val threshold = anchor + targetProfit

    if (marketValue < threshold) {
        return HarvestPreview(false, marketValue, threshold)
    }

    val excessValue = marketValue - anchor
    val calculated = excessValue.divide(current, 18, RoundingMode.HALF_UP)
    val half = calculated.divide(BigDecimal("2"), 18, RoundingMode.HALF_UP)
    val rounded = half.divide(step, 0, RoundingMode.DOWN).multiply(step)

    return HarvestPreview(true, marketValue, threshold, rounded)
}
