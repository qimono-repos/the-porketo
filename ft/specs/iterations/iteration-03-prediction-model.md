# Iteration 03 — Prediction model

**Goal:** turn the spectrum into a price model that reconstructs the window and
extrapolates it forward.

**Depends on:** Iteration 02

## Stories

- **C1** Detrend the window before the FFT. _(M, 3)_
- **C2** Reconstruct the fitted signal; extrapolate beyond the window. _(M, 5)_
- **C3** Produce a genuine forward forecast refit on the latest window. _(S, 3)_

## Acceptance criteria

**C1 — Given** a perfect straight line,
**when** I call `(ft.predict/detrend ys)`,
**then** every residual is within `1e-9` of zero.

**C2 — Given** a signal that is a trend plus a single integer-frequency sine,
**when** I `fit` with `k = n/2` (every positive bin),
**then** `predict-at` reproduces the window within `1e-6`.

**C2 (extrapolation) — Given** a trend-free periodic signal centred in the window,
**when** I extrapolate past `n`,
**then** the values match the true continuation within `1e-6`.

**C3 — Given** the most recent `window` points,
**when** `predict-series` runs for `horizon` steps,
**then** it returns `horizon` finite doubles.

## Tasks

1. `linfit` (least squares), `detrend`.
2. `fit` → `{:a :b :n :spectrum :bins}`.
3. `bin-term` + `predict-at` (real-signal inverse: DC + positive bins + Nyquist).
4. `predict-series`.

## Technical notes — the two subtleties we hit

1. **Linear detrend leaks.** A phase-shifted sine is not orthogonal to the linear
   ramp over a finite window, so `linfit` absorbs a sliver of it. Consequence:
   full reconstruction of the *window* is exact, but naive extrapolation of a
   *trended* signal is approximate. We therefore test exact extrapolation only on
   a **trend-free** signal (where there is no residual line to mis-extend).
2. **Nyquist matters.** Omitting the Nyquist bin (`k = n/2`) left a small error
   even with every positive bin selected. Adding the `(-1)^t·Re(X[n/2])/n` term
   made full-bin reconstruction exact.

## Review

**Shipped:** C1, C2, C3.
**What changed:** discovered the detrend-leakage limitation during verification
(documented above); the model is exact on the window and exact on extrapolation
for periodic signals — which is the honest, testable property.
**Backlog impact:** added story **F2** (automatic component-count selection) to
address the truncation trade-off.
