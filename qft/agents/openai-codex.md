# AGENTS.md — QFT (quantum Fourier price-prediction exercise)

> Project brief for OpenAI Codex working inside `qft/`. Mirrors the shared
> invariants in `README.md`, oriented to Codex's autonomous-task workflow.

## Objective

Safely extend the **qft** quantum forecaster. Treat each request as a task with
explicit inputs, steps, and a verifiable output.

## Ground truth

- Language: Python 3.12, managed by `uv` (`pyproject.toml` + `uv.lock`).
- Libraries: qiskit (QFT circuit + statevector), qiskit-aer (shots), numpy, pytest.
- Input: `../../samples/trading_data.csv` (**synthetic**).
- Pipeline: `data → quantum → predict → metrics → main`.

## Commands to run after every change

```bash
uv run pytest                                   # required
uv run qft --data ../samples/trading_data.csv --horizon 24
```

A change is not complete until both commands succeed.

## Task protocol

1. **Read the spec** for the current iteration in `specs/iterations/`.
2. **Locate** the smallest set of files to change.
3. **Implement** with pure functions, type hints, and docstrings.
4. **Add/extend a test** that fails without your change.
5. **Run** the two commands above; paste their results in your summary.
6. **Update** the iteration file's Review section.

## Conventions

- One module per concern; `qft.main` owns argument parsing and printing only.
- Use `QFTGate` (not the deprecated `QFT` class).
- Follow existing naming: `predict_at`, `predict_series`, `top_bins`, `mae`,
  `qft_coefficients`.
- No network calls (after `uv sync`); no order placement; no real market data;
  simulator only.

## Error handling

- Guard inputs at the boundary (`is_power_of_two`, CLI parsing) and fail with
  `ValueError` carrying context — never return silently wrong numbers.

## Do not

- Add dependencies, reorder the pipeline, or change the JSON schema without a
  spec entry (and re-run `uv lock` if you do add one).
- Edit the synthetic dataset.
- Remove the Nyquist term from `predict_at`.
- Break quantum/classical parity with the `ft` project.

## Definition of done

Green tests (26 passed), a working run for all four symbols, and an updated
Review section.
