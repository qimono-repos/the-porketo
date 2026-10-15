# AGENTS.md — FT (Clojure Fourier price-prediction exercise)

> Project brief for OpenAI Codex working inside `ft/`. Mirrors the shared
> invariants in `README.md`, oriented to Codex's autonomous-task workflow.

## Objective

Safely extend the **ft** Fourier forecaster. Treat each request as a task with
explicit inputs, steps, and a verifiable output.

## Ground truth

- Language: Clojure, tools.deps (`deps.edn`).
- Libraries: Clojure 1.12, Apache Commons Math 3.6.1 (FFT), data.csv 1.1.0.
- Input: `../../samples/trading_data.csv` (**synthetic**).
- Pipeline: `data → fft → predict → metrics → main`.

## Commands to run after every change

```bash
clojure -M:test                                                # required
clojure -M:run -- --data ../samples/trading_data.csv --horizon 24
```

A change is not complete until both commands succeed.

## Task protocol

1. **Read the spec** for the current iteration in `specs/iterations/`.
2. **Locate** the smallest set of files to change.
3. **Implement** with pure functions and docstrings.
4. **Add/extend a test** that fails without your change.
5. **Run** the two commands above; paste their results in your summary.
6. **Update** the iteration file's Review section.

## Conventions

- One namespace per concern; `ft.main` owns argument parsing and printing only.
- Follow existing naming: `predict-at`, `predict-series`, `top-bins`, `mae`.
- No network calls; no order placement; no real market data.

## Error handling

- Guard inputs at the boundary (`power-of-two?`, CLI parsing) and fail with
  `ex-info` carrying context — never return silently wrong numbers.

## Do not

- Add dependencies, reorder the pipeline, or change the JSON schema without a
  spec entry.
- Edit the synthetic dataset.
- Remove the Nyquist term from `predict-at`.

## Definition of done

Green tests, a working run for all four symbols, and an updated Review section.
