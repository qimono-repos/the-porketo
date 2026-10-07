# DRAFT — Migration: Lemon Cash stocks → Binance

Status: DRAFT (route pending further discussion) — IN PROGRESS (IONQ started)
Created: 2026-10-07 (Halifax)
Deadline: **this week** (must be done before Monday 2026-10-12)

## Rule (agreed)

- Migrating the Lemon Cash stock positions to Binance is a **must this week**.
- It can be done during any investment or harvest calendar event.
- A migration is **NOT** a checkpoint deployment (does not count toward the
  0.75 USDC budget) and is **NOT** a harvest. It is just a migration.
- **Every leg must be booked** in the book.
- A re-buy on Binance may be paid temporarily from Binance USDC before the
  Lemon Cash proceeds arrive; it is still migration, and the advance is
  repaid when the Lemon funds land.

## Progress log

### IONQ — started 2026-10-07

| Leg | When (Halifax) | Venue | Detail | Status |
|---|---|---|---|---|
| 1. Sell | 2026-10-07 14:28 | Lemon Cash | 3.292296279 IONQ @ US$40.92 = 134.73 USDT; fee 0.5% = 0.67; received **134.06 USDT**. Tx `b944dc43-6161-4879-bcf8-36c74158f73d` | DONE — to book |
| 2. Transfer | — | Lemon Cash → Binance | 134.06 USDT still parked in Lemon Cash. Not moved: real transfer fees to study first | PENDING |
| 3. Re-buy (partial) | 2026-10-07 14:45:52 | Binance Stocks (direct, not bStock) | 0.122135912 IONQ @ ≈40.94; 5.00 + 0.17 USDC fee = **5.17 USDC**, paid from Binance USDC (advance against leg 2) | DONE — to book |
| 3. Re-buy (rest) | — | Binance Stocks | 3.170160367 IONQ still to re-buy to restore the full position (subject to price) | PENDING (after leg 2) |

Lesson: Binance Stocks has a ~5 USDC minimum and a flat 0.17 USDC fee →
cheap at migration size (~0.13% on 134), expensive at checkpoint size.

## Proposed route (draft — to discuss)

1. Sell the stock on Lemon Cash.
2. Move the proceeds to Binance (operator's draft: withdraw as **BNB**,
   deposit to Binance). Lemon Cash proceeds land as USDT — compare a direct
   USDT transfer vs the BNB route on real fees.
3. Re-buy on Binance. Options: Binance Stocks (direct, ≥5 USDC + 0.17 fee)
   or Convert bStocks ([ticker]B, ~0.7–0.8% spread).
   - Operator's earlier wording: "the similar stock but in Robinhood" — to
     confirm what was meant.

## Positions to migrate — NEEDS RECONCILIATION

Binance Stocks order history shows direct buys on **2026-10-04** of DUK
(12.51), OKLO (5.18), BLK (12.51) and QBTS (5.18) USDC. These may already be
on Binance rather than Lemon Cash. Reconcile against Lemon Cash holdings
before migrating anything else.

| Ticker | Where it is (to verify) | Binance equivalent |
|---|---|---|
| AAPL | Lemon Cash? | AAPLB listed — confirm in Convert |
| IONQ | Lemon sold; Binance Stocks partial | migration in progress |
| ORCL | Lemon Cash? | NOT verified |
| AVGO | Lemon Cash? | NOT verified |
| QBTS | Binance Stocks bought 2026-10-04? | also QBTSB held |
| FLKR | Lemon Cash? | NOT verified (ETF) |
| NVDA | Lemon Cash? | NVDAB listed — confirm in Convert |
| CVX | Lemon Cash? | NOT verified |
| OKLO | Binance Stocks bought 2026-10-04? | — |
| HOOD | Lemon Cash? | also HOODB held |
| BLK | Binance Stocks bought 2026-10-04? | — |
| DUK | Binance Stocks bought 2026-10-04? | also DUKB held |

Related open TODO: IBM → IBM/IBMB switch (see ibm-ibmb notes).

## Open questions

- Real transfer cost Lemon Cash → Binance (USDT direct vs BNB route;
  network must match the Binance deposit address).
- What happens to positions with no Binance equivalent (e.g. FLKR)?
- Booking design: new lot keeps the old lot's anchor or takes a new one?
- Does a migrated lot merge with an existing lot on Binance or stay separate?
- Timing: Lemon Cash sells only in US market hours (10:30–17:00 Halifax);
  only the 16:00 investment / 16:15 harvest slots fall inside them.
