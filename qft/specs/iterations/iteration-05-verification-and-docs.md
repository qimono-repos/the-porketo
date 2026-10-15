# Iteration 05 — Verification & documentation

**Goal:** make the project trustworthy and easy to adopt anywhere.

**Depends on:** Iteration 04

## Stories

- **E1** Test suite for the QFT, model, metrics, and data. _(M, 5)_
- **E2** Offline cross-OS install/run tutorial (Windows/macOS/Linux, Guix where feasible). _(M, 5)_
- **E3** Tailored agent briefs (Claude Code, Codex, Gemini, Grok). _(S, 3)_
- **E4** Parity with the `ft` (Clojure) forecast. _(S, 3)_

## Acceptance criteria

**E1 — Given** a clean checkout, **when** I run `uv run pytest`, **then** all
tests pass (currently **26 passed**: 11 quantum, 6 predict, 6 metrics, 3 data).

**E2 — Given** a brand-new machine, **when** I follow `../docs/`, **then** I can
install `uv` (via Homebrew, winget, the installer, or Guix) and run the forecast,
with **no network access needed after the first `uv sync`**.

**E3 — Given** an AI agent, **when** it opens `../agents/<agent>.md`, **then** it
finds the mission, constraints, commands, and conventions for this sub-project.

**E4 — Given** `--window 512 --horizon 24 --k 8`, **when** I run both `uv run qft`
and the `ft` CLI, **then** the holdout MAE/RMSE/MAPE are identical for all four
symbols (see `../TRACEABILITY.md` for the table).

## Tasks

1. `tests/test_quantum.py`, `test_predict.py`, `test_metrics.py`, `test_data.py`.
2. `docs/` (per-OS install, run, libraries, troubleshooting).
3. `agents/` (four files + index).

## Review

**Shipped:** E1 (26 tests, all green on Qiskit 2.5.2 / NumPy 2.5.4), E2, E3, E4.
**What changed:** the DFT-equality test is parametrised over several sizes,
including 512 (the production window); parity with `ft` was promoted from an
informal check to story **E4** with a recorded evidence table.
**Backlog impact:** Epic F remains parked; project is at a shippable baseline.
