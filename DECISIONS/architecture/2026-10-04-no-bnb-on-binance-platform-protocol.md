# Decision — Protocol: no Binance cryptocurrency held on the Binance platform

**Date:** 2026-10-04
**Status:** Accepted (standing protocol for the duration of the current experiment)
**Context:** Voice working session on the Datomic migration. While deciding whether
the `Fee Asset` column in Crypto Trades earns its place, we examined what makes a
fee asset *vary* from one trade to the next.

## Decision

For the duration of this experiment, **I will not hold Binance cryptocurrency in
the Binance platform.**

The word *platform* is deliberate. It is the same term used by the `Platform`
column in the trading book — part of the project's **ubiquitous language**. The
protocol constrains one platform (Binance) in the same vocabulary the book uses to
record where a transaction happened, so there is no translation layer between how
we speak and how the book is built.

## Why

On the Binance platform, if Binance cryptocurrency is held, Binance automatically
charges trading fees in that asset (at a discount) whenever a balance exists, and
falls back to the quote asset only when it runs out. That makes the **fee asset
vary silently** mid-trading — the moment the balance hits zero, the next fee
switches asset without notice.

By never holding Binance cryptocurrency on the Binance platform, **every fee is
charged in the quote asset** (USDC under current habits). The fee asset stays
constant *by construction*, which keeps USD-equivalent reconciliation
straightforward and removes a class of silent error.

## Consequences

- The `Fee Asset` column in Crypto Trades stays faithful but constant (reads
  "USDC"). Kept, not deleted — recording that it does *not* vary is itself a fact
  worth keeping (the Porketo way), and the column comes alive again the day
  behaviour changes.
- **Re-arming trigger:** if this protocol is ever lifted, or a non-USDC quote pair
  (e.g. a USDT pair) is traded, the fee asset can vary again and must be tracked
  per row.
- Scope is the *asset inside the Binance account only*. Buying Binance the **stock**
  elsewhere (e.g. through Robinhood) is outside this protocol — different account,
  different book.
