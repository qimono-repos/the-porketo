# Decision: Absent Is Not Zero — Reconcile Multi-Source Prices by the Median of Present Sources

- **Date:** 2026-10-04
- **Status:** Active standing rule
- **Scope:** Any cell fed by several named price sources (currently the three
  columns Price — Yahoo Finance, Price — CoinGecko, Price — CoinMarketCap on the
  Crypto Positions and Stock Summary tabs). Applies to decision-reference prices,
  not booked execution values (those still come only from the real receipt).

## The problem we hit

We began filling three named source columns per asset. For some assets a source
returned no clean quote (e.g. Yahoo had no match for SLP or GALA). The first
reflex was to put **0** in the empty slot. That is wrong, and dangerously so:

- **Zero is a real quantity; absence is not.** A price of 0 is a specific claim —
  "this asset is worthless / the coin is broke." For SLP that is false: it trades
  fine on CoinGecko (0.000712) and CoinMarketCap (0.0007147); only Yahoo lacked a
  feed. A 0 in the Yahoo column tells a lie that looks like signal.
- **A false zero corrupts every downstream calculation.** Any average across the
  three sources would be dragged toward zero, understating the asset.

"No value observed" and "the value is zero" are different claims. They must never
share a representation.

## This is a standard data-science problem (context, for the record)

What we rediscovered at the kitchen table is an everyday problem in big data,
machine learning and data science: **missing-data handling**. Before most models
can train, the gaps must be resolved, because many algorithms refuse to run with
them. The step that fills or works around a gap is called **imputation**.

**Why is it missing? (the taxonomy)** Data scientists first classify the
mechanism of absence:

- **MCAR — Missing Completely At Random.** The gap is unrelated to the value
  itself (Yahoo simply had no feed). Benign. Our SLP/GALA case is essentially
  this.
- **MAR — Missing At Random.** The gap depends on something else we *do* observe.
- **MNAR — Missing Not At Random.** The absence is *caused by* the hidden value —
  e.g. an asset too dead to be quoted. This is the case a naive 0 would wrongly
  imply, and the one to stay alert to.

**How to fill it (the tools), weakest to strongest for our shape of data:**

- **Mean imputation** — fill with the average of the present sources. Simple and
  the textbook first move, but it *shrinks variance*: with only three sources,
  one fill is a third of the row, so it artificially tidies the data and hides
  real disagreement.
- **Median imputation** — fill with / use the median of the present sources.
  Resists outliers by construction. **Best fit for us** (see below).
- **K-Nearest-Neighbours imputation** — borrow from similar rows. Powerful with
  many features and many rows; overkill for 15 assets × 3 columns.
- **Multiple imputation** — model the uncertainty and generate several completed
  datasets. The most principled, but heavy machinery; the wiring costs more than
  it returns at this scale.

## Decision

1. **Absent is not zero.** If a source has no clean quote for an asset, its cell
   is recorded as **absent / unknown (null)**, never as 0. A 0 in a price column
   means a genuine observed zero and nothing else.
2. **Exclude the unknown, don't fill it with a lie.** An unknown is dropped from
   the reconciliation because it was never observed — a *different reason* from
   dropping an outlier (which is a value we have but distrust). Same action,
   different justification; keep the distinction explicit.
3. **Reconcile by the median of the present sources.** The reconciled decision
   price for an asset is the **median of the sources that actually have a value**.
   Rationale: the median handles *both* of our failure modes with one tool —
   - it ignores the **unknown** (we simply take the median of what's present), and
   - it shrugs off the **outlier** (e.g. AAVE Yahoo 97 vs CoinGecko 181 vs CMC
     179 → median 179, the bad quote can't drag it),
   without us having to pre-classify which problem a given row has.
4. **Fail closed.** If too few sources are present to form a trustworthy median,
   or the present sources cannot be reconciled into a confident figure, and the
   number would change a decision, do not act on it — wait for a better price.

## Representation note (to settle when we wire formulas)

Zero and "unknown" need distinct representations in the sheet so arithmetic can
tell them apart — the statistician's **0 vs NA/null**, or floating-point **NaN**
that deliberately poisons arithmetic so a missing value cannot hide. Exact
mechanism (blank cell treated as NA, an explicit sentinel, or a parallel
"source present?" mask) to be fixed when we implement the median formula, so that
"absent" never silently becomes 0 inside a SUM or AVERAGE.

## Related

- DECISIONS/strategy/2026-10-04-live-price-web-search-sources.md — names the
  web-search sources (with URLs) that feed these columns.
- DECISIONS/strategy/2026-10-03-price-reference-protocol.md — the parent protocol
  (two uses of price; Yahoo now / Binance later; drop-the-trailing-B mapping).
- DECISIONS/architecture/2026-10-04-everything-is-a-number-and-formulas-over-truncated-literals.md
  — "everything is a number" (no sentinel strings in numeric columns). This
  record refines it: the sentinel for *absence* must still be distinguishable
  from a true 0, i.e. NA/null, not a string and not a zero.
