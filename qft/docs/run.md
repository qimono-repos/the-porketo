# Running QFT

All commands are run **from the `qft/` directory**.

## 1. First run (resolves dependencies once)

```bash
uv sync                     # creates .venv, downloads Python 3.12 + locked deps
```

## 2. Tests

```bash
uv run pytest
```

Expected tail:

```
26 passed in ...s
```

## 3. The forecast

```bash
uv run qft --data ../samples/trading_data.csv --horizon 24
```

### Flags

| Flag | Default | Meaning |
|---|---:|---|
| `--data` | `../samples/trading_data.csv` | Path to the CSV |
| `--window` | `512` | Fit window length in hours. **Must be a power of two** (→ 9 qubits). |
| `--horizon` | `24` | How many future hours to predict and to hold out |
| `--k` | `8` | How many Fourier components (bins) to keep |
| `--shots` | `0` | If > 0, also simulate `--shots` measurements on Qiskit Aer and print the top measured states |
| `--out` | _(none)_ | Write a JSON report to this path |

### Example output

```
QFT — Quantum Fourier Transform price-prediction exercise
data: ../samples/trading_data.csv | window: 512 (9 qubits) | horizon: 24 | k: 8

AAPL      holdout MAE=7.549368   RMSE=8.287381   MAPE=2.48719%  trend/h=0.04449
          top periods (h): 512.0, 256.0, 170.666667, 73.142857, ...
          forecast next 24 h: [313.043809, 313.833194, ...]
```

Because the quantum transform reproduces the classical DFT exactly, these
metrics are **identical** to the `ft` (Clojure) sub-project's output — a useful
cross-check (see `../specs/TRACEABILITY.md`).

### Shot sampling

```bash
uv run qft --shots 4096 --data ../samples/trading_data.csv --horizon 24
```

This additionally runs the QFT circuit on `AerSimulator` for `--shots`
measurements and prints the most frequently measured basis states (each maps to
a frequency bin `j`). The **forecast itself always uses the exact statevector**
so results stay deterministic and reproducible; the shot path is a demonstration
of the measurement statistics of the post-QFT state.

### JSON report

```bash
uv run qft --out out/report.json
```

The file has one object per symbol with the fitted trend, the number of qubits,
the top components (bin `k`, `period_hours`, magnitude), the holdout metrics, the
24-hour forecast array, and — when `--shots > 0` — the sampled top states.

---

## The algorithm, step by step

1. **Load** the CSV; select one symbol's `close` series (length 1024).
2. **Split**: `split = total − horizon`. Train on the `window` points ending at
   `split`; hold out the final `horizon` points.
3. **Detrend** (linear regression) so the transform is dominated by cycles, not drift.
4. **Amplitude-encode** the detrended window into `n = log2(window)` qubits
   (`qc.initialize`), then apply the **QFT** (`QFTGate`).
5. **Read** the post-QFT statevector `y` and recover the standard DFT
   coefficients `X_j = √N · ‖x‖ · conj(y_j)`.
6. **Select** the `k` strongest positive-frequency bins (`k`, `period`, `mag`).
7. **Build the model**: `price(t) = a + b·t + DC + Σₖ (2/n)·Re(X[k]·e^{i2πkt/n}) + Nyquist`.
8. **Evaluate**: predict the held-out `horizon` points and compute MAE/RMSE/MAPE.
9. **Forecast**: refit on the most recent `window` points and predict the next
   `horizon` hours.

### Why the quantum amplitudes equal the DFT

Qiskit's `QFTGate` implements `y_j = (1/√N)·Σ_k e^{+2πijk/N}·v_k`. For a **real**
input the standard forward DFT (`numpy.fft.fft`, and the `ft` sub-project's
Commons Math result) is the conjugate sum, so `X_j = √N·conj(y_j)`. Amplitude
encoding normalises the window, and we multiply the norm back out. The tests
assert this equality to `1e-9` for sizes 4…512, and `tests/test_predict.py`
asserts the quantum and classical **forecasts** agree.

### Why detrend first?

A price series with a visible uptrend would put almost all its spectral energy
into the lowest bin, hiding daily/weekly cycles. Removing the fitted line exposes
the cycles; the line is added back when predicting.

### Why power-of-two windows?

Amplitude encoding needs `N = 2^n` amplitudes to fill `n` qubits. With
`window: 512` we use **9 qubits**. Non-power-of-two lengths raise a clear error.

### Choosing `k`

- Small `k` (e.g. 3–8): smooth, robust forecasts; fewer, stronger cycles.
- Large `k` (up to `window/2`): reproduces the window exactly but also fits
  noise, and extrapolation becomes less stable. `k = window/2` is the
  "use every component" limit (incl. Nyquist) demonstrated in the tests.

---

## Trying other parameters

```bash
# a smaller circuit: 256 → 8 qubits
uv run qft --window 256 --horizon 12 --k 6

# a 7-day (168 h) forecast
uv run qft --horizon 168

# demonstrate measurement sampling
uv run qft --shots 4096

# work from a different dataset
uv run qft --data /path/to/another.csv
```

## Adding a symbol

Add rows with a new `symbol` value to `../samples/trading_data.csv`; the CLI
discovers symbols automatically via `qft.data.symbols`.
