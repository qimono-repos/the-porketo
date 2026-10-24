# TODO (Monday 2026-10-26): finish the DUK → DUKB migration

Status: **OPEN** · opened 2026-10-24 · owner: Albert (any agent can run it)

## Why

DUK is a plain Binance Stocks holding: selling it costs a 0.17 USDC fee, needs about 5 USDC minimum, and only trades in market hours. That blocks micro-harvests. DUKB (the bStock wrapper) trades through Convert with 0 fee, no minimum, 24/7. Duke has proved it can be harvested (+1.75 over anchors on 2026-10-24). Swapping DUK for DUKB keeps the asset count the same. Binance offers no direct DUK → DUKB token conversion, so the route is sell, then buy.

## Leg 1 · sell DUK (placed 2026-10-24)

- Binance Stocks, **Limit Sell**, placed 2026-10-24 08:19:48 Halifax, 24-Hour Trading session
- Price 124.91 USDC · 0.194212766 DUK (whole position: lots DUKB @ 114.34 + DUKB @ 117.14 in Sprint)
- Filled 0 at 08:20 on Saturday. Expect the fill when the market opens, and the USDC to settle later (the 16 Oct AAPL/BLK exits settled on Monday 15:00).
- Expected: 0.194212766 × 124.91 = 24.26 gross, minus 0.17 fee ≈ **24.09 USDC**

## Monday checklist

1. [ ] Order History: confirm the DUK sell filled (time, price, fee, order no.).
2. [ ] Wallet: confirm the USDC has settled. If not, wait; do not invest money that has not landed.
3. [ ] **Harvest from the gain** ([harvest ladder](../protocols/harvest-ladder.md)). Anchors 9.83 + 12.67926 = 22.50926. Gain = net proceeds − 22.50926 (≈ 1.58 at the expected fill). 50% ≈ 0.79, so step **0.75**: Convert 0.75 USDC → USDT. Recompute from the real fill first.
4. [ ] **Buy DUKB** with the rest (≈ 23.34 USDC) via Convert. New lot `DUKB @ <rate>`, anchor = USDC actually converted.
5. [ ] Book it (the DUK sell is a **migration leg**, not a harvest; it doesn't count against the slot budget):
   - `Trades-October`: DUK SELL (migration), USDC→USDT harvest 0.75, DUKB BUY (migration).
   - `Sprint`: close rows `DUKB @ 114.34` and `DUKB @ 117.14 (recon)` (they are really DUK); add the new DUKB lot.
   - `Slots`: note the harvest at the slot it happened in. No investment amount in column F (migration money isn't slot money).
6. [ ] Mark this file DONE with the event IDs.

## Next (after this works)

Consider the same route for the other plain Binance Stocks holdings (MDB, QBTS, IONQ, OKLO, XNDU, PSQL) once each is above its anchor, so the sale itself is not at a loss.
