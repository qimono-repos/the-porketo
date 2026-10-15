# GEMINI.md — FT (Clojure Fourier price-prediction exercise)

> Brief for the Gemini CLI working inside `ft/`. Consistent with `README.md`;
> phrased for Gemini's plan-and-execute loop.

## Context

`ft/` is a standalone Clojure sub-project: it loads a **synthetic** hourly price
CSV and forecasts the next `horizon` hours per symbol using a detrended radix-2
FFT model, reporting MAE/RMSE/MAPE on a holdout.

## Setup

```bash
clojure -P          # once, needs network
clojure -M:test
clojure -M:run -- --data ../samples/trading_data.csv
```

Toolchain: a JDK 17+ and the Clojure CLI. See `../docs/` for Windows/macOS/
Linux/Guix install steps. Guix users: `guix install openjdk clojure-tools`.

## Repo map

```
ft/
├── deps.edn
├── src/ft/{data,fft,predict,metrics,main}.clj
├── test/ft/{fft,predict,metrics}_test.clj + runner.clj
├── specs/   (agile backlog + iterations)
├── docs/    (offline install/run + library guide)
└── agents/  (this file and peers)
```

## How to behave

- **Ground yourself first:** read the target namespace and its test before editing.
- **Small steps:** change one concern, run the tests, then continue.
- **Explain briefly** what you changed and why in your final message.
- **Cite files by path** (`src/ft/predict.clj`) so a human can follow.

## Constraints

- Synthetic data only. No network, no trading, no real prices.
- Keep the public functions and the CLI/JSON contract stable.
- No new dependencies without a spec entry in `specs/`.
- `clojure -M:test` must remain green; verify before finishing.

## Useful invariants

- `predict-at` = trend + DC + selected positive bins + Nyquist.
- Windows must be powers of two.
- Exact extrapolation holds only for trend-free periodic signals (see
  `specs/iterations/iteration-03-prediction-model.md`).

## Definition of done

Criteria met, tests green, `clojure -M:run` prints four symbol blocks, and the
matching iteration Review section is updated.
