# Exits MDB and DOT, entries PAXG and ALB (2026-10-24)

**Status:** decided by Albert on the voice call, 2026-10-24 (~14:00 Paramaribo/Halifax). Amends [`2026-10-24-diversification-gold-and-narrative.md`](2026-10-24-diversification-gold-and-narrative.md).

## Pairing

| In | Out | When |
|---|---|---|
| **PAXG** | **MDB** | Same day MDB is sold |
| **ALB** (Albemarle, lithium) | **DOT** | ALB bought **today**; DOT exits later via a programmed limit sell |

**OKLO stays** (and may receive more units; separate discussion). **FLKR stays**: Albert considers it the best proxy for AI.

## MDB: documented exception to the "out" rule

- Thesis for the exit: the portfolio is too tied to AI. MDB is not a bad company, but it grows because of AI, not because it is an exceptional database.
- Normal "out" rule: sold only once back at anchor. **Exception (Albert):** wait about one week for the CEO-news dust to settle and exit with the least loss, **even below anchor**.
- Lot: page Sprint, row #38, MDB @ 434.49, anchor 14.99009, 0.034500419 units. At 371.09 (book, 24 Oct 09:33) value is about 12.80, about -15%.

## DOT: exit with a programmed limit sell (preferred tool for "out" exits on Binance)

- Lots (page Crypto Sprint): DOT @ 1.11301 (anchor 2.25, 2.00391167 units) and DOT @ 1.1591 (anchor 4.50, 3.88225125 units).
- Combined: anchor 6.75 for 5.88616292 DOT, so **break-even is about 1.147**. Book price 1.064 (24 Oct 09:33): a lossless exit today would need about +8%.
- **Mechanism:** Binance Convert, Limit tab: sell **all DOT** at **1.15 USDC**. It works 24/7 with nobody watching. If it fills, proceeds are about 6.77 USDC (just above the anchor, no loss). The candle alert (`apps-script/candle-alert.gs`) reports it; book the fill; full exits settle in **USDC**.
- **Funding order:** the budget has margin, so **ALB is bought today** and the limit sell is programmed later. The DOT sale is a pending "money shot" back into USDC whenever it fills.
- If 1.15 is never touched, DOT simply stays frozen (no new units).

## Why limit sells are the default for "out" exits

"Out" means sell only at or above anchor. A standing limit order at the break-even price enforces exactly that, catches a candle at any hour, and needs no human at the screen. Albert prefers not to rely on limit orders for harvests; for exits at break-even they are now the preferred tool.

## To do

- [ ] Buy ALB today (venue and tier at execution; book it as a new lot).
- [ ] Program Binance Convert Limit: sell 5.88616292 DOT at 1.15 USDC.
- [ ] MDB: watch for one week; sell, then buy PAXG the same day.
