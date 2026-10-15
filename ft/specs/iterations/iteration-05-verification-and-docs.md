# Iteration 05 — Verification & documentation

**Goal:** make the project trustworthy and easy to adopt anywhere.

**Depends on:** Iteration 04

## Stories

- **E1** Test suite for FFT, model, metrics. _(M, 5)_
- **E2** Offline cross-OS install/run tutorial (Windows/macOS/Linux, Guix where feasible). _(M, 5)_
- **E3** Tailored agent briefs (Claude Code, Codex, Gemini, Grok). _(S, 3)_

## Acceptance criteria

**E1 — Given** a clean checkout, **when** I run `clojure -M:test`,
**then** all tests pass with 0 failures and 0 errors.

**E2 — Given** a brand-new machine,
**when** I follow `../docs/`, **then** I can install a JDK + Clojure (via Guix,
Homebrew, winget, or Chocolatey) and run the forecast, with **no network access
needed after install**.

**E3 — Given** an AI agent, **when** it opens `../agents/<agent>.md`,
**then** it finds the mission, constraints, commands, and conventions for this sub-project.

## Tasks

1. `test/ft/runner.clj` (dependency-free test entry point).
2. `test/ft/{fft,predict,metrics}_test.clj`.
3. `docs/` (per-OS install, run, libraries, troubleshooting).
4. `agents/` (four files + index).

## Review

**Shipped:** E1 (12 tests / 87 assertions, all green), E2, E3.
**What changed:** the "exact extrapolation" acceptance criterion was tightened
to a **trend-free periodic signal** after Iteration 03 showed why a trended
signal cannot be exact.
**Backlog impact:** Epic F remains parked; project is at a shippable baseline.
