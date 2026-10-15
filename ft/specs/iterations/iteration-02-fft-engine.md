# Iteration 02 — Fourier engine

**Goal:** expose a correct, guarded forward FFT and the strongest frequency bins.

**Depends on:** Iteration 01

## Stories

- **B1** Forward FFT of a real vector. _(M, 3)_
- **B2** Reject non power-of-two lengths. _(M, 1)_
- **B3** Strongest positive-frequency bins with periods. _(M, 2)_

## Acceptance criteria

**B1 — Given** `[5 5 5 5]`,
**when** I call `(ft.fft/forward xs)`,
**then** I get 4 `[re im]` pairs and all energy is in bin 0 (magnitude 20).

**B2 — Given** a 3-element vector,
**when** I call `forward`,
**then** it throws `ExceptionInfo` mentioning "power of two".

**B3 — Given** a length-8 cosine of frequency 2,
**when** I call `(ft.fft/top-bins spectrum 1)`,
**then** the top bin's `:k` is `2`.

## Tasks

1. Wrap `org.apache.commons.math3.transform.FastFourierTransformer` (`DftNormalization/STANDARD`).
2. Add `power-of-two?`, `magnitudes`, `bands`, `top-bins`.
3. Add `test/ft/fft_test.clj`.

## Technical notes

- Commons Math's forward transform is `X[k] = Σ x[n]·e^{-2πikn/N}` (STANDARD), so the raw FFT *is* the standard DFT with `k` = cycles per window.
- `bands` excludes DC (k=0) and Nyquist (k=N/2); `top-bins` ranks the rest.
- `:period = N/k` reports the detected cycle length in hours.

## Review

**Shipped:** B1, B2, B3.
**What changed:** B3 originally returned raw magnitudes; refined to include `:period` so reports read in hours.
**Backlog impact:** none.
