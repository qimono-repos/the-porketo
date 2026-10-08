# Trading Book to MongoDB Atlas migration strategy

Status: scaffold / design phase
Cutover: not approved

## 1. Objective

Move the live trading book from spreadsheet-shaped state to structured, auditable MongoDB state without changing strategy behavior.

Must preserve:
- every strategy lot and material anchor;
- investment and harvest event order;
- wallet/book reconciliation history;
- trade receipts;
- USDT harvest settlement;
- crypto versus stock-side classification;
- 50 percent of excess harvest policy;
- no same ticker in two consecutive harvest evaluations;
- when multiple lots of one ticker qualify, highest-entry lot wins and the others wait one turn;
- the fact that strategy rules can change and the latest GitHub decision supersedes older policy.

## 2. Atlas topology

Development:
Atlas Project the-porketo-dev
  Cluster porketo-dev
    Database porketo_dev

Production:
Atlas Project the-porketo-prod
  Cluster porketo-prod
    Database porketo
    Database porketo_audit

For the current 100-dollar experiment, do not introduce sharding. Use a replica-set-backed Atlas deployment. Keep audit data logically separate even if it initially shares the same cluster.

## 3. Collections

portfolio_lots
One document per strategy lot. Fields: lotId, ticker, assetClass, entryPrice, units, anchor, status, lastHarvestEventNo, createdAt, updatedAt, sourceRefs.

trades
Immutable execution receipts. Fields: tradeId, eventNo, ticker, side, assetClass, nativeUnits, quoteCurrency, quoteAmount, executionPrice, fee, venue, venueTradeId, executedAt, receipt, source.

investment_events
Calendar-driven investment checkpoints. Fields: eventNo, scheduledAt, status, ticker, plannedAmount, actualTradeIds, notes.

harvest_events
Calendar-driven harvest evaluations. Fields: eventNo, scheduledAt, status, candidateLotIds, selectedLotId, selectedTicker, selectedEntryPrice, selectionReason, quantityCalculated, quantityExecutable, expectedQuote, actualTradeIds, previousHarvestTicker, policyVersion, evaluatedAt.

balances
Point-in-time wallet/book snapshots. Fields: snapshotId, capturedAt, venue, wallet, asset, units, source, reconciliationStatus.

prices
Market observations used by the strategy. Fields: observedAt, ticker, assetClass, venue, priceType, price, currency, source.

reconciliation_events
Every comparison between book state and executable/wallet state. Fields: reconciliationId, capturedAt, scope, asset, bookUnits, walletUnits, delta, status, blocking, resolution.

policy_snapshots
Versioned copies of strategy rules used for an evaluation. Fields: policyVersion, sourceCommit, capturedAt, rules.

migration_runs
Operational record of imports and validation. Fields: runId, source, sourceSnapshot, startedAt, completedAt, status, counts, errors, checksum.

## 4. Identity

Use immutable IDs. Spreadsheet row numbers are not permanent IDs.

Recommended lot ID:
LOT-NEAR-0001

Existing strategy trade IDs such as CRT-0052 should be retained.

Calendar event numbers are retained because event order is strategy state.

## 5. Harvest decision model

At harvest event N:
1. Read current active lots.
2. Read the latest reconciliation state.
3. Block lots with unresolved wallet/book mismatch.
4. Evaluate current executable price.
5. Apply material anchor plus the 0.01 trigger.
6. Exclude the ticker harvested at event N-1.
7. Group qualifying lots by ticker.
8. If multiple lots of one ticker qualify, select the highest-entry lot.
9. Other qualifying lots wait one harvest turn.
10. Calculate 50 percent of excess using the current policy.
11. Round to executable venue quantity.
12. Verify the post-harvest value remains above the policy floor.
13. Execute externally.
14. Store the actual receipt.
15. Update book state through an auditable domain event.

Do not invent a permanent swing-reset rule. The current strategy does not require one. This selection rule is explicitly allowed to change.

## 6. Spreadsheet migration

Phase A: freeze
Create a timestamped export. Record export timestamp, checksum, tab names, row counts, formulas versus values, current balances, lot state, last investment event, and last harvest event.

Phase B: normalize
Map:
Crypto Sprint / Stock Sprint -> portfolio_lots
Crypto Trades / Stock Trades -> trades
Investment calendar -> investment_events
Harvest calendar -> harvest_events
USDT wallet -> balances
Price snapshots -> prices
Reconciliation notes -> reconciliation_events
Strategy version -> policy_snapshots

Preserve original row/cell references in sourceRefs.

Phase C: staging
Load the first import into a database named porketo_migration_YYYYMMDD. Never load the first import directly into production.

Phase D: deterministic validation
Compare lot count, units by ticker, anchor by lot, total book value, USDT balance, trade count, investment-event count, harvest-event count, last harvested ticker, last selected lot, and crypto/stock classification.

Phase E: behavioral replay
Replay historical harvest evaluations. The expected result must agree on selected lot, eligibility, quantity, and previous-ticker exclusion, not merely aggregate totals.

Phase F: dual-read
Google Sheet -> candidate
MongoDB -> candidate
Both -> comparison -> human review

Mongo must not execute trades during dual-read.

Phase G: cutover
Mongo becomes canonical only after structural reconciliation, behavioral replay, live dual-read validation, and explicit user approval. The Sheet then becomes an archival/reporting surface.

## 7. API safety

Initial server is read-first.

Initial endpoints:
GET /health
GET /lots
GET /lots/:lot-id
GET /harvest-events
GET /balances/:asset

Do not expose arbitrary Mongo queries, deletes, trade execution, or Binance execution.

Later writes should be domain commands such as:
POST /harvest-events/:id/decision
POST /trades/receipt
POST /reconciliations

Every write must create an audit record.

## 8. AI connector posture

The database is intended to be queryable by multiple AI systems.

Use stable domain collections, not a spreadsheet-shaped document dump.

Default AI access should be read-only.

Suggested roles:
porketo_reader
porketo_operator
porketo_admin

Never give an AI agent unrestricted Atlas administrator credentials.

## 9. Indexes

Initial indexes:
portfolio_lots: unique lotId; ticker + status + entryPrice
trades: unique tradeId; eventNo + executedAt
investment_events: unique eventNo
harvest_events: unique eventNo; selectedTicker + eventNo
balances: asset + capturedAt
prices: ticker + observedAt
reconciliation_events: asset + capturedAt
migration_runs: unique runId

Avoid speculative indexes until real query patterns exist.

## 10. Numeric policy

Trading quantities, prices, anchors, proceeds, and fees should use MongoDB Decimal128. The Clojure boundary should convert numeric strings deliberately. Do not route monetary values through JVM doubles.

## 11. Acceptance checklist

- Sheet export frozen and checksummed.
- All lots imported.
- All trades imported.
- Investment events imported.
- Harvest events imported.
- USDT reconciliation passes.
- Crypto/stock classification passes.
- Anchor values pass.
- Historical harvest replay passes.
- No-consecutive-ticker rule passes.
- Highest-entry selection passes.
- Unresolved reconciliation blocks a candidate.
- Executable quantity validation passes.
- Dual-read period passes.
- User approves cutover.

## 12. Open decisions

Still intentionally open:
- production Atlas tier;
- whether audit data gets a separate cluster;
- raw price retention;
- AI-agent authentication mechanism;
- whether Clojure becomes the only write boundary;
- whether stock execution eventually uses the same domain-command API.

These are architecture decisions, not silently invented strategy rules.