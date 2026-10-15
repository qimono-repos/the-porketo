"""Tests for the detrend + Fourier predict model."""

from __future__ import annotations

import numpy as np

from qft import predict


def test_linfit_recovers_exact_line():
    y = 3.0 + 2.5 * np.arange(10)
    a, b = predict.linfit(y)
    assert np.isclose(a, 3.0) and np.isclose(b, 2.5)


def centered_cos(n, freqs, dc=0.0, center=None):
    """Sum of cosines that is even about the window centre (zero linear coupling)."""
    if center is None:
        center = (n - 1) / 2.0
    t = np.arange(n)
    out = np.full(n, float(dc))
    for f, amp in freqs:
        out += amp * np.cos(2 * np.pi * f * (t - center) / n)
    return out


def test_detrend_removes_line_and_keeps_centered_signal():
    n = 64
    t = np.arange(n)
    line = 5.0 - 0.3 * t
    signal = centered_cos(n, [(4, 1.0)])
    d = predict.detrend(line + signal + 7.0)
    assert np.allclose(d, signal, atol=1e-9)


def test_fit_finds_dominant_bin():
    n = 64
    k = 5
    window = np.sin(2 * np.pi * k * np.arange(n) / n)
    model = predict.fit(window, k=3, transform=np.fft.fft)
    assert model.bins[0]["k"] == k
    assert np.isclose(model.bins[0]["period"], n / k)


def test_full_spectrum_reconstructs_window_exactly():
    rng = np.random.default_rng(0)
    n = 32
    window = 100.0 + rng.standard_normal(n).cumsum()
    model = predict.fit(window, k=n // 2, transform=np.fft.fft)
    recon = predict.predict_series(model, 0, n)
    assert np.allclose(recon, window, atol=1e-6)


def test_extrapolation_matches_continuation_of_a_centered_periodic_signal():
    n = 64
    freqs = [(5, 7.0), (3, 2.5), (8, 1.2)]
    center = (n - 1) / 2.0
    ys = centered_cos(n, freqs, dc=120.0)

    def true_at(t):
        return 120.0 + sum(a * np.cos(2 * np.pi * f * (t - center) / n) for f, a in freqs)

    model = predict.fit(ys, k=n // 2, transform=np.fft.fft)
    for t in (n, n + 10, n + 24, n + 100):
        assert np.isclose(predict.predict_at(model, t), true_at(t), atol=1e-6)


def test_quantum_transform_matches_classical_spectrum():
    rng = np.random.default_rng(3)
    window = rng.standard_normal(64)
    qmodel = predict.fit(window, k=5)  # default = quantum
    cmodel = predict.fit(window, k=5, transform=np.fft.fft)
    assert np.allclose(qmodel.spectrum, cmodel.spectrum, atol=1e-9)
    assert np.allclose(predict.predict_series(qmodel, 64, 8),
                       predict.predict_series(cmodel, 64, 8), atol=1e-9)
