# Decision — Carried open facts: documented, not resolved by import

**Date:** 2026-10-04
**Status:** Accepted (closes migration blocker #6 — carried open facts)
**Context:** Voice working session on the Datomic migration. Blocker #6 is unlike
the others: it is not a defect to fix before migrating, but a set of known
irregularities that must **ride alongside** the migration as acknowledged, owed
facts — never silently imported, never silently dropped.

## Decision

The migration **carries** the following three open facts. Each is recorded
explicitly, with its value, and marked **acknowledged and owed** — not resolved by
the act of import. They do not block the migration; they are exceptions the book
stays honest about.

1. **Accidental TAO reverse convert.** A convert that happened but was outside the
   experiment's intent. Recorded as a real event, flagged as unintended, excluded
   from experiment performance until reviewed.

2. **4.36637774 USDC outside the experiment.** Cash present but outside the
   experiment's scope. Recorded at full precision, flagged out-of-scope, and kept
   out of experiment reconciliation totals.

3. **ORCL average-cost review.** The ORCL lot's average cost is still pending
   review. Carried as an open question against that lot, not closed by assuming the
   current figure is correct.

## Consequences

- Each fact is modelled as an explicit, queryable marker in the book (an event
  flag or an open-question attribute on the relevant lot), so it surfaces rather
  than hides.
- Reconciliation must **exclude** the out-of-scope USDC and the unintended TAO
  convert from experiment totals, by flag, not by deletion.
- These remain open after migration. Closing them is follow-up work, tracked
  separately; the migration's job is only to carry them faithfully.
- Consistent with the project principle: the book of record records *what actually
  happened*, including the irregular, and never launders an irregularity by
  importing it as if clean.
