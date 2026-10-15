# Decision — "Everything is a number": strong typing, and formulas over truncated literals

**Date:** 2026-10-04
**Status:** Accepted (standing principle for the book and the migration)
**Context:** Voice working session on the Datomic migration, while adding the
`Receipts per Share` column to the stock `Trades` tab and discussing fee precision.

## Decision

Three linked principles, in the project's ubiquitous language.

### 1. Everything is a number

As object-oriented design says "everything is an object," in this book
**everything is a number.** Each quantitative column has a numeric contract and
holds *only* numbers — never sentinel strings like `TBD` that break the type. A
missing-but-owed value is represented numerically (e.g. a reference default), not
by a foreign type.

### 2. Reference limits, not guesses

Where a value tends toward a reference, store that reference as its default and
treat deviations as the real data. Example: `Receipts per Share (ref. limit = 1)`.
A CEDEAR tends one-to-one toward its underlying share (the calculus notion of a
**limit**), so the column defaults to `1`; triangulation then records how far a
given ticker departs (tech names often 10:1 or 20:1). DUK confirmed at `1`
empirically (receipt price ~118.97 vs real DUK ~114–117 in the same window).

### 3. Formulas over truncated literals

A cell may hold a **formula** instead of a literal; it still satisfies the numeric
contract because it *evaluates* to a number. Prefer the formula wherever a
displayed value hides precision.

- **Why it matters:** Binance (and brokers) display fees truncated — e.g. a real
  sub-penny fee shows as `0.00`. Storing the literal `0.00` bakes the rounding
  error in permanently; the fee silently becomes nothing.
- **The fix:** store *how the fee is derived* (rate × notional) so the cell computes
  the true value at full precision, below the display's resolution.
- **The payoff — summability:** when each fee is a faithful formula, the **sum**
  over all fees is exact. Dozens of fees each shown as `0.00` would total zero as
  literals, but as formulas they sum to a real, material drag on the harvest. Honest
  at the cell, honest at the aggregate.

This directly serves the migration **precision** blocker: carry receipt-level
precision, not displayed precision. The guiding spirit: **we can do better** than
accept the display's lie.
