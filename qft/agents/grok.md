# grok.md — QFT (quantum Fourier price-prediction exercise)

> Brief for Grok. Same ground truth as `README.md`; written to be read quickly.

## TL;DR

`qft/` is a Python program that amplitude-encodes a **synthetic** hourly price
window into qubits, applies the Quantum Fourier Transform (Qiskit), and forecasts
the next N hours per symbol — then scores itself on a holdout. The numbers match
the classical `ft` project exactly.

```bash
cd qft
uv sync
uv run pytest
uv run qft --data ../samples/trading_data.csv --horizon 24
```

## Mental model

```
CSV ──data.py──► close[] ──predict.py──► detrend ──quantum.py──► QFT ──► spectrum
                     │              (encode n qubits, append QFTGate, read y)
                     │              X_j = √N·conj(y_j)
                     └── holdout ──metrics.py──► MAE/RMSE/MAPE
                                     trend + top-k bins + Nyquist = forecast
```

## Rules of engagement

- Read the code before proposing changes; mirror existing style.
- Only `qft.data` reads files; only `qft.main` prints/writes.
- Numbers are `float64`/`complex128` via NumPy.
- Use `QFTGate` (not the deprecated `QFT` class).
- Never add a dependency, never touch the dataset, never call the network (after
  `uv sync`), never use real hardware.
- `uv run pytest` green is non-negotiable.

## Where to look

- Quantum core: `src/qft/quantum.py` (`qft_statevector`, `qft_coefficients`,
  `sample_qft`).
- Algorithm: `src/qft/predict.py` (`fit`, `predict_at`, `predict_series`).
- Library rationale: `docs/libraries.md`.
- Process/backlog: `specs/README.md`, `specs/BACKLOG.md`.

## Non-obvious facts

- Qiskit's QFT uses a **positive** exponent and `1/√N` scaling; the forward DFT is
  `√N·conj(y)` for real input.
- `QuantumCircuit.initialize` is phase-clean (no global-phase correction needed).
- Aer can't run the composite `qft` instruction — transpile first.
- Windows must be powers of two (amplitude encoding).
- The Nyquist term is required; leave it in.
- Exact extrapolation is only guaranteed for trend-free, centred periodic signals.

## Deliverable checklist

- [ ] Acceptance criteria met
- [ ] `uv run pytest` green (26 passed)
- [ ] `uv run qft` forecasts all four symbols
- [ ] iteration Review updated
