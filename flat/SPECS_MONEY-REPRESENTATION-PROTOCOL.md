# Money Representation Protocol

**Status:** Binding protocol for the next implementation stage (Datomic migration).
**Date:** 2026-10-06 (Halifax)
**Applies to:** all teammates — Claude, ChatGPT, Gemini, any other model, and the human operator. "The AI stored it as a float" and "the human typed 36.79" are equally non-exemptions.

## Why this exists

The current Google Sheet book stores money as decimal values and truncates on
display. During a reconciliation we found the only full-precision anchor we had
was the Binance wallet reading `73.57980772` USDC; every other input (box count
`12.47`, booked buys summing `65.08`) was **truncated, not rounded** — the lost
decimals are unrecoverable data loss. This document fixes how money is
represented so that class of loss cannot recur in the new model.

## The rule

**Never store money as a floating-point number.** Binary floats cannot
represent decimal fractions like 0.10 exactly, so they drift. No money value in
the system is ever a `float`/`double`.

## The representation: integer-with-scale (fixed-point)

Store every monetary amount as:

- an **integer** count of the asset's smallest unit (the *minor unit*), plus
- an explicit **scale** = the number of decimal places that asset uses.

Examples:

| Human value | Asset | Scale | Stored integer |
|---|---|---|---|
| $36.79 | USD | 2 | 3679 |
| 73.57980772 USDC | USDC | 8 | 7357980772 |
| 1.5 ETH | ETH | 18 | 1500000000000000000 |

All arithmetic (sums, postings, balances) is performed on the integers, which
is exact. Division by `10^scale` happens **only at display**, never in storage
or calculation.

- **Scale is per-asset**, carried as data, not assumed. USD = 2, USDC = 8,
  ETH = 18. A dollars-only "work in cents" convention is a special case of this
  with scale fixed at 2; it is insufficient for crypto, so the general
  integer-with-scale form is the protocol.
- Databases: use `DECIMAL`/`NUMERIC` with explicit precision and scale, never
  `FLOAT`. Code: arbitrary-precision decimal / BigDecimal / Python
  `decimal.Decimal`, or a dedicated money type. Never native floats.

## Money as a value object

An amount is never a bare number. It is an indivisible triple:

```
{ integer_amount, asset, scale }
```

Postings are immutable and signed; a balance is an **exact integer sum over the
event log**, computed on demand — not a stored, hand-edited cell. This matches
the event-ID ledger direction (CRT/CRF/CRP/CORR/TRD/STT/STF/STR...) and the
"a balance is a query, not a scan" principle.

## Rounding and data loss

- **Round only at display, or at a legally/venue-defined settlement step** —
  never in intermediate arithmetic.
- Distinguish **truncated** from **rounded** inputs. A value like `12.47` whose
  further decimals are unknown is truncated: record it as-is, do **not** pad
  with false zeros (`12.47000000`) and do **not** back-solve the missing
  decimals.
- When an amount is reconstructed from truncated inputs, mark it in the posting
  note as carrying known data loss, and instruct that it be re-anchored only
  from a fresh full-precision reading (wallet/venue), never "fixed" by inventing
  decimals. (See STR-0001 in the Trades-October ledger for a worked example.)

## Carry-forward for the Datomic schema

- Each amount attribute stores an integer plus an explicit scale attribute.
- Each posting: event id, timestamp (Halifax/Paramaribo convention), asset,
  signed integer amount, scale, method, related event, note.
- Balances are queries (sum of signed integers for an asset), formatted to the
  asset's scale only when presented to a human.
- A "precision provenance" marker per amount: full-precision vs truncated-input,
  so data loss is visible and never silently repaired.
