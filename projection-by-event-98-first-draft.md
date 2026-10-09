# Projection by Event 98 — FIRST DRAFT

Status: **FIRST DRAFT** — snapshot projection, to be refined
Created: 2026-10-09 (Halifax)
Horizon: Checkpoint / Event **98 of 98** — Fri 30 Oct 2026, 22:00 Halifax (last calendar checkpoint of the October sprint)

## Question

Treat every holding as **one squad** (the Ted Lasso view: a player is a player, stock or crypto, no separation between engines). From Checkpoint 12 to 98 we **stop expanding** into new assets. Every remaining checkpoint's budget goes into **levelling up** the squad, bringing the lower-funded players up towards equal invested capital.

**How much invested capital (material anchor, USDC) does each player have by Event 98?**

## Inputs

- **Remaining budget:** Checkpoints 12 → 98 inclusive = 87 checkpoints × 0.75 USDC = **65.25 USDC**.
- **Metric:** capital invested (sum of material anchors). **Not** market value.
- **Players:** lots unified by asset (all SOL lots = one player, all TAO lots = one player, etc.).
- **Source snapshot:** `Crypto Sprint` + `Sprint` tabs of the book, 2026-10-09 morning — 31 players, 373.05 USDC invested.

## Method — fill from the bottom (waterline)

1. Rank every player by current invested capital.
2. Pour the budget into the lowest player until it meets the next-lowest, then raise both, and so on.
3. Stop when the budget is spent. The level reached is the **waterline** *L*.
4. Everyone below *L* finishes at *L*; everyone at or above *L* keeps their capital and gets nothing new.

Formally, with the *k* lowest players funded: L = (65.25 + Σ capital of those k) / k, choosing the *k* for which L doesn't exceed the next player up.

## Result

> **Waterline ≈ 11.23 USDC.** 14 players are topped up to 11.23; the other 17 stay where they are.

Projected squad total at Event 98: 373.05 + 65.25 = **438.30 USDC** invested.

| # | Player | Engine | Invested now | Top-up | **Invested at Event 98** |
|---|---|---|---:|---:|---:|
| 1 | DOT | crypto | 2.25 | 8.98 | **11.23** |
| 2 | ALGO | crypto | 2.25 | 8.98 | **11.23** |
| 3 | BLK | stock | 2.49 | 8.74 | **11.23** |
| 4 | DUK | stock | 2.49 | 8.74 | **11.23** |
| 5 | SPCXB | stock | 4.90 | 6.33 | **11.23** |
| 6 | HOOD | stock | 4.97 | 6.26 | **11.23** |
| 7 | RONIN | crypto | 6.50 | 4.73 | **11.23** |
| 8 | ZEC | crypto | 6.53 | 4.70 | **11.23** |
| 9 | TAO | crypto | 8.98 | 2.25 | **11.23** |
| 10 | CVX | stock | 9.95 | 1.28 | **11.23** |
| 11 | OKLO | stock | 9.95 | 1.28 | **11.23** |
| 12 | AVGO | stock | 10.00 | 1.23 | **11.23** |
| 13 | QBTS | stock | 10.00 | 1.23 | **11.23** |
| 14 | ETH | crypto | 10.75 | 0.48 | **11.23** |
| 15 | IMX | crypto | 12.00 | — | 12.00 |
| 16 | TSLAB | stock | 14.70 | — | 14.70 |
| 17 | NVDA | stock | 14.92 | — | 14.92 |
| 18 | FLKR | stock | 14.94 | — | 14.94 |
| 19 | PUMP | crypto | 15.00 | — | 15.00 |
| 20 | SUI | crypto | 15.00 | — | 15.00 |
| 21 | NEAR | crypto | 15.00 | — | 15.00 |
| 22 | GALA | crypto | 15.00 | — | 15.00 |
| 23 | ILV | crypto | 15.00 | — | 15.00 |
| 24 | AAPL | stock | 15.00 | — | 15.00 |
| 25 | SOL | crypto | 15.68 | — | 15.68 |
| 26 | SLP | crypto | 15.75 | — | 15.75 |
| 27 | BTC | crypto | 16.28 | — | 16.28 |
| 28 | LINK | crypto | 17.00 | — | 17.00 |
| 29 | AAVE | crypto | 19.84 | — | 19.84 |
| 30 | ORCL | stock | 19.97 | — | 19.97 |
| 31 | IONQ | stock | 29.95 | — | 29.95 |
| | **Total** | | **373.05** | **65.25** | **438.30** |

(Top-ups shown rounded to cents; they sum to 65.25.)

### Correction note

The figure first quoted in conversation was a waterline of ~13.9. Recomputed exactly, raising the bottom 15 players to 13.9 would cost ~104.48 USDC — more than the 65.25 available. With 65.25, the waterline is **11.23**.

## Sensitivity — Binance lots missing from the Sprint tabs

The 31-player snapshot comes from the `Sprint` / `Crypto Sprint` cockpits, which do not yet hold several Binance stock lots (in `Positions` or the repo, but no Sprint row): QBTSB 9.83, DUKB 9.83, HOODB 10.03 + 0.75, IBMB 9.83 + 0.75, IonQ (Binance) 5.17, MUB 0.75 + 5.83, AMDB 2.25, TSMB 2.25.

Folding them in by underlying asset gives **35 players, 430.32 USDC invested**, and the waterline drops to **≈ 10.76 USDC** (15 players topped up). The main differences:

- New players at the bottom: AMD 2.25, TSM 2.25, MU 6.58, IBM 10.58 — all levelled to 10.76.
- DUK (12.32), HOOD (15.75) and QBTS (19.83) move above the waterline and get nothing.
- IONQ rises to 35.12.

Once those lots are booked into Sprint, the second view is the correct one.

## Caveats

- **First draft.** It is a snapshot of current anchors; the waterline moves if anything changes: the no-expansion rule, the 0.75 per-checkpoint amount, catch-up or prepaid buys, harvests, or lots still to be booked.
- **Capital in, not value.** This says how much money each player will have received, not what it will be worth on 30 Oct.
- **Checkpoint granularity.** Real buys come in 0.75 slices (and venue minimums — e.g. Binance Stocks needs ~5.29 USD for MU overnight), so actual end values will land near, not exactly on, the waterline.
- **Harvests don't move anchors**, so they don't change this projection.
- Order of execution isn't prescribed: levelling from the bottom up is one natural sequence, but any order that ends at the same totals is consistent with this plan.

## Related

- `new_investments.md` — checkpoint budget ledger and the expansion phase this projection follows.
- `DECISIONS/strategy/execution-precedence-over-book-order.md`
