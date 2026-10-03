# Decision — Databricks is a complementary analytics layer, not the book of record

**Date:** 2026-10-03
**Status:** Accepted (deferred to a later phase)
**Context:** Voice working session on database strategy for the-porketo.

## Decision

Databricks is adopted **in principle for a later phase** of the experiment as a
**complementary analytics, insights and dashboard layer** — explicitly **not** a
competitor to the book-of-record decision. The book-of-record priority remains
**Datomic** (immutable, time-travelling ledger; Clojure/Datalog fit; Nubank's
use in finance). Databricks sits on a different shelf: compute and analytics
**on top of** the record, not the record itself.

This is recorded today so it can be revisited later without re-deriving it.

## Why Databricks is a complement, not a competitor

- The earlier database shortlist (see `no-sql/examples/`) — **MongoDB Atlas,
  Datomic, Neo4j** — was about *where the immutable truth lives*. Databricks does
  not answer that question; it is a lakehouse analytics/compute platform.
- The pain driving the database move is **agentic access** — uneven read/write
  across different LLMs on a Google Sheet, plus Sheets quota limits. The book of
  record must give every agent clean, equal, first-class read/write. Databricks
  does not replace that need.
- Therefore the architecture is **two layers, two decisions**:
  1. **Book of record** — priority: Datomic. (Open candidates documented in repo.)
  2. **Analytics / insights / dashboard** — Databricks, later phase.

## Why Databricks specifically (operator motivation)

- Operator led a **Synapse → Databricks migration** at previous role; currently on
  sabbatical and wants to keep the skill sharp on a low-stakes project.
- Prior hands-on with **Parquet** datasets, Azure Data Factory, and early
  Databricks learning. This project is a deliberate practice ground.
- Finance affinity: analytics platform regularly visited, with a **dashboard** as
  the eventual best-fit surface for insights.

## Good use of Databricks for CSV data analysis (capabilities notes)

Captured as the "what it's for" register for the later phase:

- **CSV / flat-file ingestion:** read CSVs directly into DataFrames; infer or
  declare schema; land raw CSV in a bronze layer.
- **Parquet / Delta conversion:** convert CSV to columnar **Parquet / Delta
  Lake** for efficient, versioned analytical queries — operator's existing
  strength.
- **Medallion pattern:** bronze (raw trade/event CSVs) → silver (cleaned,
  typed, deduped on Event ID) → gold (aggregates: P/L, excess vs anchor,
  harvest-ready counts).
- **SQL warehouse + notebooks:** ad-hoc exploration and reproducible analysis
  over the event history.
- **Dashboards:** Databricks SQL dashboards as a candidate surface for the
  regular-visit insights view (equity curve, realized vs unrealized P/L,
  harvest cadence vs the 0.75/day target).
- **Agentic access:** Databricks managed **MCP servers** connect Claude (and
  Claude Code, Cursor) via **OAuth or PAT** through **Unity Catalog**. Not a
  one-click connector as of mid-2026 — add the managed MCP server URL manually;
  Azure may require workspace enablement and allow-listing the Claude IP under
  IP restrictions. This access is **read/analyse-first (Genie)**, reinforcing
  that Databricks is the analytics layer, not the writable source of truth.

## Consequences

- Revisit this in the next phase; until then, **no Databricks build work** — the
  priority is standing up the executive/book-of-record system in **Datomic**.
- When revisited, the writable source of truth stays elsewhere (Datomic/repo);
  Databricks ingests from it to produce insights and dashboards.

## References

- `no-sql/examples/DATOMIC-SKETCH.md`
- `no-sql/examples/LOT-IDENTITY-AND-GROUPING.md`
- `PROJECT_STATE.md`
