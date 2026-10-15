# FT (Fourier Transform price-prediction exercise) — Clojure sub-project

A standalone, monorepo-style Clojure sub-project that reads the synthetic
hourly dataset in `../samples/trading_data.csv` and produces short-horizon
price **forecasts** for each dummy asset using a Fourier (frequency-domain)
model.

> **This is an exercise.** It is not a trading system, places no orders, and
> the dataset is **synthetic** (see `../samples/`).

## What it does

For each symbol (`AAPL`, `IBM`, `BTC-USD`, `SOL-USD`):

1. Loads the hourly close series.
2. Detrends it (linear regression) so the FFT sees cyclical structure, not drift.
3. Runs a radix-2 **FFT** (Apache Commons Math).
4. Keeps the top-K frequency components.
5. Reconstructs/extrapolates the fitted sinusoids + trend to forecast the next N hours.
6. Scores the forecast on a held-out window (MAE / RMSE / MAPE).

## Layout

```
ft/
├── deps.edn            # tools.deps project + :run/:test aliases
├── src/ft/             # data, fft, predict, metrics, main
├── test/ft/            # clojure.test suites + runner
├── docs/               # offline cross-OS install/run tutorial, library guide
├── specs/              # agile iterations: spec -> feature -> spec ...
└── agents/             # tailored briefs for Claude Code, OpenAI Codex, Gemini, Grok
```

## Quick start

```bash
# from the ft/ directory
clojure -M:run -- --data ../samples/trading_data.csv --horizon 24
clojure -M:test
```

See `docs/` for a complete offline install/run tutorial (Windows, macOS,
Linux, with Guix where feasible) and detailed library usage.

## Design notes

- No order placement, no network. The program is pure I/O + math.
- The FFT requires a power-of-two window; the default fit window is 512 hours.
- Deterministic given the same input file.
