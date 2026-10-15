# Decision — The binding constraint is Sheets *access*, not model intelligence

**Date:** 2026-10-03
**Status:** Accepted (finding of record)
**Context:** Voice working session reviewing multi-LLM bookkeeping experience
across ChatGPT, Gemini and Claude on the Google Sheet book.

## The finding

After running the bookkeeping workflow across three vendors, the operator's
conclusion is that **the AI intelligence layer is not the bottleneck — access to
the Google Sheet is.**

- **Model carefulness has been excellent.** ChatGPT in particular has been
  effectively flawless and highly detailed at the bookkeeping — doing in minutes,
  reliably, the same reconciliation and double-checking that took the operator a
  full afternoon by hand. No clumsy-write problem occurred in practice.
- **The recurring failure is Sheets access.** Read/write access to the Google
  Sheet has been the struggle with **every** assistant tried: Claude, ChatGPT,
  and — most tellingly — **Gemini**. Google's own model struggling against
  Google's own spreadsheet is the strongest signal that the problem is the
  **surface**, not the model.

## Why this matters for the architecture

- It is **evidence, not theory**, for the agnostic-substrate decision. The
  experiment ran across three vendors; the constant that failed was always the
  Google Sheet surface.
- It **simplifies** the database choice. The goal is not a database to compensate
  for weak agents — the agents are capable. The goal is a substrate that **gets
  out of their way**: clean, equal, first-class read/write for any agent, with the
  least friction and no vendor quota wall.
- The repo already demonstrates the target property: **plain files in git** are
  read and written equally by every agent, with version history and no Sheets
  quota limit.

## Relationship to prior decisions

- Reinforces **Datomic as the protected book of record** (time-travel/audit fit,
  Clojure, Nubank-in-finance signal). As capital grows and this becomes the
  operator's primary personal-finance system, an immutable auditable ledger moves
  from "elegant" to "protective."
- Consistent with **Databricks as a later-phase analytics complement**, not a
  book-of-record competitor (see companion note).

## Scale context (why urgency is rising)

- This began as training wheels: hand-reading charts in trading apps (2024–2025),
  then a first Google Sheets automation, then the current event-sourced book.
- The "$150 experiment" is the **stock ticket only**; combined stocks + crypto
  invested capital is **already > $300** and intended to **keep growing until this
  is the operator's primary personal-finance system.**
- At that trajectory, the access constraint stops being an annoyance and becomes a
  **risk management** concern — motivating migration off Sheets as real money
  leans on the book.

## References

- `DECISIONS/architecture/2026-10-03-databricks-as-analytics-complement.md`
- `no-sql/examples/DATOMIC-SKETCH.md`
- `no-sql/examples/LOT-IDENTITY-AND-GROUPING.md`
