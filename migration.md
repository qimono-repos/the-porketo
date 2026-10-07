# DRAFT — Migration: Lemon Cash stocks → Binance

Status: DRAFT (pending further discussion)
Created: 2026-10-07 (Halifax)
Deadline: **this week** (must be done before Monday 2026-10-12)

## Rule (agreed)

- Migrating the Lemon Cash stock positions to Binance is a **must this week**.
- It can be done during any investment or harvest calendar event.
- A migration is **NOT** a checkpoint deployment (does not count toward the
  0.75 USDC budget) and is **NOT** a harvest. It is just a migration.
- **Every leg must be booked** in the book.

## Proposed route (draft — to discuss)

1. Sell the stock on Lemon Cash.
2. Withdraw the proceeds from Lemon Cash as **BNB**.
3. Deposit the BNB into the Binance wallet.
4. Convert BNB → the equivalent tokenised stock.
   - Operator wording: "the similar stock but in Robinhood". To confirm:
     Binance bStocks ([ticker]B) or Robinhood stock tokens.

## Positions to migrate (Lemon Cash, from Positions tab)

| Lemon Cash ticker | Binance equivalent | Verified on Binance? |
|---|---|---|
| AAPL | AAPLB | Listed per Binance announcements — confirm in Convert |
| IONQ | IONQB | NOT verified |
| ORCL | ORCLB | NOT verified |
| AVGO | AVGOB | NOT verified |
| QBTS | QBTSB | Yes — already held |
| FLKR | — | NOT verified (ETF) |
| NVDA | NVDAB | Listed per Binance announcements — confirm in Convert |
| CVX | CVXB | NOT verified |
| OKLO | OKLOB | NOT verified |
| HOOD | HOODB | Yes — already held |
| BLK | BLKB | NOT verified |
| DUK | DUKB | Yes — already held |

Related open TODO: IBM → IBM/IBMB switch (see ibm-ibmb notes).

## Open questions

- Is the route (sell → BNB → Binance → convert) the cheapest? Costs to
  measure per leg: Lemon Cash sell fee/spread, BNB buy spread, withdrawal
  fee, Binance Convert spread.
- Does Lemon Cash support BNB withdrawal on the right network (BNB Smart
  Chain)? Network must match the Binance deposit address.
- What happens to positions with no Binance equivalent (e.g. FLKR)?
- Booking design: how to book each leg (stock-side SELL, transfer, BUY of
  the [ticker]B) and whether the new lot keeps the old lot's anchor or
  takes a new one.
- Does a migrated lot merge with an existing [ticker]B lot (QBTS→QBTSB,
  HOOD→HOODB, DUK→DUKB) or stay a separate lot?
- Execution timing: Lemon Cash sells only during US market hours, so the
  sell leg must sit in a 10:00 / 16:00 Halifax event window.
