# Iteration 01 — Data ingestion & project skeleton

**Goal:** stand up a runnable tools.deps project and read the synthetic CSV.

**Duration:** small (half-day equivalent)
**Depends on:** `../../samples/trading_data.csv`

## Stories

- **A1** Load the CSV into plain data. _(M, 2)_
- **A2** Return one symbol's series in file order. _(M, 1)_
- **A3** Parse numeric columns as doubles. _(M, 1)_

## Acceptance criteria

**A1 — Given** the file has a header row,
**when** I call `(ft.data/load-rows path)`,
**then** I get a vector of maps keyed by `:timestamp :symbol :open :high :low :close :volume`.

**A2 — Given** rows for several symbols,
**when** I call `(ft.data/series-for rows "AAPL")`,
**then** I get only AAPL rows, in the same order as the file.

**A3 — Given** a close value `"262.476002"`,
**when** parsed,
**then** it is the double `262.476002`.

## Tasks

1. Create `deps.edn` with paths, deps (`data.csv`, `commons-math3`), and `:run`/`:test` aliases.
2. Add `src/ft/data.clj`.
3. Add `.gitignore` for `.cpcache/`, `target/`, `out/`.

## Technical notes

- `org.clojure/data.csv/read-csv` returns lazy seqs of strings; realise with `mapv`.
- Keywords come from the header row, so column order is not hard-coded.

## Review

**Shipped:** all three stories. `load-rows`, `symbols`, `series-for` in `src/ft/data.clj`.
**What changed:** none to the plan.
**Backlog impact:** none.
