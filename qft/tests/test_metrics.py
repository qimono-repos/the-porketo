"""Tests for forecast error metrics."""

from __future__ import annotations

import numpy as np
import pytest

from qft import metrics


def test_mae():
    assert np.isclose(metrics.mae([1, 2, 3], [2, 2, 2]), 2 / 3)


def test_rmse():
    assert np.isclose(metrics.rmse([0, 0], [1, 1]), 1.0)


def test_mape():
    assert np.isclose(metrics.mape([100, 200], [110, 180]), 10.0)


def test_mape_skips_zero_actuals():
    assert np.isclose(metrics.mape([0, 100], [5, 110]), 10.0)


def test_mape_all_zero_actuals():
    assert metrics.mape([0, 0], [1, 2]) == 0.0


def test_metrics_zero_on_perfect_prediction():
    y = [1.5, 2.5, 3.5]
    assert metrics.mae(y, y) == 0.0
    assert metrics.rmse(y, y) == 0.0
    assert metrics.mape(y, y) == 0.0
