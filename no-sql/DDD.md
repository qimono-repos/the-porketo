# DDD — Domain-driven design and the theory behind the data strategy

Started 2026-09-30. This document holds the *thinking*, not the implementation. It is deliberately written so it survives the database decision, which is **still open**.

Companions:
- `no-sql/examples/LOT-ORCL-1.md` — the canonical lot document
- `no-sql/examples/LOT-IDENTITY-AND-GROUPING.md` — natural key and grouping patterns
- `no-sql/examples/DATOMIC-SKETCH.md` — the same model in Datomic
- `no-sql/examples/NEO4J-SKETCH.md` — the same model as a graph
- `no-sql/stock-trades.json` — the 24 migrated stock events

---

## 1. Why this work exists

The TRADING BOOK spreadsheet cannot support the project's stated ambition: reacting faster than a human reading rows. A sheet with hand-typed prices has no queries, no price feed, and no way to compute a harvest signal automatically. Moving the book into a database is the first step; the JSON conversion of the Trades tab was the first step of that first step.

## 2. The thesis, stated precisely

The unit of investment is **not a ticker**. It is a ticker at a price at a moment:

> I am not investing in ORCL. I am investing in **ORCL at 157.18, opened 2026-09-10**.

Everything else follows from taking this literally. Two buys of the same ticker on different days at different prices are different investments with different anchors, different thresholds and different fates. This is already law in the sprint sheet: *same ticker may have multiple lots; never blend their material anchors.*

## 3. The domain objects

**Lot — aggregate root.** The consistency boundary. It owns its invariants, and every one of them is checkable using only what is inside a single lot:

- net units may never go negative
- the material anchor is immutable once set
- a harvest may only fire when market value ≥ harvest threshold
- no lot's state ever depends on another lot's state

That last invariant is what makes the lot the correct boundary rather than the sprint or the ticker.

**Ticker — value object.** No identity, immutable. Promote to an `Asset` entity only when sector and thesis need a single shared home.

**Mark (price + time + source) — value object.** Immutable. Never updated, only recorded anew. Prices come from Yahoo Finance or Binance at query time; what is stored is the snapshot a decision was based on — an audit trail, not a price feed.

**Sprint — bounded context**, or at most a lightweight root holding window, budget and mark timestamp. Explicitly *not* an aggregate containing all lots: that would mean loading and locking the entire portfolio to record one harvest.

**Events — the ledger.** Append-only facts. Referenced by ID from lots, never nested inside them.

## 4. Identity

`ticker` + `entryPrice` + `openedDate` is the lot's **natural key**.

`label` ("ORCL Lot 1 @ 157.18") is a human-readable caption only. Never the identity, never parsed.

**Rule: store the three components as separate indexed fields, never as a single string.** A string cannot be sorted, ranged or filtered on its parts. This single decision is what keeps flexible grouping cheap.

## 5. Grouping

Groups are not stored and have no identity. A group spanning several lots cannot be an aggregate, because a transaction should not span aggregate boundaries.

A group is a **specification** — a named rule, which in a database is simply a query. Store the rule, run it, get the current members. Required lenses include: first N lots of a ticker by date; lots within a price band; lots opened in a date range; all lots above harvest threshold.

When a group action is executed (harvesting three lots at once), record an **event listing the participating lot IDs**. The audit trail captures the result of the grouping, not the grouping itself.

## 6. What is computed, never stored

```
harvestThreshold = materialAnchor + targetProfit
marketValue      = netUnits × mark.price
excess           = marketValue − materialAnchor
signal           = marketValue ≥ harvestThreshold ? HARVEST : WAIT
```

Derived values that are stored can go stale and contradict their inputs — the exact failure mode the spreadsheet suffers from today, where tabs disagree.

## 7. The discipline

| Layer | Rule |
|---|---|
| Events | Append-only. History is never edited. |
| Lots | A projection. Disposable and rebuildable from events. Only identity and strategy fields are set by hand, at creation. |
| Sprints | Set per window, archived when superseded. |

No database enforces this. It is a project rule, and it is written here so it survives whichever engine is chosen.

---

## 8. OPEN QUESTION — the database

**Not decided.** Three candidates have been sketched, and each wins on something the project genuinely wants.

| | MongoDB Atlas | Datomic | Neo4j |
|---|---|---|---|
| Aggregate fit | Excellent — document = aggregate | Good | Blurry |
| Ledger / audit | Manual, by discipline | **Built in** | Weak |
| Time travel | Hand-rolled | **`as-of`, free** | Hand-rolled |
| Relationship questions | Awkward | Awkward | **Excellent** |
| Semantic / vector search | **Atlas Vector Search** | None built in | Vector indexes |
| Effort for one operator | **Lowest** | Highest | Medium-high |

**The pulls, honestly stated:**

- *Atlas* — lowest effort, and semantic search lives in the same system. The 24 events are already in Extended JSON, ready to import.
- *Datomic* — the immutable audited ledger with free time travel, which is this project's snapshot philosophy built into the engine rather than hand-rolled. Clojure is the operator's preferred language. Nubank, a bank, acquired the company outright.
- *Neo4j* — turns correlation and diversification into traversals. The standing research question in `PROJECT_STATE.md` — *find stock names uncorrelated with AI* — is literally a graph query.

**Current leaning:** a book of record (Atlas or Datomic) with a graph derived from it for research questions, rather than a graph as primary store. Not a commitment.

**What would settle it:** whether the project needs auditable time travel or semantic search *first*. That depends on how the 30-day experiment beginning 2026-10-01 actually goes.

---

## 9. Still to model

- Crypto book alongside stocks, distinguished by `book`, sharing the lot model
- Capital additions — the Trades tab has no row type for them; past top-ups appear only as Budget changes in Positions
- Crisis Harvest selection (smallest absolute gap to threshold among lots below threshold) as a query over lots
- The Harvest Reserve and its relationship to realized P/L
