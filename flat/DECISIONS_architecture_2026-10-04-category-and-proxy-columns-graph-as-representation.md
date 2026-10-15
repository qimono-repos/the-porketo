# Decision: Category and Proxy-For Columns on Both Books — Graph Is a Representation, Storage Is Arithmetic

- **Date:** 2026-10-04
- **Status:** Active standing structure
- **Scope:** The Positions (stocks) and Crypto Positions tabs of the book. Adds
  two structural columns to each — **Category** and **Proxy For** — and fixes the
  conventions that govern them.

## Why these columns exist

Two separate needs surfaced in the same session and turned out to share one
structure:

1. **Neighbourhoods for reconciliation (Category).** When we considered
   K-Nearest-Neighbours as a missing-data imputation method (see the
   absent-is-not-zero record), we found KNN on raw price is nonsense: SLP at
   0.0007 would be "near" dollar-scale coins and get an absurd fill. The fix is
   that the real neighbourhood is the **ecosystem / sector**, not the price. So
   category must be an explicit column — it *is* the KNN feature space, and it
   future-proofs the table as it grows from 15 to 40–70 assets.
2. **Leading indicators (Proxy For).** Some assets lead others. That is a
   relationship, not a flag, so it needs a column that records *what* a thing is
   a proxy for — not a mere Boolean "is a proxy".

## Category taxonomies (controlled vocabulary)

**Crypto (Crypto Positions):**
- L1: ETH, BTC, SOL, SUI, NEAR
- Gaming: RONIN, SLP, GALA, ILV, IMX
- DeFi/Infrastructure: LINK, AAVE
- AI: TAO
- Meme/Launchpad: PUMP
- Privacy: ZEC

Gaming is the project's primary crypto research priority (full-stack gaming
ecosystems). SLP's true neighbours are RONIN (its Ronin chain) and the Axie
Infinity ecosystem — not whatever trades near its price.

**Stocks (Positions):**
- Technology: AAPL, ORCL, AVGO, NVDA, FLKR
- Quantum: IONQ, QBTS
- Energy: CVX, OKLO, DUK
- Finance: HOOD, BLK
- EV/Auto: TSLAB
- Space: SPCXB

## The FLKR insight (the reasoning that belongs here, not in the sheet)

FLKR is the **Franklin FTSE South Korea ETF** — the Korea index in one ticker.
It is *not* a neutral geographic diversifier. Korea's largest businesses are
**SK Hynix and Samsung**, the memory/chip backbone, highly reactive to technology
broadly and AI in particular. So FLKR is effectively a **proxy for US tech /
Silicon Valley**, and categorised as Technology alongside AAPL, ORCL, AVGO, NVDA
(and future names like Micron).

Its special value is **temporal**: Korea's market opens ~8 p.m. New York time,
hours *before* Wall Street. So Samsung/SK Hynix trading overnight is a
**leading indicator** — a pre-US-open signal readable before the US session
starts. This narrative is the valuable part and lives here in the repo; the sheet
cell carries only the bare relation.

## Proxy structure — stocks vs crypto are asymmetric

- **Stocks have a temporal proxy.** FLKR leads because of time zones (markets
  open and close, so one can open first).
- **Crypto has no temporal proxy** — crypto never closes, so nothing opens
  "first." Instead crypto has a **hierarchical** proxy structure:
  - **BTC → the whole market** (market beta; alts follow Bitcoin).
  - **ETH → its ecosystem** (DeFi + gaming on Ethereum).
  - **SOL → its ecosystem**, **RONIN → the Ronin gaming ecosystem** (Axie, SLP).

## Self-proxy at distance zero — the null problem, dissolved

A blank "Proxy For" cell would be a missing-data representation — the very trap
the absent-is-not-zero record warns against. It is dissolved by an identity, not
a sentinel:

- **Every asset is a perfect proxy for itself.** SLP is a proxy for SLP; LINK for
  LINK. Reading the column as a **distance**, an asset that leads nothing sits at
  **distance zero from itself** — a genuine observed quantity, not an absence.
- Therefore the column is **total**: no nulls are possible by construction. The
  default is never blank or "none" — it is the asset's own identity.

## Representation vs storage — graph is the lens, arithmetic is the truth

- The relationship is naturally a **directed graph**: assets are nodes, "proxy
  for" is an edge, self-proxy is a loop. **But the graph is a *representation* —
  how we will read/visualise the structure later — not how we store it.**
- Storage obeys **"everything is a number"**: the cell records an **operation**,
  written with **`+`** (e.g. `SLP + SLP`, `BTC + Market`, `FLKR + US-Tech`), not
  an arrow. The arrow (`→`) was tried and rejected precisely because it encodes a
  graph representation into the stored value. Keep the store arithmetic; derive
  the graph from it when needed.

## As written in the sheet (bare relations only)

**Crypto Positions, column P "Proxy For":**
ETH + ETH-Ecosystem · LINK + LINK · AAVE + AAVE · IMX + IMX ·
RONIN + Ronin-Gaming · TAO + TAO · PUMP + PUMP · ZEC + ZEC · BTC + Market ·
SOL + SOL-Ecosystem · SUI + SUI · NEAR + NEAR · SLP + SLP · GALA + GALA · ILV + ILV

**Positions, column V "Proxy For":**
AAPL + AAPL · IONQ + IONQ · ORCL + ORCL · AVGO + AVGO · QBTS + QBTS ·
FLKR + US-Tech · NVDA + NVDA · CVX + CVX · OKLO + OKLO · HOOD + HOOD · BLK + BLK ·
DUK + DUK · TSLAB + TSLAB · SPCXB + SPCXB

Category columns: Crypto Positions column O; Positions column U.

## Related

- DECISIONS/strategy/2026-10-04-absent-is-not-zero-median-reconciliation.md — the
  KNN/neighbourhood discussion that motivated an explicit Category column, and the
  null-vs-zero principle this record applies to Proxy For (self-proxy = distance
  zero, not absence).
- DECISIONS/architecture/2026-10-04-everything-is-a-number-and-formulas-over-truncated-literals.md
  — "everything is a number"; here extended to: store operations (`+`), keep the
  graph as a derived representation.
