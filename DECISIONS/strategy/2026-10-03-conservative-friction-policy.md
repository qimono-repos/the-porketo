# Decision: Conservative Friction Policy for Rounded 0.00 Fee Receipts

- **Date:** 2026-10-03
- **Status:** Active standing rule
- **Scope:** All trades onward, both the stock engine (Trades / Positions / Sprint) and the crypto engine (Crypto Trades / Crypto Positions / Crypto Sprint).

## Decision

For every trade from this point forward, whenever a Binance Convert, Binance Instant, or broker receipt shows a **rounded 0.00 fee**, always book a **conservative friction of 1% of the converted / gross proceeds** as the Fees / Friction value, and label it in the notes as an assumption.

If a higher actual fee is known from the receipt, use the actual fee instead. The 1% figure is a floor applied only when the displayed fee is a rounded zero.

## Why

- A displayed 0.00 fee is almost always a rounding artifact, not a true zero cost. Treating it as literally zero overstates reusable cash and causes fee starvation across many small repeated harvests and buys.
- This formalizes the book's existing Rule 7 ("Rounded fee displays are not zero") into a standing, always-applied policy so it does not have to be re-decided per trade.
- Confirmed explicitly by the operator on 2026-10-03: "Always apply the conservative friction."

## Key Knowledge / Mechanics

- Friction = 1% of the converted amount (USDC-equivalent for crypto, converted USD amount for stocks).
- Materialized amount = converted amount − booked friction.
- The assumption must be stated in the trade's Notes field (e.g. "Receipt showed 0.00 fee; booked conservative 1% friction per this policy as an assumption").
- Net cash flow and Harvest Reserve receive gross proceeds minus the booked friction.

## Related

- Book Rule 7 in the TRADE-October-26-Sprint README ("the book").
- First applied to TRD-0024 (TSLAB) and TRD-0025 (SPCXB), both Binance Convert fills dated 2026-09-30, booked into the Trades tab. Tokenized stocks such as TSLAB (Tesla) and SPCXB (SpaceX) are booked in the stock Trades tab, not the crypto tabs.
