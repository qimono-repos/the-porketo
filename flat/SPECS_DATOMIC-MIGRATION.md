# Spec — Migrating the book into Datomic (book of record)

**Date:** 2026-10-04
**Status:** Draft — migration plan, not yet executed
**Source of truth during migration:** the Google Sheet *TRADE-October-26-Sprint*
(ID `1N_osVjWlUVElmZ8UoPUIa5aFex-gfSvy4nJ02k-_KrY`), referred to as "the book".

## Purpose

Move the book (currently a Google Sheet) into **Datomic** as the immutable,
time-travelling **book of record**. This supersedes the earlier MongoDB-leaning
export (`no-sql/stock-trades.json`), per the 2026-10-03 decision
(`DECISIONS/architecture/2026-10-03-databricks-as-analytics-complement.md`):
Datomic is the writable source of truth; Databricks is a later analytics layer.

The sheet and Datomic run **in parallel** until reconciliation queries agree over
several sessions; only then does the cut-over happen. Fail closed: any mismatch
stops the migration.

## What already exists (do not redo)

- `no-sql/stock-trades.json` — 24 stock events (MIG-0001…BOOK-0001) in Mongo
  Extended JSON, from the Trades tab as of 2026-09-30. Reference, not the target.
- `no-sql/examples/DATOMIC-SKETCH.md` — lot schema sketch (`:lot/*`).
- `no-sql/DDD.md` — domain thinking: lot as aggregate root; natural key
  `ticker + entryPrice + openedDate`; events append-only; derived values computed,
  never stored.

## What is missing (this spec adds)

- An **event** schema in Datomic (the sketch only covers lots).
- A **unified book** attribute (`:event/book` = `:book/stocks` | `:book/crypto`).
- Event types for **capital additions, FX, penalty, correction**, not just trades.
- `PROJECT_STATE.md` and `DDD.md` §8 still say "database not decided" — update to
  record the Datomic decision.

## Decisions settled in this session (2026-10-04)

- **Tokenised stocks are stocks.** TSLAB and SPCXB get `:event/book :book/stocks`
  even though their cash settled in Binance USDC. Therefore **an event's book is
  independent of its cash-settlement currency**: schema must allow a stock-book lot
  whose money moved in USDC. Reconciliation must not assume book == settlement
  currency.

## Blockers to resolve before load (fail closed)

1. **Duplicate Event ID `CRF-0002`** in Crypto Trades (the 3.58017 BNB top-up and
   the +30.00 allocation). Under `:db.unique/identity` the second upserts over the
   first and a capital event is lost. Re-ID one before export.
2. **`CORR-0034` (SOL) incomplete** — signed units -0.008875 and USDC wallet flow
   0.98930592, but no amount/price/USDC-eq cash flow (original harvest row
   overwritten). Rebuild from the exchange receipt before load.
3. **TSLAB / SPCXB dual-book** — resolved: stock book (see above). Settlement in
   USDC recorded as a settlement-currency field, not as book membership.
4. **Precision** — stock JSON used displayed values (6 dp). Use **receipt
   precision** for `bigdec` (e.g. 0.04416961 NVDA) and keep the displayed value
   alongside for trace.
5. **Timestamps** — formats vary ("~05:30", "00:00 checkpoint", "post-session",
   blank for MIG rows). Carry an explicit **precision** attribute
   (`minute|day|unknown`), as the Mongo export did; never guess an instant.
6. **Carry as documented open facts, not resolved by import:** the accidental TAO
   reverse convert; the 4.36637774 USDC outside the experiment; the ORCL
   average-cost review.

## Sequence

1. Update `DDD.md` and `PROJECT_STATE.md` to record the Datomic decision.
2. Write the full schema: events (stocks + crypto unified by `:event/book`), lots
   with refs to their events, event types (trade, migration, bookkeeping, capital,
   FX, penalty, correction), settlement-currency field.
3. Freeze a **timestamped snapshot** of the book as the migration source.
4. Export every source tab to **EDN**, deterministically, keeping the sheet row
   reference on each entity.
5. Load into a **local Datomic** (dev/local first — not Gardisto yet).
6. **Reconciliation gate** — must reproduce before trusting anything:
   - stock cash -148.10 -> 1.90 total cash;
   - crypto cash 21.76120387;
   - every Sprint and Crypto Sprint lot's units;
   - every Positions and Crypto Positions aggregate.
   Any mismatch halts the migration.
7. Run in parallel; sheet stays source of truth until both agree over several
   sessions, then cut over.

## References
- `DECISIONS/architecture/2026-10-03-databricks-as-analytics-complement.md`
- `no-sql/examples/DATOMIC-SKETCH.md`
- `no-sql/DDD.md`
- `PROJECT_STATE.md`
