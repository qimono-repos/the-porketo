"""Detrend + (quantum) Fourier model, with reconstruction and extrapolation.

The maths is identical to the ``ft`` Clojure sub-project; the only difference is
the source of the frequency spectrum: here it comes from the QFT
(:mod:`qft.quantum`) rather than a classical FFT. Because a real DTFT spectrum is
conjugate-symmetric, extrapolation past the fit window follows the same
``trend + DC + sum(2/n · Re(X[k]·e^{iθ})) + Nyquist`` recipe.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from dataclasses import dataclass, field

import numpy as np

from . import quantum

Transform = Callable[[Sequence[float]], np.ndarray]


def linfit(ys: Sequence[float]) -> tuple[float, float]:
    """Least-squares fit of ``y = a + b*x`` over ``x = 0..n-1``. Returns ``(a, b)``."""
    y = np.asarray(ys, dtype=float)
    n = y.size
    x = np.arange(n, dtype=float)
    denom = n * np.sum(x * x) - x.sum() ** 2
    b = 0.0 if denom == 0 else (n * np.sum(x * y) - x.sum() * y.sum()) / denom
    a = (y.sum() - b * x.sum()) / n
    return float(a), float(b)


def detrend(ys: Sequence[float]) -> np.ndarray:
    """Remove the fitted straight line from the window."""
    y = np.asarray(ys, dtype=float)
    a, b = linfit(y)
    return y - (a + b * np.arange(y.size, dtype=float))


def top_bins(spectrum: Sequence[complex], k: int) -> list[dict]:
    """The ``k`` strongest positive-frequency bins (k = 1 .. N/2-1), strongest first."""
    spec = np.asarray(spectrum)
    n = spec.size
    mags = np.abs(spec)
    bins = [
        {"k": kk, "mag": float(mags[kk]), "period": n / kk}
        for kk in range(1, n // 2)
    ]
    bins.sort(key=lambda d: d["mag"], reverse=True)
    return bins[:k]


@dataclass
class Model:
    a: float
    b: float
    n: int
    k: int
    spectrum: np.ndarray
    bins: list[dict] = field(default_factory=list)


def fit(ys: Sequence[float], k: int, transform: Transform | None = None) -> Model:
    """Fit a Fourier model to a window of prices, keeping the ``k`` strongest bins.

    ``transform`` defaults to the quantum transform
    (:func:`qft.quantum.qft_coefficients`); pass ``numpy.fft.fft`` for a classical
    cross-check.
    """
    if transform is None:
        transform = quantum.qft_coefficients
    y = np.asarray(ys, dtype=float)
    a, b = linfit(y)
    spectrum = np.asarray(transform(detrend(y)))
    return Model(a=a, b=b, n=y.size, k=k, spectrum=spectrum, bins=top_bins(spectrum, k))


def _bin_term(spectrum: np.ndarray, n: int, k: int, t: int) -> float:
    """Real contribution of positive-frequency bin ``k`` at index ``t``.

    Includes the conjugate bin's contribution: ``(2/n)·Re(X[k]·e^{iθ})``.
    """
    x_k = spectrum[k]
    theta = 2.0 * np.pi * k * t / n
    return (2.0 / n) * float(np.real(x_k * np.exp(1j * theta)))


def predict_at(model: Model, t: int) -> float:
    """Predict the price at integer index ``t`` (``t`` may exceed the window).

    Sums trend + DC + selected positive-frequency bins + the Nyquist bin (the
    real-signal inverse transform). When every positive bin is selected this
    reproduces the fitted window exactly.
    """
    n = model.n
    spectrum = model.spectrum
    dc = float(np.real(spectrum[0])) / n
    nyq = 0.0
    if n % 2 == 0:
        nyq = (float(np.real(spectrum[n // 2])) / n) * (1.0 if t % 2 == 0 else -1.0)
    sinus = sum(_bin_term(spectrum, n, b["k"], t) for b in model.bins)
    return model.a + model.b * t + dc + nyq + sinus


def predict_series(model: Model, start: int, count: int) -> list[float]:
    """Predict ``count`` points starting at index ``start``."""
    return [predict_at(model, t) for t in range(start, start + count)]
