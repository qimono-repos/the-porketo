# FT — Product Backlog

Status legend: ✅ done · 🔜 next · 🅿️ parked · ❌ dropped.

Estimates in **points** (1 = small, 8 = large). Priorities: M = must, S = should,
C = could.

## Epic A — Data ingestion

| # | Story | Pri | Est | Status |
|---|---|---|---|---|
| A1 | As a researcher, I want to load the CSV into plain data, so that downstream code sees vectors, not strings. | M | 2 | ✅ |
| A2 | As a researcher, I want the series for one symbol in file order, so that time order is preserved. | M | 1 | ✅ |
| A3 | As a researcher, I want the parsed numbers as doubles, so the FFT can consume them. | M | 1 | ✅ |

## Epic B — Fourier engine

| # | Story | Pri | Est | Status |
|---|---|---|---|---|
| B1 | As a contributor, I want a forward FFT of a real vector, so I can inspect the spectrum. | M | 3 | ✅ |
| B2 | As a contributor, I want to reject non power-of-two lengths, so misuse fails loudly. | M | 1 | ✅ |
| B3 | As a researcher, I want the strongest positive-frequency bins with their periods, so I can read seasonality. | M | 2 | ✅ |

## Epic C — Prediction model

| # | Story | Pri | Est | Status |
|---|---|---|---|---|
| C1 | As a researcher, I want to detrend the window, so the FFT shows cycles, not drift. | M | 3 | ✅ |
| C2 | As a researcher, I want to reconstruct the fitted signal and extrapolate it forward. | M | 5 | ✅ |
| C3 | As a researcher, I want a genuine future forecast refit on the most recent window. | S | 3 | ✅ |

## Epic D — Metrics & CLI

| # | Story | Pri | Est | Status |
|---|---|---|---|---|
| D1 | As a researcher, I want MAE/RMSE/MAPE on a holdout, so accuracy is measured, not assumed. | M | 2 | ✅ |
| D2 | As an operator, I want a CLI with `--data/--window/--horizon/--k/--out`. | M | 3 | ✅ |
| D3 | As an operator, I want a machine-readable JSON report. | S | 2 | ✅ |

## Epic E — Verification & docs

| # | Story | Pri | Est | Status |
|---|---|---|---|---|
| E1 | As a contributor, I want a test suite covering FFT, model, and metrics. | M | 5 | ✅ |
| E2 | As a new user, I want an offline cross-OS install/run tutorial. | M | 5 | ✅ |
| E3 | As an AI collaborator, I want tailored agent briefs. | S | 3 | ✅ |

## Parked / future

| # | Story | Pri | Est | Status |
|---|---|---|---|---|
| F1 | Multi-window walk-forward backtest (rolling evaluation). | C | 8 | 🅿️ |
| F2 | Automatic component-count selection (AIC/BIC or energy threshold). | C | 5 | 🅿️ |
| F3 | Write forecasts back to a CSV for the QFT project to compare. | C | 3 | 🅿️ |
| F4 | Real market-data adapter (explicitly out of scope; synthetic only). | C | — | ❌ |
