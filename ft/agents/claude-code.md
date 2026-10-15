# CLAUDE.md — FT (Clojure Fourier price-prediction exercise)

> This file guides Claude Code when working inside `ft/`. It is the
> Claude-oriented view of the shared brief in `README.md`.

## Mission

Maintain and extend the **ft** sub-project: a Fourier (frequency-domain) price
forecaster written in Clojure. Input is a **synthetic** hourly CSV; output is a
short-horizon forecast plus holdout error metrics per symbol.

## Commands

```bash
clojure -P                 # resolve deps (first run)
clojure -M:test            # MUST be green before you finish
clojure -M:run -- --data ../samples/trading_data.csv --horizon 24
clojure -M:run -- --out out/report.json
```

## Working style (for Claude Code)

- **Plan, then act.** For non-trivial changes, outline the plan first; keep edits
  scoped to one iteration.
- **Prefer the REPL for exploration:** start `clj`, load a namespace, poke at the
  data; then write the test that captures what you learned.
- **Read before writing:** `src/ft/data.clj`, `fft.clj`, `predict.clj`,
  `metrics.clj`, `main.clj` (in that order) mirror the data → spectrum → model →
  score → CLI pipeline.
- **Use the todo/plan tooling** to track multi-file changes.

## Code conventions

- Namespaces are `ft.<area>`; files live at `src/ft/<area>.clj`.
- Keep functions pure; the only I/O is in `ft.data` (read) and `ft.main`
  (print/write).
- Numbers are JVM doubles via `Math/*`; do not introduce a numeric tower.
- Docstrings on every public `defn`; explain the *why*, not the *how*.
- Tests live at `test/ft/<area>_test.clj` and are wired into `ft.runner`.

## Guardrails

- Do **not** add dependencies (Commons Math + data.csv are enough). If you think
  you need one, write the spec first.
- Do **not** touch `../../samples/` (shared with the QFT project) without noting
  it in the iteration spec.
- Keep `--out` JSON valid; a broken report is a failing change.

## Definition of done

1. Acceptance criteria in the iteration spec are met.
2. `clojure -M:test` is green.
3. `clojure -M:run` emits a forecast for all four symbols.
4. `docs/` and the iteration's Review section are updated.

## Known subtleties (do not "fix" these)

- Linear detrending leaks a sliver of a phase-shifted sine; exact extrapolation
  is only guaranteed for **trend-free periodic** signals. This is intentional and
  tested.
- The Nyquist term is required for exact full-bin reconstruction. Leave it in.
