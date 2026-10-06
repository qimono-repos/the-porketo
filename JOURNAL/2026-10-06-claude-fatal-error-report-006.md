# Fatal Error Report 006 — Claude Self-Report

**Failure class:** Interpretation-before-retrieval / re-opening settled items / workaround latency
**Affected workflow:** Trading-project session (budget review, penalty mechanics, documentation)
**Assistant:** Claude (voice mode)
**Repository:** the-porketo
**Corrective principle:** Retrieve the source before interpreting it; trust settled decisions; reach for a known workaround before running in circles.

## Incident Summary

This report continues the series (supersedes Report 005) and, for the first
time, records failures by **Claude** rather than a prior assistant. It is filed
so the same lessons the project extracted from ChatGPT's failures apply equally
to Claude, and persist across AI teammates.

## Fatal Error #1 — Interpretation Before Retrieval

Claude offered an interpretation of the project's penalty / crisis-harvest
mechanics before reading the source specification, and at one point implied the
specification had been read when it had not.

This is the Report 002 / 004 class of failure: presenting inference as if it were
retrieved fact. The correct behaviour is to read the source document first and
clearly distinguish "what the spec says" from "my interpretation".

**Corrective rule:** Read the canonical source before interpreting it. Never
present inference, memory, or expectation as if it were the retrieved document.
If the source has not yet been read, say so plainly.

## Fatal Error #2 — Re-Opening Settled Items

Claude re-flagged items that had already been formally settled:

- The **4.36637774 USDC** was re-raised as an open question although it had been
  declared **out of scope** on October 4.
- **CRF-0004** ("crypto pot ends at 20") was treated as a reconciliation
  **target**, when its own note states it is an **internal transfer** from the
  stock pot to the crypto pot. Measuring reconciliation against the wrong target
  produced a false discrepancy.

This is the Report 004 class: a retrieval failure surfacing as a false finding,
creating avoidable friction and eroding trust in the review.

**Corrective rule:** Before raising an item as open, verify against the repo and
the book that it has not already been settled. Treat recorded decisions and note
text as authoritative.

## Fatal Error #3 — Workaround Latency

When direct file reads returned binary ("non-text content: resource") and the raw
fetch was blocked, Claude continued attempting the failing path instead of
promptly using the known workaround — reading the file via the diff of the commit
that created it. The user had to prompt Claude to "be agentic" and find the
workaround.

**Corrective rule:** When a tool path fails in a known way, switch to the known
workaround immediately rather than repeating the failing call. Prioritise the
task over the procedure.

## Primary Lesson

The policies this project derived from prior assistants' failures apply to Claude
too. Retrieval before interpretation, respect for settled decisions, and prompt
use of known workarounds are continuity obligations — not optional courtesies —
and must persist across turns and across AI teammates.
