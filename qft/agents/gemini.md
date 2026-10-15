# GEMINI.md — QFT (quantum Fourier price-prediction exercise)

> Brief for the Gemini CLI working inside `qft/`. Consistent with `README.md`;
> phrased for Gemini's plan-and-execute loop.

## Context

`qft/` is a standalone Python sub-project: it loads a **synthetic** hourly price
CSV, amplitude-encodes each window into qubits, applies the **Quantum Fourier
Transform** (Qiskit), and forecasts the next `horizon` hours per symbol,
reporting MAE/RMSE/MAPE on a holdout. For equal parameters its metrics match the
classical `ft` sub-project exactly.

## Setup

```bash
uv sync                 # once, needs network: installs Python 3.12 + deps
uv run pytest
uv run qft --data ../samples/trading_data.csv
```

Toolchain: **`uv` only** — it manages Python for you. See `../docs/` for
Windows/macOS/Linux/Guix install steps. Guix users: run `uv` inside a
`guix shell` (see `docs/install-guix.md`).

## Repo map

```
qft/
├── pyproject.toml / uv.lock
├── src/qft/{data,quantum,predict,metrics,main}.py
├── tests/{test_quantum,test_predict,test_metrics,test_data}.py
├── specs/   (agile backlog + iterations)
├── docs/    (offline install/run + library guide)
└── agents/  (this file and peers)
```

## How to behave

- **Ground yourself first:** read the target module and its test before editing.
- **Small steps:** change one concern, run the tests, then continue.
- **Explain briefly** what you changed and why in your final message.
- **Cite files by path** (`src/qft/predict.py`) so a human can follow.

## Constraints

- Synthetic data only. No network, no trading, no real prices, no QPU hardware.
- Keep the public functions and the CLI/JSON contract stable.
- No new dependencies without a spec entry in `specs/` (and a `uv lock`).
- `uv run pytest` must remain green; verify before finishing.

## Useful invariants

- QFT convention: `X_j = √N·conj(y_j)` for real input (positive-exponent QFT).
- `predict_at` = trend + DC + selected positive bins + Nyquist.
- Windows must be powers of two (`N = 2^n` → `n` qubits).
- Exact extrapolation holds only for trend-free, centred periodic signals (see
  `specs/iterations/iteration-03-prediction-model.md`).

## Definition of done

Criteria met, tests green, `uv run qft` prints four symbol blocks, and the
matching iteration Review section is updated.
