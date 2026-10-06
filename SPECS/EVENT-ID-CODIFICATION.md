# Event ID codification

How Event IDs in the book are coded. An ID is a **prefix** plus a **zero-padded
sequence number** (e.g. `CRF-0003`). The prefix marks the event *type*; the number
keeps the row uniquely identifiable. The prefix letters are a **codification**, not
an acronym with a fixed word expansion — read each row by its note, not by decoding
the letters. The expansions below are the intended meaning of each code, recorded so
the scheme is not reconstructed from scratch again.

## Crypto book (prefix starts `C`)

- **CRT** — Crypto TRade. A buy or sell of a crypto position.
- **CRF** — Crypto Funding / capital event. Moves capital into (or allocates within)
  the crypto pot — including an internal transfer from the stock pot to the crypto
  pot (see CRF-0004).
- **CFX** — Crypto FX conversion. A currency/asset conversion that is not a strategy
  trade (e.g. a stablecoin or coin-to-coin convert).
- **CRP** — Crypto Penalty. A rule penalty booked against the crypto pot.
- **CORR** — CORRection. A row that repairs or restores a previously mis-recorded or
  overwritten movement. Must carry the full corrected figures or a receipt reference.

## Stock / shared book

- **TRD** — TRaDe. A stock buy or sell.
- **MIG** — MIGration. A row seeded from an earlier migration of historical data.

## Mapping to the Datomic event types

The migration schema unifies both books by `:event/book` with these event types:
**trade, migration, bookkeeping, capital, FX, penalty, correction**. The ID prefixes
map onto them: CRT/TRD -> trade; MIG -> migration; CRF -> capital; CFX -> FX;
CRP -> penalty; CORR -> correction. Bookkeeping events are typed on the event, not a
distinct prefix.

## Rules

- Each Event ID is **unique** across its tab. Fail closed: no two rows share an ID
  (this is the first migration blocker — see `MIGRATION-TODO.md`).
- The sequence number runs **per prefix**, in order of booking where possible.
- The prefix is set by the **instrument/event nature**, independent of the
  settlement currency (a tokenised stock settling in USDC is still a stock event).
- When in doubt about what a row did, the **note** is authoritative, not the letters.
