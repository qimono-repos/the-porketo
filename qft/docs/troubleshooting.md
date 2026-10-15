# QFT — Troubleshooting

## `uv: command not found`

`uv` is not installed or not on `PATH`. See the per-OS install docs
(`install-macos.md`, `install-linux.md`, `install-windows.md`). After installing
with the shell script, open a **new** terminal or `source ~/.local/bin/env`.

---

## `uv sync` fails to download Python or wheels (offline)

The first sync needs network access (managed Python 3.12 + wheels). If you are
offline:

- Pre-sync on a connected machine, then copy the `uv` cache and the project
  (with `uv.lock`) to the target:
  - Linux: `~/.cache/uv`
  - macOS: `~/Library/Caches/uv`
  - Windows: `%LOCALAPPDATA%\uv\cache`
- Then run `uv sync --offline` (or `uv run --offline ...`).

---

## `No module named qft` when running tests

Run through `uv` so the environment and editable install are in place:

```bash
uv sync
uv run pytest
```

Do **not** call the system `python`/`pytest` directly — they do not have the
project on their path.

---

## `unknown instruction: qft` (from `qiskit_aer`)

`AerSimulator` cannot execute the composite `qft` gate. Transpile first:

```python
tqc = transpile(qc, sim)
```

`qft.quantum.sample_qft` already does this. This only affects the `--shots` path;
the exact-statevector forecast is unaffected.

---

## `window length must be a power of two`

You passed a `--window` value that is not a power of two. Amplitude encoding
needs `N = 2^n`. Use 128, 256, 512, 1024, … (The default, 512, is fine.)

---

## `DeprecationWarning: ... qiskit.circuit.library.basis_change.qft.QFT is deprecated`

You imported the old `QFT` class. Use `QFTGate` instead:

```python
from qiskit.circuit.library import QFTGate   # correct
```

The project already uses `QFTGate`.

---

## Forecast looks "flat" or trivially tracks the trend

Too few components. Increase `--k` (e.g. `--k 16`). Conversely, if the forecast
is wild, reduce `--k` — large `k` fits noise and destabilises extrapolation.

---

## `--horizon` implies a window longer than the data

`analyse` needs `total − horizon ≥ window`. With 1024 samples per symbol,
`window + horizon` must be ≤ 1024. If you raise `--window` to 1024 you must lower
`--horizon`.

---

## Forecast drifts away over long horizons

This is expected for **trended** windows: linear detrending leaks a sliver of a
phase-shifted signal, so the extrapolated line component can drift. Exact
extrapolation holds only for **trend-free periodic** signals — this is documented
and tested (`specs/iterations/iteration-03-prediction-model.md`). For long
horizons, use a smaller `k` and a shorter horizon.

---

## CSV path errors

Run from the `qft/` directory, or pass an absolute path:

```bash
uv run qft --data /full/path/to/trading_data.csv
```

---

## Results differ from the `ft` (Clojure) sub-project

They should not: for the same `--window`, `--horizon`, `--k`, the holdout
metrics are identical, because the QFT reproduces the classical DFT to `1e-9`.
If they differ:

- confirm `uv.lock` is intact (`uv sync` should not change versions);
- confirm both runs use the same window/horizon/k;
- re-run `uv run pytest` — the DFT-equality tests will localise a regression.

---

## Verbose / filtered test runs

```bash
uv run pytest -v                       # per-test verbose
uv run pytest -k predict              # only tests matching "predict"
uv run pytest tests/test_quantum.py   # one file
```
