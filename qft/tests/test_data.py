"""Tests for the CSV loader against the shared synthetic dataset."""

from __future__ import annotations

from pathlib import Path

import pytest

from qft import data

CSV = Path(__file__).resolve().parents[2] / "samples" / "trading_data.csv"


@pytest.fixture(scope="module")
def rows():
    return data.load_rows(CSV)


def test_symbols_in_file_order(rows):
    assert data.symbols(rows) == ["AAPL", "IBM", "BTC-USD", "SOL-USD"]


def test_rows_have_expected_columns(rows):
    assert set(rows[0].keys()) == set(data.COLUMNS)
    assert len(rows) == 4096


def test_series_for_parses_types(rows):
    s = data.series_for(rows, "AAPL")
    assert s["symbol"] == "AAPL"
    assert len(s["close"]) == 1024
    assert isinstance(s["close"][0], float)
    assert isinstance(s["volume"][0], int)
    assert s["timestamps"][0].endswith("Z")
