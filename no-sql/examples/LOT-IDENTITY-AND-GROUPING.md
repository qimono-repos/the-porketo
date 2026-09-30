# Lot identity and grouping

Companion to `LOT-ORCL-1.md`. Written 2026-09-30 from a conversation about domain-driven design and how the lot model supports flexible grouping.

## The investment thesis, stated precisely

The unit of investment is **not** a ticker. It is a ticker at a given price at a given moment:

> I am not investing in ORCL. I am investing in **ORCL at 157.18, opened 2026-09-10**.

Two buys of the same ticker on different days at different prices are genuinely different investments. This is the reason behind the existing sprint rule: *same ticker may have multiple lots; never blend their material anchors.*

## Consequence: the triple is the natural key

`ticker` + `entryPrice` + `openedDate` is the lot's **natural key**, not a decorative label.

`label` ("ORCL Lot 1 @ 157.18") stays in the document, but only as a human-readable caption. It is never the identity and is never parsed.

**Critical rule: store the three components as separate, indexed fields.** Never bake them into a single string. A string cannot be sorted, ranged or filtered on its parts; three fields can.

## DDD roles

| Concept | Role | Why |
|---|---|---|
| **Lot** | Aggregate root | Owns the invariants: net units never negative, material anchor immutable once set, harvest only fires above threshold. All checkable within one lot. |
| **Ticker** | Value object | No identity, immutable. (Promote to an `Asset` entity only if sector/thesis need a single home shared by many lots.) |
| **Mark** (price + time + source) | Value object | Immutable; never updated, only recorded anew. Embedded in the lot. |
| **Sprint** | Bounded context / lightweight root | Holds window, budget, mark timestamp. *Not* an aggregate containing all lots — that would lock the whole portfolio to record one harvest. |
| **Events** | Ledger | Append-only facts, referenced by ID from the lot, never nested inside it. |

Aggregate = transactional boundary; document = Mongo's transactional boundary. That correspondence is why the mark is embedded rather than given its own collection.

### Why value objects are embedded, not collected

Default: embed. A value object has no identity to look it up by, and nothing else references it. A separate collection would force joins for data stored in one place.

Break the rule only when (a) it turns out to be an entity many documents reference and update centrally, or (b) volume is large enough to threaten the document size limit — e.g. a continuous price feed. Neither applies here: one mark per lot per sprint.

Note: being *read* from many places (reporting, search, calculation) does not justify a separate collection. Indexed embedded fields serve all of those without joins.

## Grouping: many lenses, no stored groups

Groups are **not** stored and have no identity. A group spanning several lots cannot be an aggregate, because a transaction should not span aggregate boundaries.

Instead a group is a **specification** — a named rule — and in MongoDB a specification *is* a query. Store the rule, run it, get the current members.

Because the triple is three indexed fields, each grouping is one query:

| Grouping | Query |
|---|---|
| First three ORCL lots | match `ticker`, sort `openedDate` ascending, limit 3 |
| ORCL lots near 157 | match `ticker`, range on `entryPrice` |
| Everything opened in September | range on `openedDate`, ignore ticker |
| All lots above harvest threshold | computed comparison across all open lots |

If a group action is executed (e.g. harvesting three lots at once), record an **event listing the participating lot IDs**. That preserves the audit trail of the result, without persisting the grouping itself.
