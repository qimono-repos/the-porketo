# Decision: 50% Partial Harvest Policy

- **Date:** 2026-10-06
- **Status:** Active standing rule
- **Scope:** Crypto harvests in the Trading book, with the policy intended to govern all future harvest calculations unless explicitly overridden by a later decision.

## Decision

From this point forward, when a strategy lot crosses its harvest criterion, the project does **not** automatically harvest the full amount produced by the legacy harvest formula.

The default harvest quantity is **50% of the amount calculated by the legacy harvest formula**, then rounded down to a Binance-compatible USDT precision.

Canonical expression:

`new_harvest_quantity = ROUND_DOWN_TO_BINANCE_USDT_PRECISION(old_harvest_formula / 2)`

In operational language:

> **Harvest half of the calculated harvest quantity, rounded down to the precision required to approach the Binance USDT conversion amount safely.**

The 50% rule applies to the **calculated harvest quantity**, not to the strategy lot's material anchor.

## Purpose

This is a deliberate conservative execution policy intended to reduce:

- fee and friction exposure,
- quote drift between calculation and execution,
- slippage risk,
- minimum-precision / dust problems,
- accidental over-harvesting during fast market movement.

The goal is to liberate part of the excess while preserving meaningful exposure in the strategy lot.

## Accounting Rules

1. The strategy lot's **material anchor does not change** because of a harvest.
2. The strategy lot's **remaining units decrease by the actual executed quantity**.
3. The event log records the **actual Binance execution**, not the calculated target.
4. The Binance receipt remains execution truth.
5. The calculation is only a pre-trade target.
6. If Binance requires a smaller precision or produces a slightly different executable quantity, use the Binance-compatible rounded-down amount.
7. Never round upward merely to reach the calculated target.
8. A partial harvest is still a harvest. Do not create a new strategy lot.
9. Multiple active rungs continue to follow the existing **highest-active-rung** selection protocol. The 50% rule changes the quantity harvested from the selected rung; it does not change which rung is selected.
10. If the resulting quantity is below Binance's executable minimum, do not fabricate an order. Treat it as not executable and preserve the signal for a later opportunity.

## Example

If the legacy formula calculates:

`0.02411932 AAVE`

the new target is:

`0.02411932 / 2 = 0.01205966 AAVE`

Then round down to the Binance-compatible precision before execution.

For the 2026-10-06 AAVE harvest, the operator independently executed a conservative partial harvest of **0.02411932 AAVE → 4.23045 USDT**. That execution is historical execution truth and is not retroactively rewritten by this policy. The new 50% rule governs future harvest calculations.

## Relationship to Fee/Friction Policy

This policy is complementary to the existing conservative-friction policy. A 50% harvest does **not** remove the requirement to apply the project's established fee/friction treatment.

## Verification

Before proposing a harvest:

1. Verify the current strategy-lot state.
2. Verify the active harvest criterion.
3. Calculate the legacy harvest quantity.
4. Divide that quantity by 2.
5. Round down to Binance-compatible precision.
6. Present the resulting target quantity and expected quote proceeds.
7. Execute only against the live Binance conversion/receipt.
8. Record actual execution data in the source event log.
9. Recalculate the derived position and strategy lot.
10. Read the Dashboard last.

## Precedence

This is an active standing strategy decision. A later dated decision may explicitly revise or supersede it. Historical executions remain immutable.

