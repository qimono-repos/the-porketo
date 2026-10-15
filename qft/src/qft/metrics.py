"""Forecast error metrics."""

from __future__ import annotations

import math
from collections.abc import Sequence

import numpy as np


def mae(actual: Sequence[float], pred: Sequence[float]) -> float:
    """Mean absolute error."""
    a = np.asarray(actual, dtype=float)
    p = np.asarray(pred, dtype=float)
    return float(np.mean(np.abs(a - p)))


def rmse(actual: Sequence[float], pred: Sequence[float]) -> float:
    """Root mean squared error."""
    a = np.asarray(actual, dtype=float)
    p = np.asarray(pred, dtype=float)
    return float(math.sqrt(np.mean((a - p) ** 2)))


def mape(actual: Sequence[float], pred: Sequence[float]) -> float:
    """Mean absolute percentage error (%). Zero actuals are skipped."""
    a = np.asarray(actual, dtype=float)
    p = np.asarray(pred, dtype=float)
    mask = a != 0
    if not mask.any():
        return 0.0
    return float(100.0 * np.mean(np.abs((p[mask] - a[mask]) / a[mask])))
