# Migration TODO — blockers before the Datomic load

Checklist of the six blockers from `SPECS/DATOMIC-MIGRATION.md`. Fail closed:
no load until every item is resolved or explicitly carried as a documented open fact.

- [x] **1. Duplicate Event ID `CRF-0002`** (Crypto Trades). Resolved 2026-10-04 —
  the +30.00 USDC allocation (sheet row 31) re-IDed to **CRF-0003**; the 3.58017
  USDC BNB top-up (row 15) keeps CRF-0002. All 43 Event IDs now unique.
- [x] **2. Incomplete `CORR-0034` (SOL correction, row 40).** Resolved 2026-10-04 —
  recovered from the Binance Convert receipt: 0.008875 SOL → 0.98930592 USDC at
  1 SOL = 111.471 USDC, 2026-09-19 06:50 ART, fee 0. Kept as a CORRECTION; Related
  Event still to be linked to the source SOL lot.
- [ ] **3. TSLAB / SPCXB dual-book.** Decided: they are **stocks**
  (`:event/book :book/stocks`) though cash settled in Binance USDC. Still to do:
  encode in the schema that an event's book is independent of its settlement
  currency.
- [ ] **4. Precision.** Stock export used displayed values (6 dp). Use **receipt
  precision** for `bigdec` (e.g. 0.04416961 NVDA) and keep the displayed value
  alongside for trace.
- [ ] **5. Timestamps.** Mixed formats ("~05:30", "00:00 checkpoint",
  "post-session", blank MIG rows). Carry an explicit precision attribute
  (`minute|day|unknown`); never guess an instant.
- [ ] **6. Carry as documented open facts (record, do not resolve by import):**
  the accidental TAO reverse convert; the 4.36637774 USDC outside the experiment;
  the ORCL average-cost review.

## Next

- Write the full Datomic schema (events + lots, both books unified by
  `:event/book`, event types: trade, migration, bookkeeping, capital, FX, penalty,
  correction). This is the real unlock before any data load.

_Last updated: 2026-10-04_
