# grok.md — FT (Clojure Fourier price-prediction exercise)

> Brief for Grok. Same ground truth as `README.md`; written to be read quickly.

## TL;DR

`ft/` is a Clojure program that FFTs a **synthetic** hourly price series and
forecasts the next N hours per symbol, then scores itself on a holdout.

```bash
cd ft
clojure -P
clojure -M:test
clojure -M:run -- --data ../samples/trading_data.csv --horizon 24
```

## Mental model

```
CSV ──data.clj──► close[] ──predict.clj──► detrend ──fft.clj──► spectrum
                     │                                            │
                     └── holdout ──metrics.clj──► MAE/RMSE/MAPE   │
                                                                  ▼
                                     trend + top-k bins + Nyquist = forecast
```

## Rules of engagement

- Read the code before proposing changes; mirror existing style.
- Only `ft.data` reads files; only `ft.main` prints/writes.
- Numbers are JVM doubles; use `Math/*`.
- Never add a dependency, never touch the dataset, never call the network.
- `clojure -M:test` green is non-negotiable.

## Where to look

- Algorithm: `src/ft/predict.clj` (`fit`, `predict-at`, `predict-series`).
- FFT wrapper: `src/ft/fft.clj` (Commons Math `FastFourierTransformer`).
- Library rationale: `docs/libraries.md`.
- Process/backlog: `specs/README.md`, `specs/BACKLOG.md`.

## Non-obvious facts

- Windows must be powers of two (radix-2).
- The Nyquist term is required; leave it in.
- Exact extrapolation is only guaranteed for trend-free periodic signals.

## Deliverable checklist

- [ ] Acceptance criteria met
- [ ] `clojure -M:test` green
- [ ] `clojure -M:run` forecasts all four symbols
- [ ] iteration Review updated
