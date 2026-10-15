# QFT (Quantum Fourier Transform price-prediction exercise) — Python sub-project

A standalone, monorepo-style Python sub-project that reads the synthetic hourly
dataset in `../samples/trading_data.csv` and produces short-horizon price
**forecasts** for each dummy asset using a **Quantum Fourier Transform** built
with [Qiskit](https://www.ibm.com/quantum/qiskit), managed with
[uv](https://docs.astral.sh/uv/).

> **This is an exercise.** It is not a trading system, places no orders, and the
> dataset is **synthetic** (see `../samples/`).

## What it does

For each symbol (`AAPL`, `IBM`, `BTC-USD`, `SOL-USD`):

1. Loads the hourly close series and takes a power-of-two **window**.
2. Detrends it and **amplitude-encodes** it into an n-qubit state
   (`N = 2^n` amplitudes).
3. Applies the **QFT** (Qiskit) and reads the resulting statevector — the
   frequency-domain representation.
4. Recovers the standard DFT coefficients from the QFT amplitudes and keeps the
   top-K frequency components.
5. Reconstructs + extrapolates the fitted sinusoids and trend to forecast the
   next N hours.
6. Scores the forecast on a held-out window (MAE / RMSE / MAPE).

The classical `numpy.fft` is used only to **validate** that the quantum circuit
reproduces the DFT (see `tests/`).

## Layout

```
qft/
├── pyproject.toml      # uv/PEP-621 project (qiskit, qiskit-aer, numpy)
├── uv.lock             # committed lockfile
├── src/qft/            # data, quantum (encode+QFT), predict, metrics, main
├── tests/              # pytest suites
├── docs/               # offline cross-OS install/run tutorial, library guide
├── specs/              # agile iterations: spec -> feature -> spec ...
└── agents/             # briefs for Claude Code, OpenAI Codex, Gemini, Grok
```

## Quick start

```bash
# from the qft/ directory
uv sync
uv run pytest
uv run qft --data ../samples/trading_data.csv --horizon 24
```

See `docs/` for a complete offline install/run tutorial (Windows, macOS, Linux,
with Guix where feasible) and detailed library usage.

## Design notes

- The transform is genuine quantum: an encoded state is evolved by the QFT
  unitary and simulated (exact statevector by default, or shot-sampled with
  `--shots`).
- Windows must be powers of two (`N = 2^n`); the default window is 512 (9 qubits).
- Deterministic given the same input file.
