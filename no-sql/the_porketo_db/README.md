# the_porketo_db — the trade book from November 2026

From **1 November 2026** every booked event (stocks *and* crypto, one stream) goes into
MongoDB Atlas, not the Google Sheet.

| | |
|---|---|
| Atlas org / project | Qimono / the-porketo |
| Cluster | `the-porketo-nosql` |
| Database | `the_porketo_db` |
| Collection | `trades` (the only one for now) |
| October and earlier | stays in the Google Sheet, now **archive / sample**. Not migrated. |

The Sheet tabs `Trades-October` (stocks) and `Crypto Trades` (crypto) had almost the same
columns. `trades` keeps those columns and merges the two books with `assetClass`.

## Files

- `trades.validator.json` — the `$jsonSchema` validator (strict, rejects bad inserts).
- `setup.mongosh.js` — creates or updates the collection, validator and indexes. Idempotent.
- `example-trade.json` — one illustrative document (not a real fill).

## Setup state (2026-10-31)

- Database, collection and the 5 indexes below were created on the cluster.
- **The validator still has to be attached** (the tool used to create the collection could
  not set it). Do one of:
  - Atlas → Data Explorer → `the_porketo_db.trades` → **Validation** tab → paste the
    contents of the `$jsonSchema` object from `trades.validator.json`, action *Error*, level *Strict*.
  - or `mongosh "$MONGODB_URI" --file no-sql/the_porketo_db/setup.mongosh.js` from the repo root.

## Field mapping (Sheet column → field)

| Sheet column (Trades-October / Crypto Trades) | Field | Type |
|---|---|---|
| Event ID | `_id` | string `EVT-0001`, `EVT-0002`, … (one sequence for everything) |
| Executed At (Halifax/Paramaribo / ART) | `executedAt` (UTC date) + `executedAtLocal` (text as on receipt) + `executedAtPrecision` | date / string / `second`·`minute`·`approx`·`day` |
| — (new) | `assetClass` | `stock` · `crypto` · `cash` |
| Asset | `asset` | string, ticker as held (TSLAB, MU, BTC, USDC) |
| — (was "Proxy For" in Notes) | `underlying` | string or null (TSLAB → TSLA) |
| Action | `action` | `BUY` `SELL` `FUND` `WITHDRAW` `RECON` `CORRECTION` `PENALTY` `FX` |
| — (new) | `harvest` | bool, true when a SELL is a harvest |
| — (new) | `lotId` | `TICKER@price!!yyyyMMddHHmmss` — lot opened (BUY) or drawn from (SELL) |
| Quote Asset | `quoteAsset` | string |
| Report Amount / Anchor (USDC eq.) | `anchorUsdc` | decimal |
| Execution Price (native quote) | `executionPrice` | decimal |
| Units | `units` | decimal |
| Signed Units | `signedUnits` | decimal (+ buy, − sell) |
| Fee Asset + Fee Qty | `fee: {asset, qty}` | object |
| Platform (crypto tab) | `venue` | Binance, Lemon Cash, Robinhood… |
| Method | `method` | Binance Convert, Binance Stocks (market)… |
| — (was in Notes) | `venueOrderId` | Order No. / Tx id, if any |
| Related Event | `relatedEvents` | array of strings |
| Notes | `notes` | string |
| USDC-eq Portfolio Cash Flow | `usdcEqCashFlow` | decimal |
| USDC Wallet Flow | `usdcWalletFlow` | decimal |
| USDT Wallet Flow | `usdtWalletFlow` | decimal |
| Tier (at slot) | `tier` | string |
| Trading slot # (e.g. `20`, `11–18`) | `slots: {first, last}` | ints; one slot → first == last |
| Forecast Range / Forecast Value / Target Time / Result / Square Error / SPE | `forecast: {range, value, targetTime, result, squareError, spe}` | object |
| — (new) | `bookedAt`, `bookedBy` | when and by whom the document was written |

Required: `_id, executedAt, executedAtLocal, assetClass, asset, action, venue, method, anchorUsdc, usdcEqCashFlow`.
Extra fields are allowed.

## Booking rules

- **Money, prices and units as Decimal128** (`{"$numberDecimal": "0.00355672"}`, or
  `NumberDecimal("…")` in mongosh). The validator also accepts plain numbers so a hand insert
  from Data Explorer is not blocked, but decimals are the norm. Never round or truncate a
  receipt figure.
- **Append-only.** A mistake is fixed with a new `CORRECTION` event that points at the
  original in `relatedEvents`, not by editing history.
- **Time**: November slots follow Paramaribo time (UTC−3). Store `executedAt` in UTC and
  keep the receipt text in `executedAtLocal`.
- **November cadence**: 6 checkpoints/day (every 4 h), 2 units × 0.75 = **1.50 USDC per slot**.
  `slots` numbers count from 1 within the exercise (see the Sheet's `Slots` tab for October).
- Tokenized stocks (…B on Binance) are `assetClass: "stock"` with `underlying` set.
- USDC/USDT funding, transfers and reconciliations are `assetClass: "cash"`.

## Handy queries

```js
use the_porketo_db
db.trades.find().sort({ executedAt: -1 }).limit(5)                    // latest moves
db.trades.find({ assetClass: "crypto" }).sort({ executedAt: -1 })     // crypto only
db.trades.find({ asset: "TSMB" }).sort({ executedAt: 1 })             // one asset's history
db.trades.find({ "slots.first": { $lte: 12 }, "slots.last": { $gte: 12 } }) // what paid slot 12
db.trades.aggregate([{ $group: { _id: "$assetClass", cash: { $sum: "$usdcEqCashFlow" } } }])
```

## Indexes

`_id` (event id), `executedAt_desc`, `asset_executedAt`, `assetClass_executedAt`, `lotId`, `slots_first`.
