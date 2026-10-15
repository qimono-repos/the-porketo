# Decision — The three carried open facts, now RESOLVED

**Date:** 2026-10-04
**Status:** Accepted — **closes migration blocker #6.** First recorded as "carried
open facts"; later the same session all three were **disposed of**, so none remains
owed. This record supersedes the earlier "documented, not resolved by import"
framing.

**Context:** Voice working session on the Datomic migration. Blocker #6 began as a
set of known irregularities to carry alongside the migration. On review, the
decision was to **resolve or ditch each now**, not park them. All three are now
closed.

## Dispositions

1. **Accidental TAO reverse convert — RESOLVED as a marginal realized loss.**
   The convert was reversed straight back out; the two legs were ~2 minutes apart
   ("solved in the air"). Not a wash to zero: a marginal residue remained and the
   original figures are not recoverable. **Disposition: considered lost — booked as
   a small realized loss, both legs recorded for truthful history.** Related book
   note already lives on CRT-0037 (the preceding accidental 0.482 USDC → 0.00180895
   TAO at 266.452, excluded from strategy accounting).

2. **4.36637774 USDC surplus — RESOLVED as formally out of scope.**
   Origin: Crypto Trades row CRF-0003 (sheet row 30), note cell M30. The wallet
   physically showed 35.15184952 USDC; only 30.00 was admitted as experiment
   capital and pre-funding experiment cash was 0.78547178, leaving
   35.15184952 − 30 − 0.78547178 = **4.36637774** physically present but never
   admitted. **Disposition: formally declared outside the experiment — not owed,
   not pending, excluded from all experiment reconciliation totals.**

3. **ORCL average-cost review — RESOLVED as confirmed correct.**
   Computed from the three ORCL rows: MIG-0003 BUY 0.095432 @ 157.18; TRD-0009 SELL
   0.003280 @ 162.61; TRD-0021 BUY 0.033017 @ 150.53. **Net held 0.125169 units;
   gross buys 19.97 USD over 0.128449 units → average cost 155.47 USD/unit.** The
   figure reconciles with the position held materially in the wallet. **Disposition:
   average cost confirmed correct at 155.47; review closed.**

## Consequences

- Blocker #6 is fully closed; nothing from it is carried into the migration as open.
- Reconciliation excludes the 4.36637774 USDC surplus and the unintended TAO
  convert from experiment totals — by flag, not deletion; both stay recorded.
- The TAO residue stands as a booked marginal loss, not a zero.
- ORCL migrates with a confirmed 155.47 average cost on 0.125169 net units.
- Consistent with the project principle: the book records what actually happened —
  including a small loss and an out-of-scope surplus — rather than laundering or
  erasing either.
