# Reference example — `lots` collection: ORCL Lot 1 @ 157.18

Canonical example of a document in the `lots` collection, agreed on 2026-09-30 while designing the migration of the TRADING BOOK Google Sheet to MongoDB Atlas. Use this as the reference shape in future conversations.

Source: Sep 15 Sprint, row `3A` (ORCL Lot 1 @ 157.18). Numbers are shown as plain JSON for readability; the real import uses `{"$numberDecimal": "..."}` for money, prices and units, as in `no-sql/stock-trades.json`.

```json
{
  "_id": "LOT-ORCL-1",
  "label": "ORCL Lot 1 @ 157.18",
  "book": "stocks",
  "ticker": "ORCL",
  "sprintId": "SPRINT-2026-09-15",
  "thesis": "Earnings exposure",
  "catalystDate": "2026-09-10",

  "openedBy": "MIG-0003",
  "eventIds": ["MIG-0003", "TRD-0009"],

  "materialAnchor": 15.00,
  "targetProfit": 0.10,
  "entryPrice": 157.18,

  "netUnits": 0.092152,
  "status": "OPEN",
  "lastHarvestHour": "2026-09-09T15 NY",

  "mark": {
    "price": 141.32,
    "markedAt": "2026-09-24T04:00:00Z",
    "source": "manual"
  }
}
```

## The three kinds of fields

**Identity and strategy** (`_id` through `entryPrice`) — set once when the lot is created, never changed afterwards. The immutable material-anchor rule lives here: no rebuild process may touch `materialAnchor`.

**Derived from events** (`eventIds`, `netUnits`, `status`, `lastHarvestHour`) — recomputed by replaying the events linked to the lot. MIG-0003 bought 0.095432 units and TRD-0009 sold 0.003280, so `netUnits` = 0.092152. If a lot ever disagrees with the event log, rebuild it from the events; never hand-edit the lot. `lastHarvestHour` is the sheet's **Epic** column.

**The mark** — the price snapshot for this lot within its sprint. Prices come from Yahoo Finance / Binance at query time; Mongo stores only the snapshot that a decision was based on, as an audit trail.

## Deliberately NOT stored

`harvestThreshold`, `marketValue`, `excess`, `signal` are pure arithmetic over stored fields and are computed at query time, so they can never go stale or contradict their inputs:

```
harvestThreshold = materialAnchor + targetProfit    → 15.10
marketValue      = netUnits × mark.price            → 13.02
signal           = marketValue ≥ harvestThreshold ? HARVEST : WAIT   → WAIT
```

## Collection roles (SQL analogy)

| Collection | Role | Editable? |
|---|---|---|
| `events` | Event table — every buy, sell, harvest, capital addition, bookkeeping adjustment (stocks + crypto, split by `book`) | Append-only. Never edit history. |
| `lots` | Materialized view / projection rebuilt from events | Disposable; rebuild from events. Only identity/strategy fields are set by hand, at creation. |
| `sprints` | Closest to a lookup table — dated window, budget, mark timestamp | Set per sprint; archived when superseded. |

MongoDB does not enforce these roles. The discipline of which collection may be edited is a project rule, documented here.
