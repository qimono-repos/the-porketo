# Iteration 03 — Prediction model

**Goal:** turn the quantum spectrum into a price model that reconstructs the
window and extrapolates it forward.

**Depends on:** Iteration 02

## Stories

- **C1** Detrend the window before the transform. _(M, 3)_
- **C2** Reconstruct the fitted signal; extrapolate beyond the window. _(M, 5)_
- **C3** Produce a genuine forward forecast refit on the latest window. _(S, 3)_

## Acceptance criteria

**C1 — Given** a perfect straight line, **when** I call `predict.detrend(ys)`,
**then** every residual is within `1e-9` of zero; and **given** a window centred
cosine, `detrend` returns the cosine within `1e-9`.

**C2 — Given** a signal that is a trend plus periodic terms, **when** I `fit` with
`k = n/2` (every positive bin), **then** `predict_at` reproduces the window within
`1e-6`.

**C2 (extrapolation) — Given** a trend-free periodic signal centred in the window,
**when** I extrapolate past `n`, **then** the values match the true continuation
within `1e-6`.

**C3 — Given** the most recent `window` points, **when** `predict_series` runs for
`horizon` steps, **then** it returns `horizon` finite floats.

**C4 — Given** the same window, **when** I fit with the quantum transform (default)
and with `numpy.fft.fft`, **then** the spectra and the extrapolated series agree
within `1e-9`.

## Tasks

1. `linfit` (least squares), `detrend`.
2. `fit` → `Model(a, b, n, k, spectrum, bins)`; `transform` parameter defaults to
   the quantum transform.
3. `_bin_term` + `predict_at` (real-signal inverse: DC + positive bins + Nyquist).
4. `predict_series`.
5. Add `tests/test_predict.py`.

## Technical notes — the two subtleties we inherited from `ft`

1. **Linear detrend leaks.** A phase-shifted sine is not orthogonal to the linear
   ramp over a finite window, so `linfit` absorbs a sliver of it. Consequence:
   full reconstruction of the *window* is exact, but naive extrapolation of a
   *trended* signal is approximate. We therefore test exact extrapolation only on
   a **trend-free, centred** signal (where there is no residual line to
   mis-extend). Our first draft of the test used a phase-0 sine (not centred) and
   failed — a useful reminder that "periodic" is not the same as "orthogonal to
   the ramp".
2. **Nyquist matters.** Omitting the Nyquist bin (`k = n/2`) leaves a small error
   even with every positive bin selected. Including the `(-1)^t·Re(X[n/2])/n`
   term makes full-bin reconstruction exact.

## Review

**Shipped:** C1, C2, C3, C4.
**What changed:** rewrote two tests to use a **centred** cosine after confirming
the detrend-leakage limitation; added an explicit **quantum-vs-classical parity**
test (C4) so the quantum path can never silently drift from the classical one.
**Backlog impact:** added story **E4** (parity with `ft`) to make the cross-check
a first-class acceptance criterion.
