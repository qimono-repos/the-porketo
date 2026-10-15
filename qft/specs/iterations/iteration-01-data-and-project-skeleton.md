# Iteration 01 — Data ingestion & project skeleton

**Goal:** stand up a runnable `uv` project and read the synthetic CSV.

**Duration:** small (half-day equivalent)
**Depends on:** `../../samples/trading_data.csv` (shared with the `ft` sub-project)

## Stories

- **A1** Load the CSV into Python dicts. _(M, 2)_
- **A2** Return one symbol's series in file order. _(M, 1)_
- **A3** Parse numeric columns as `float`. _(M, 1)_

## Acceptance criteria

**A1 — Given** the file has a header row, **when** I call `qft.data.load_rows(path)`,
**then** I get a list of dicts keyed by `timestamp, symbol, open, high, low, close, volume`.

**A2 — Given** rows for several symbols, **when** I call `qft.data.series_for(rows, "AAPL")`,
**then** I get only AAPL rows, in the same order as the file.

**A3 — Given** a close value `"262.476002"`, **when** parsed,
**then** it is the `float` `262.476002`.

## Tasks

1. Create `pyproject.toml` (PEP 621) with deps (`qiskit`, `qiskit-aer`, `numpy`),
   the `dev` group (`pytest`), a `src/` layout, and the `qft` console script.
2. Add `src/qft/data.py` and `src/qft/__init__.py`.
3. Add `.gitignore` for `.venv/`, `__pycache__/`, `.pytest_cache/`, `out/`.
4. Pin the interpreter with `.python-version` (3.12) and commit `uv.lock`.

## Technical notes

- `csv.DictReader` yields dicts keyed by the header; column order is never
  hard-coded.
- `uv` manages the interpreter, so no system Python is required; `src/` layout
  means tests import the *installed* (editable) package.
- The dataset is byte-identical to the one `ft` reads, so results are directly
  comparable.

## Review

**Shipped:** A1, A2, A3. `load_rows`, `symbols`, `series_for` in `src/qft/data.py`.
**What changed:** `uv sync` initially failed because `pyproject.toml` declared a
`README.md` that did not exist yet — fixed by adding `README.md` before syncing.
**Backlog impact:** none.
