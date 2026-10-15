# FT — Traceability matrix

Maps every story to the code that satisfies it and the test that verifies it.

| Story | Code | Test / verification |
|---|---|---|
| A1 load CSV | `src/ft/data.clj` `load-rows` | exercised by `ft.main` run; covered indirectly via CLI |
| A2 series per symbol | `src/ft/data.clj` `series-for`, `symbols` | `clojure -M:run` prints one block per symbol |
| A3 parse doubles | `src/ft/data.clj` `dbl` | `ft.predict`/`ft.fft` consume the doubles without error |
| B1 forward FFT | `src/ft/fft.clj` `forward` | `ft.fft-test/forward-detects-sinusoid-frequency`, `magnitudes-of-known-vector` |
| B2 power-of-two guard | `src/ft/fft.clj` `power-of-two?`, `forward` | `ft.fft-test/power-of-two-tests`, `forward-rejects-bad-length` |
| B3 top bins + periods | `src/ft/fft.clj` `bands`, `top-bins` | `ft.fft-test/forward-detects-sinusoid-frequency` |
| C1 detrend | `src/ft/predict.clj` `linfit`, `detrend` | `ft.predict-test/linfit-recovers-a-line`, `detrend-removes-the-line` |
| C2 reconstruct/extrapolate | `src/ft/predict.clj` `fit`, `bin-term`, `predict-at` | `ft.predict-test/full-bin-model-reconstructs-window-exactly`, `extrapolation-matches-continuation-of-a-periodic-signal` |
| C3 forward forecast | `src/ft/predict.clj` `predict-series`, `src/ft/main.clj` `analyse` | CLI output (`forecast next N h`) |
| D1 metrics | `src/ft/metrics.clj` `mae` `rmse` `mape` | `ft.metrics-test/*` |
| D2 CLI | `src/ft/main.clj` `parse-args` `-main` | `clojure -M:run -- --horizon 24` |
| D3 JSON report | `src/ft/main.clj` `->json` | `--out` producing valid JSON (checked with a JSON parser) |
| E1 tests | `test/ft/*` | `clojure -M:test` → 0 failures / 0 errors |
| E2 docs | `docs/*` | manual walkthrough |
| E3 agents | `agents/*` | manual review |

## Commands used for verification

```bash
clojure -P                 # resolve projects/deps
clojure -M:test            # 12 tests, 87 assertions
clojure -M:run -- --data ../samples/trading_data.csv --horizon 24
clojure -M:run -- --out out/report.json
```
