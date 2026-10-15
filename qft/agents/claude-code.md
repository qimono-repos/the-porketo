# CLAUDE.md — QFT (quantum Fourier price-prediction exercise)

> This file guides Claude Code when working inside `qft/`. It is the
> Claude-oriented view of the shared brief in `README.md`.

## Mission

Maintain and extend the **qft** sub-project: a price forecaster that replaces the
classical FFT of the `ft` (Clojure) sub-project with a **Quantum Fourier
Transform** (Qiskit). Input is a **synthetic** hourly CSV; output is a
short-horizon forecast plus holdout error metrics per symbol.

## Commands

```bash
uv sync                                         # resolve/create .venv (first run)
uv run pytest                                   # MUST be green before you finish
uv run qft --data ../samples/trading_data.csv --horizon 24
uv run qft --shots 4096 --out out/report.json
```

## Working style (for Claude Code)

- **Plan, then act.** For non-trivial changes, outline the plan first; keep edits
  scoped to one iteration.
- **Explore in a REPL.** `uv run python` drops you into the environment; import
  `qft.quantum`, poke at a circuit, then write the test that captures what you
  learned. We validated the entire QFT convention this way before writing code.
- **Read before writing:** `src/qft/data.py`, `quantum.py`, `predict.py`,
  `metrics.py`, `main.py` (in that order) mirror the data → spectrum → model →
  score → CLI pipeline.
- **Use the todo/plan tooling** to track multi-file changes.

## Code conventions

- Package is `qft` under a **`src/` layout** (`src/qft/`); tests import the
  installed (editable) package, never a relative path.
- Add `from __future__ import annotations` and type hints; keep functions pure.
  The only I/O is in `qft.data` (read) and `qft.main` (print/write).
- Numbers are `float64` via NumPy; spectra are `complex128`.
- Docstrings on every public function; explain the *why*, not the *how*.
- Tests live at `tests/test_<area>.py`.

## Guardrails

- Do **not** add dependencies (Qiskit + NumPy are enough). If you think you need
  one, write the spec first, then update `pyproject.toml` and re-run `uv lock`.
- Use **`QFTGate`**, not the deprecated `QFT` class.
- Do **not** touch `../../samples/` (shared with the `ft` project) without noting
  it in the iteration spec.
- Keep `--out` JSON valid; a broken report is a failing change.

## Definition of done

1. Acceptance criteria in the iteration spec are met.
2. `uv run pytest` is green.
3. `uv run qft` emits a forecast for all four symbols.
4. `docs/` and the iteration's Review section are updated.

## Known subtleties (do not "fix" these)

- The QFT uses a **positive exponent**; the forward DFT is recovered as
  `X_j = √N·conj(y_j)` for real input. This is correct and tested.
- `QuantumCircuit.initialize` preserves the state with no global phase; no
  correction is needed.
- Aer cannot run the composite `qft` instruction — `sample_qft` transpiles first.
- Linear detrending leaks a sliver of a phase-shifted sine; exact extrapolation is
  only guaranteed for **trend-free, centred periodic** signals. Intentional/tested.
- The Nyquist term is required for exact full-bin reconstruction. Leave it in.
