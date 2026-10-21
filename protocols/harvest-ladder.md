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

## Worked example (2026-10-21, 09:33 Halifax prices)

| Lot | 50% of excess | Ladder step |
|---|---|---|
| AXS | 0.83 | 0.75 |
| IBMB lot 1 | 0.55 | 0.45 |
| SPCXB (2 lots) | 0.47 | 0.45 |
| BTC @ 77,360 | 0.32 | 0.30 |
| TSLAB | 0.31 | 0.30 |
