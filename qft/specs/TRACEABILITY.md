# QFT — Traceability matrix

Maps every story to the code that satisfies it and the test that verifies it.

| Story | Code | Test / verification |
|---|---|---|
| A1 load CSV | `src/qft/data.py` `load_rows` | `tests/test_data.py::test_rows_have_expected_columns` |
| A2 series per symbol | `src/qft/data.py` `symbols`, `series_for` | `tests/test_data.py::test_symbols_in_file_order`, `test_series_for_parses_types` |
| A3 parse floats | `src/qft/data.py` `series_for` | `tests/test_data.py::test_series_for_parses_types` |
| B1 encode + QFT | `src/qft/quantum.py` `qft_statevector` | `tests/test_quantum.py::test_qft_statevector_is_normalised`, `test_qft_then_inverse_recovers_signal` |
| B2 DFT equivalence | `src/qft/quantum.py` `qft_coefficients` | `tests/test_quantum.py::test_qft_coefficients_match_numpy_fft` (sizes 4…512) |
| B3 power-of-two guard | `src/qft/quantum.py` `is_power_of_two`, `n_qubits` | `tests/test_quantum.py::test_n_qubits_and_power_of_two` |
| B4 top bins + periods | `src/qft/predict.py` `top_bins` | `tests/test_predict.py::test_fit_finds_dominant_bin` |
| B5 shot sampling | `src/qft/quantum.py` `sample_qft`, `qft_probabilities` | `tests/test_quantum.py::test_sample_qft_argmax_matches_exact`, `test_probabilities_sum_to_one` |
| C1 detrend | `src/qft/predict.py` `linfit`, `detrend` | `tests/test_predict.py::test_linfit_recovers_exact_line`, `test_detrend_removes_line_and_keeps_centered_signal` |
| C2 reconstruct/extrapolate | `src/qft/predict.py` `fit`, `_bin_term`, `predict_at` | `tests/test_predict.py::test_full_spectrum_reconstructs_window_exactly`, `test_extrapolation_matches_continuation_of_a_centered_periodic_signal` |
| C3 forward forecast | `src/qft/predict.py` `predict_series`, `src/qft/main.py` `analyse` | CLI output (`forecast next N h`) |
| D1 metrics | `src/qft/metrics.py` `mae` `rmse` `mape` | `tests/test_metrics.py::*` (6 tests) |
| D2 CLI | `src/qft/main.py` `build_parser`, `main` | `uv run qft --horizon 24` |
| D3 JSON report | `src/qft/main.py` `main` (`--out`) | `--out` producing valid JSON (checked with `json.load`) |
| E1 tests | `tests/*` | `uv run pytest` → 26 passed |
| E2 docs | `docs/*` | manual walkthrough |
| E3 agents | `agents/*` | manual review |
| E4 parity with ft | `src/qft/predict.py` + `src/qft/quantum.py` | `tests/test_predict.py::test_quantum_transform_matches_classical_spectrum`; CLI metrics equal `ft` output for `--window 512 --horizon 24 --k 8` |

## Commands used for verification

```bash
uv sync
uv run pytest                                   # 26 passed
uv run qft --data ../samples/trading_data.csv --horizon 24
uv run qft --shots 4096 --out out/report.json
# cross-check (identical metrics):
cd ../ft && JAVA_HOME=/opt/homebrew/opt/openjdk clojure -M:run -- --data ../samples/trading_data.csv --horizon 24
```

## Parity evidence

With defaults (`window 512`, `horizon 24`, `k 8`) both sub-projects report:

| Symbol | holdout MAE | RMSE | MAPE % |
|---|---:|---:|---:|
| AAPL | 7.549368 | 8.287381 | 2.48719 |
| IBM | 7.633028 | 7.867921 | 2.768209 |
| BTC-USD | 990.963112 | 1178.827253 | 2.243199 |
| SOL-USD | 5.087379 | 6.433396 | 2.129371 |
