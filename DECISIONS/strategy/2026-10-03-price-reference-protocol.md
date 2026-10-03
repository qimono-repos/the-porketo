# Decision: Price Reference Protocol (Decision Reference vs. Booked Data)

- **Date:** 2026-10-03
- **Status:** Active standing rule
- **Scope:** All assets, both engines, from now on.

## Decision

Separate two distinct uses of price:

1. **Decision reference (directional context):** For deciding/monitoring, use the real underlying asset's price and trend, as up-to-date as reasonably possible. Exact precision is NOT required here — the underlying's tendency is what informs the decision.
   - Source priority: **Yahoo Finance** for now. When a **Binance MCP/connector** becomes available, use Binance instead.
2. **Booked data (execution truth):** Brute price/units/amount values entered into the books (Trades / Positions / Crypto Trades / Crypto Positions) still come ONLY from the real Binance receipt for the tokenized instrument actually traded. The decision-reference price is never pasted into the book cells.

## Tokenized symbol -> underlying mapping (for decision reference only)

General rule: **drop the trailing "B"** from the tokenized Binance symbol and use the real underlying ticker for Yahoo Finance reference.

Named examples:
- TSLAB -> TSLA (Tesla)
- SPCXB -> SPCX (SpaceX reference)
- IBMB -> IBM

## Why

- The tokenized wrappers (e.g. TSLAB) are thin and inconsistently listed across data providers, with mismatched symbols and unreliable timestamps. The underlying stock gives a cleaner, more current trend signal for decisions.
- Keeping decision reference separate from booked data preserves the book's audit chain: source -> timestamp -> data -> calculation -> interpretation. Execution truth stays anchored to the real receipt; fail closed on booking if the receipt value is unavailable.

## Related

- Conservative friction policy: DECISIONS/strategy/2026-10-03-conservative-friction-policy.md
- Book Step -1 / Step 0 (capture previous reference, refresh current prices) in the TRADE-October-26-Sprint README ("the book").
