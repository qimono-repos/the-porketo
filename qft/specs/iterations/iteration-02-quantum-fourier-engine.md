# Iteration 02 — Quantum Fourier engine

**Goal:** amplitude-encode a real window and apply the QFT, exposing coefficients
that provably equal the classical DFT.

**Depends on:** Iteration 01

## Stories

- **B1** Amplitude-encode + apply the QFT. _(M, 5)_
- **B2** Coefficients equal `numpy.fft.fft`. _(M, 3)_
- **B3** Reject non power-of-two windows. _(M, 1)_
- **B4** Strongest positive-frequency bins with periods. _(M, 2)_
- **B5** Optional shot-sampled path (Aer). _(S, 3)_

## Acceptance criteria

**B1 — Given** a real window, **when** I call `qft.quantum.qft_statevector(x)`,
**then** I get a normalised complex statevector, and QFT-then-inverse-QFT returns
the encoded state within `1e-9`.

**B2 — Given** a real window of length 4/8/16/64/512,
**when** I call `qft.quantum.qft_coefficients(x)`,
**then** it equals `numpy.fft.fft(x)` within `1e-9`.

**B3 — Given** a length-7 vector, **when** I call `qft_coefficients`,
**then** it raises `ValueError` mentioning "power of two".

**B4 — Given** a length-64 cosine of frequency 5, **when** I call
`predict.top_bins(spectrum, 1)`, **then** the top bin's `k` is `5`.

**B5 — Given** a length-16 cosine of frequency 3 and `shots=4000`,
**when** I call `qft.quantum.sample_qft(x)`, **then** the measured arg-max is in
`{3, 13}` and matches the exact distribution's arg-max.

## Tasks

1. Wrap `QFTGate(n)` and `Statevector`; add `qft_statevector`, `qft_coefficients`.
2. Add `is_power_of_two`, `n_qubits`, `qft_probabilities`.
3. Add `sample_qft` using `AerSimulator` (with `transpile` + `measure_all`).
4. Add `dft_reference` (NumPy) for tests.
5. Add `tests/test_quantum.py`.

## Technical notes — the two subtleties we hit

1. **Sign/conjugation convention.** Qiskit's QFT uses a *positive* exponent and
   `1/√N` scaling, `y_j = (1/√N)Σ_k e^{+2πijk/N} v_k`. The standard forward DFT
   (what `np.fft.fft` returns for a real signal) is the conjugate sum, so
   `X_j = √N·conj(y_j)`. We verified this empirically and codify it in
   `qft_coefficients`; the DFT-equality test locks it down.
2. **Amplitude encoding is phase-clean.** `QuantumCircuit.initialize` prepares the
   exact state with no residual global phase (verified: prep state equals the
   input to machine precision), so no phase correction is needed.

Also learned during implementation: **Aer cannot run the composite `qft`
instruction** (`unknown instruction: qft`) — the circuit must be `transpile`d
first. Handled inside `sample_qft`.

## Review

**Shipped:** B1–B5.
**What changed:** adopted `QFTGate` instead of the `QFT` class after Qiskit 2.5
emitted a deprecation warning (removal scheduled in 3.0). Added `transpile` to
the shot path after the first Aer run failed.
**Backlog impact:** none.
