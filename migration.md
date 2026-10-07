# DRAFT — Migration: Lemon Cash stocks → Binance

Status: DRAFT (route pending further discussion) — IN PROGRESS
Created: 2026-10-07 (Halifax)
Deadline: **this week** (must be done before Monday 2026-10-12)

## Rule (agreed)

- Moving off Lemon Cash to Binance is a **must this week**.
- Migration work can happen during any investment or harvest calendar event.
- Pure migration moves (sell on Lemon, move funds) are **NOT** checkpoint
  deployments and **NOT** harvests.
- **Every leg must be booked** in the book.

## Progress log

### IONQ — 2026-10-07 (outcome: exit Lemon + new Binance position)

The Lemon Cash IONQ position was **closed altogether**, not moved 1:1. A new,
smaller IONQ position was opened on Binance and **counted as checkpoint
budget** (operator decision 2026-10-07).

| Leg | When (Halifax) | Venue | Detail | Classification |
|---|---|---|---|---|
| Sell (close position) | 2026-10-07 14:28 | Lemon Cash | 3.292296279 IONQ @ US$40.92 = 134.73 USDT; fee 0.5% = 0.67; received **134.06 USDT**. Tx `b944dc43-6161-4879-bcf8-36c74158f73d` | Migration (exit) — to book |
| New position | 2026-10-07 14:45:52 | Binance Stocks (direct, not bStock) | 0.122135912 IONQ @ ≈40.94; 5.00 + 0.17 USDC fee = **5.17 USDC** | **Checkpoint budget**: covers CP4–CP9, 0.67 credit to CP10 — to book |
| Funds moved | 2026-10-07 (after sale) | Lemon Cash → Binance Spot | Local currency from the sale converted → **43.00529321 USDC** received in Spot | Migration (funding) — to book |
| Remainder | — | Lemon Cash | ≈ 91 of the 134.06 not yet accounted for (assumed still in Lemon Cash) | PENDING |

Lesson: Binance Stocks has a ~5 USDC minimum and a flat 0.17 USDC fee.

## Proposed route (draft — to discuss)

1. Sell the stock on Lemon Cash.
2. Move the proceeds to Binance (options seen so far: local currency →
   USDC as on 2026-10-07; operator's draft BNB route; direct USDT). Compare
   real fees before the next one.
3. Re-buy on Binance only if wanted: Binance Stocks (direct, ≥5 USDC + 0.17
   fee) or Convert bStocks ([ticker]B, ~0.7–0.8% spread).

## Positions to migrate — NEEDS RECONCILIATION

Binance Stocks order history shows direct buys on **2026-10-04** of DUK
(12.51), OKLO (5.18), BLK (12.51) and QBTS (5.18) USDC. These may already be
on Binance rather than Lemon Cash. Reconcile against Lemon Cash holdings
before migrating anything else.

| Ticker | Where it is (to verify) | Binance equivalent |
|---|---|---|
| AAPL | Lemon Cash? | AAPLB listed — confirm in Convert |
| IONQ | Lemon CLOSED; new Binance Stocks position | done |
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

- Real transfer cost Lemon Cash → Binance per route.
- Positions with no Binance equivalent (e.g. FLKR)?
- Booking design for exits vs 1:1 moves (anchor handling).
- Timing: Lemon Cash sells only in US market hours (10:30–17:00 Halifax);
  only the 16:00 investment / 16:15 harvest slots fall inside them.
