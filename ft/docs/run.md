# Running FT

All commands are run **from the `ft/` directory**.

## 1. First run (resolves dependencies once)

```bash
clojure -P                 # pre-download Clojure, Commons Math, data.csv
```

## 2. Tests

```bash
clojure -M:test
```

Expected tail:

```
Ran 12 tests containing 87 assertions.
0 failures, 0 errors.
```

## 3. The forecast

```bash
clojure -M:run -- --data ../samples/trading_data.csv --horizon 24
```

`--` separates the `clojure` launcher arguments from the program's arguments.

### Flags

| Flag | Default | Meaning |
|---|---:|---|
| `--data` | `../samples/trading_data.csv` | Path to the CSV |
| `--window` | `512` | Fit window length in hours. **Must be a power of two.** |
| `--horizon` | `24` | How many future hours to predict and to hold out |
| `--k` | `8` | How many Fourier components (bins) to keep |
| `--out` | _(none)_ | Write a JSON report to this path |

### Example output

```
FT — Fourier price-prediction exercise
data: ../samples/trading_data.csv | window: 512 | horizon: 24 | k: 8

AAPL      holdout MAE=7.549368   RMSE=8.287381   MAPE=2.48719%  trend/h=0.04449
          top periods (h): 512.0, 256.0, 170.666667, 73.142857, ...
          forecast next 24 h: [313.043809 313.833194 ...]
```

### JSON report

```bash
clojure -M:run -- --out out/report.json
```

The file has one object per symbol with the fitted trend, the top components
(their bin `k`, `period_hours`, and magnitude), the holdout metrics, and the
24-hour forecast array.

---

## The algorithm, step by step

1. **Load** the CSV into rows; select one symbol's `close` series (length 1024).
2. **Split**: `split = total − horizon`. Train on the `window` points ending at
   `split`; hold out the final `horizon` points.
3. **Detrend** (linear regression) so the FFT is dominated by cycles, not drift.
4. **Forward FFT** (radix-2) of the detrended window → complex spectrum.
5. **Select** the `k` strongest positive-frequency bins (`:k`, `:period`, `:mag`).
6. **Build the model**: `price(t) = a + b·t + DC + Σₖ (2/n)·Re(X[k]·e^{i2πkt/n}) + Nyquist`.
7. **Evaluate**: predict the held-out `horizon` points and compute MAE/RMSE/MAPE.
8. **Forecast**: refit on the most recent `window` points and predict the next
   `horizon` hours.

### Why detrend first?

A price series with a visible uptrend would put almost all its FFT energy into
the lowest bin (the trend), hiding the daily/weekly cycles. Removing the fitted
line exposes the cycles; the line is added back when predicting.

### Why power-of-two windows?

The radix-2 FFT requires it. With `window: 512` the FFT is exact-O(n log n).
Non-power-of-two lengths raise a clear error.

### Choosing `k`

- Small `k` (e.g. 3–8): smooth, robust forecasts; fewer, stronger cycles.
- Large `k` (up to `window/2`): reproduces the window exactly but also fits
  noise, and extrapolation becomes less stable. `k = window/2 − 1` is the
  "use every component" limit demonstrated in the tests.

---

## Trying other parameters

```bash
# a shorter, snappier window with fewer components
clojure -M:run -- --window 256 --horizon 12 --k 6

# a 7-day (168 h) forecast
clojure -M:run -- --horizon 168

# work from a different dataset
clojure -M:run -- --data /path/to/another.csv
```

## Adding a symbol

Add rows with a new `symbol` value to `../samples/trading_data.csv`; the CLI
discovers symbols automatically via `ft.data/symbols`.
