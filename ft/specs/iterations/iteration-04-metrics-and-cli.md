# Iteration 04 — Metrics & CLI

**Goal:** score forecasts on a holdout and ship an operator-facing command.

**Depends on:** Iteration 03

## Stories

- **D1** MAE / RMSE / MAPE on a holdout. _(M, 2)_
- **D2** CLI with `--data/--window/--horizon/--k/--out`. _(M, 3)_
- **D3** JSON report. _(S, 2)_

## Acceptance criteria

**D1 — Given** `actual=[1 2 3]`, `pred=[2 4 6]`,
**then** `MAE = 2.0`, and `RMSE([0 0 0],[3 3 3]) = 3.0`.

**D2 — Given** defaults, **when** I run `clojure -M:run`,
**then** it prints one block per symbol (holdout metrics, top periods, next-24h forecast).

**D3 — Given** `--out report.json`,
**then** a valid JSON file is written with one result object per symbol.

## Tasks

1. `src/ft/metrics.clj`.
2. `src/ft/main.clj`: `parse-args`, `analyse`, `->json`, `-main`.
3. Fix: `:trend_per_hour` must read `(:b model)`, not `(:b (:a model))`.

## Split design (holdout vs forecast)

- **Holdout:** fit on `[split-window, split)`, predict `[split, split+horizon)`.
- **Forecast:** refit on the most recent `window` points, predict beyond the data.
- This keeps evaluation honest (no test information used to build the model).

## Review

**Shipped:** D1, D2, D3. Example run (horizon 24): MAPE ≈ 2.1–2.8% per symbol.
**What changed:** caught and fixed the trend-field typo above before the first
successful run.
**Backlog impact:** added **F3** (export forecasts to CSV) so QFT can compare.
