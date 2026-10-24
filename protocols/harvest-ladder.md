# Harvest Ladder Protocol (fixed steps)

Adopted: 2026-10-21 (ART). Replaces odd-amount harvests.

## Ladder (USDT)

0.30 · 0.45 · 0.75 · 1.50 · 2.25 · 3.75 · 6.00

- 0.75 = 1 unit (same unit as checkpoints).
- Below the unit, steps follow Fibonacci multiples of 0.15 (2, 3, 5), rounded for real-world amounts.
- Above the unit, steps are 2, 3, 5, 8 units.
- Minimum harvest: 0.30. 0.15 was considered and removed.

## Rule

1. Compute the raw harvest as before: 50% of the lot's excess above its material anchor.
2. Snap to the closest ladder step.
3. Cap: the step may never exceed the full excess (anchor stays protected). If the closest step breaks the cap, take the next step down.
4. If no step fits (excess below 0.30), do not harvest; wait.
5. Harvests still settle in USDT; venue fees must not turn the harvest into a net loss.

## Amendment 2026-10-24: never round up past 50%

Operator rule (Albert, 2026-10-24): **snap to the closest ladder step, unless that step is more than 50% of the excess. Then take the next step down.** If no step is at or below 50% of the excess, do not harvest; wait.

So rule 3's cap becomes **50% of the excess** instead of the full excess. The original rule 3 is kept above for history.

- Consequence: a harvest needs at least **0.60 excess** (so that 50% ≥ 0.30, the lowest step).
- Book: since 2026-10-24 the threshold columns use this floor: page Sprint column P and page Crypto Sprint column J, renamed "Min excess to harvest", = 0.60 on every lot. See `JOURNAL/2026-10-24-harvest-threshold-0-60.md`.
- Why: rounding up to the closest step could sell more than half the gain (for example 50% = 0.21 → step 0.30 = 73% of the excess). The 50% rule (2026-10-06) is the anchor-protecting principle; the ladder must not undo it.

| Case (2026-10-24) | Excess | 50% | Closest step | Result |
|---|---|---|---|---|
| IBMB @ 220.29 (STT-0064) | 1.02 | 0.51 | 0.45 | harvest 0.45 ✅ |
| IBMB @ 239.03 | 0.41 | 0.21 | 0.30 > 0.21 | **no harvest, wait** |

The 2026-10-21 examples below all still comply (each step ≤ its 50%).

## Worked example (2026-10-21, 09:33 Halifax prices)

| Lot | 50% of excess | Ladder step |
|---|---|---|
| AXS | 0.83 | 0.75 |
| IBMB lot 1 | 0.55 | 0.45 |
| SPCXB (2 lots) | 0.47 | 0.45 |
| BTC @ 77,360 | 0.32 | 0.30 |
| TSLAB | 0.31 | 0.30 |
