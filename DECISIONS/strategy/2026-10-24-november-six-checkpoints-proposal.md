# November: 6 checkpoints a day (proposal, 2026-10-24)

**Status:** PROPOSAL. Albert asked for shorter gaps between checkpoints from November (6 a day instead of 4) to catch more candles. Open points are at the bottom.

## Schedule

Every 4 hours: **00:00, 04:00, 08:00, 12:00, 16:00, 20:00**. The price worker runs one hour before each: 23, 03, 07, 11, 15, 19.

November has 30 days × 6 = **180 slots** (October had 98 slots of 6 h).

## Budget

The November budget is **270 USDC** (already funded, CRF-NOV-0001).

| Option | Per slot | Total | Tiers |
|---|---|---|---|
| **A (recommended)** | **2 units = 1.50 USDC** at every slot | 180 × 1.50 = **270** ✅ | A slot = one B, or C + C. An A pick (3 units) takes one slot plus a C in the next slot. |
| B | Harvest check at all 6; invest 3 units at 4 of them | 120 × 2.25 = 270 ✅ | Unchanged (A, B+C, C+C+C) |
| C | 3 units at all 6 | 180 × 2.25 = 405 ❌ | Needs +135 USDC |

**Why A:** every slot is the same, so the `Slots` tab, the calendar and the catch-up rule stay simple: a slot is a slot. The budget fits to the cent. Each slot is smaller, so more of them can wait for a dip.

## What changes if approved

- **`Slots` tab:** a November copy with 180 rows, 4 h step, 2 units per slot.
- **Calendar:** 180 "Checkpoint N of 180" events. The harvest check is part of every checkpoint.
- **Price worker:** `RUN_HOURS = [23, 3, 7, 11, 15, 19]`.
- **The candle alert (hourly) stays as it is.** It covers the gaps between checkpoints.
- **Docs:**
  - `protocols/catch-up-process.md`: "a slot is 2 units" from 1 Nov;
  - `three-units-per-slot-fibonacci-tiers.md`: amended for November.

## Open points for Albert

1. Option A, B or C?
2. **Clock change:** Halifax moves to GMT-4 on Sunday 1 Nov; Buenos Aires stays GMT-3. October used "Halifax/ART" because they matched. Which clock runs November? The scripts use `America/Halifax`.
