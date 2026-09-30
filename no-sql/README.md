# Trading Book · Stock Trades (JSON export)

`stock-trades.json` is a one-to-one conversion of the **Trades** tab (stock event log, columns A:M, rows 2–25) of the Google Sheet *TRADING BOOK*, as of 2026-09-30. It contains 24 events: MIG-0001…MIG-0006, TRD-0007…TRD-0023 and BOOK-0001.

The Google Sheet remains the bookkeeping source of truth. This file is a snapshot for moving the event log into MongoDB, not a replacement for the sheet.

## Format

A JSON array in MongoDB Extended JSON (relaxed), one document per line, ready for `mongoimport`:

```bash
mongoimport --uri "$MONGODB_URI" --db porketo --collection stock_trades \
  --file no-sql/stock-trades.json --jsonArray
```

- `_id` is the sheet's Event ID, so re-importing the same event is rejected as a duplicate instead of silently creating a second copy.
- Money, prices and units are `{"$numberDecimal": "..."}` (Decimal128), so values like `0.10` don't pick up floating-point error.
- `executedAt` is a `{"$date": ...}` in UTC, converted from ART (UTC−3).

## Field mapping

| Sheet column | JSON field | Notes |
|---|---|---|
| Event ID | `_id`, `eventId` | |
| Executed At (ART) | `executedAt`, `executedAtRaw` | `executedAtRaw` keeps the original text. |
| Ticker | `ticker` | |
| Action | `action` | |
| Converted Amount ($) | `convertedAmount` | |
| Broker Price ($) | `brokerPrice` | |
| Units | `units` | |
| Fees / Friction ($) | `feesFriction` | |
| Reason | `reason` | |
| Related Event | `relatedEvent` | `null` when blank. |
| Notes | `notes` | Verbatim. |
| Cash Flow ($) | `cashFlow` | |
| Signed Units | `signedUnits` | |

Added fields, derived only from the row itself:

- `eventType`: `migration` (MIG), `trade` (TRD) or `bookkeeping` (BOOK), from the ID prefix.
- `book`: always `stocks`, to keep this collection distinguishable from a future crypto trades collection.
- `executedAtPrecision`: `minute` when the sheet has a time, `day` when it has only a date (BOOK-0001 "post-session"), `unknown` when blank (MIG rows). `executedAt` is `null` unless the precision is `minute`.
- `executedDate`: the ART calendar date when known.
- `brokerTransactionId`: extracted from the Notes when a transaction ID is written there; otherwise `null`.
- `source`: workbook, sheet and original row number, for tracing a document back to the sheet.

## Precision caveat

Values are the sheet's **displayed** values (units to 6 decimals, cash to 2). Full-precision figures that appear only in Notes (e.g. 0.04416961 NVDA, TRD-0007's $0.0055 friction) were not substituted into the numeric fields. Check: the `cashFlow` values sum to −148.10, which against the $150.00 stock budget gives the $1.90 total cash shown in Positions.
