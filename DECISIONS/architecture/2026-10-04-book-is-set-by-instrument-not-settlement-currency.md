# Decision — An event's book is set by instrument type, never by settlement currency

**Date:** 2026-10-04
**Status:** Accepted (closes migration blocker #3 — the tokenised-stock dual-book question)
**Context:** Voice working session on the Datomic migration. The open question was:
a tokenised stock (e.g. TSLAB, SPCXB) is traded as a stock but settles in Binance
USDC — which book does it belong to? Today's CEDEAR work on the stock `Trades` tab
supplied the answer by analogy.

## Decision

**An event's `book` is set by the instrument's nature, never by the currency it
settled in.** Reconciliation must never assume that `book == settlement currency`.

- A **CEDEAR** settles in the local currency of a country but **is a stock** →
  `:event/book :book/stocks`.
- A **tokenised stock** (TSLAB, SPCXB) settles in **USDC** but **is also a stock** →
  `:event/book :book/stocks`.

Same shape, two different settlement currencies. The instrument's nature decides
the book; the settlement currency — whether the local currency of a country or
USDC — is a **recorded attribute underneath**, kept for audit, never the thing that
decides the book.

## Consequences

- The Datomic schema must make `:event/book` **independent** of a separate
  settlement-currency attribute. Both are stored; neither derives the other.
- Reconciliation logic must group by `book`, not by settlement currency. A stock
  that cleared in USDC still reconciles against the stock book.
- Note: TSLAB/SPCXB live only in the Sprint tab, not the stock `Trades` tab — the
  rule applies wherever the event is recorded.
- This is the same principle as the "everything is a number" / venue-neutrality
  work: the book of record is faithful to *what a thing is*, and treats venue and
  currency as recorded facts, not as structure.
