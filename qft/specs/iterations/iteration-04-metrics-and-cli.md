# Iteration 04 — Metrics & CLI

**Goal:** score forecasts on a holdout and ship an operator-facing command.

**Depends on:** Iteration 03

## Stories

- **D1** MAE / RMSE / MAPE on a holdout. _(M, 2)_
- **D2** CLI with `--data/--window/--horizon/--k/--shots/--out`. _(M, 3)_
- **D3** JSON report. _(S, 2)_

## Acceptance criteria

**D1 — Given** `actual=[1 2 3]`, `pred=[2 2 2]`, **then** `MAE = 2/3`;
`RMSE([0 0],[1 1]) = 1.0`; `MAPE([100,200],[110,180]) = 10.0`; zero actuals are
skipped.

**D2 — Given** defaults, **when** I run `uv run qft`, **then** it prints one block
per symbol (qubits, holdout metrics, top periods, next-24h forecast).

**D3 — Given** `--out report.json`, **then** a valid JSON file is written with one
result object per symbol.

## Tasks

1. `src/qft/metrics.py` (NumPy-vectorised).
2. `src/qft/main.py`: `build_parser`, `analyse`, `main`; `[project.scripts] qft`.
3. Support `--shots` (adds sampled top states to output and JSON).

## Split design (holdout vs forecast)

- **Holdout:** fit on `[split−window, split)`, predict `[split, split+horizon)`.
- **Forecast:** refit on the most recent `window` points, predict beyond the data.
- This keeps evaluation honest (no test information used to build the model).

## Determinism

The forecast uses the **exact statevector**, so it is deterministic. The
`--shots` path uses `seed_simulator=1234` so its sampled output is reproducible
too.

## Review

**Shipped:** D1, D2, D3. Example run (horizon 24): MAPE ≈ 2.1–2.8% per symbol,
**identical** to the `ft` sub-project.
**What changed:** the JSON report's top-level `model` tag is `"qiskit-qft"` (vs
`ft`'s `"detrended-radix2-fft"`), making reports self-describing. Added the
`--shots` flag as a small extra (not in the `ft` CLI) to expose the measurement
statistics.
**Backlog impact:** added **F3** (export forecasts to CSV) for direct diffing
against `ft`.
