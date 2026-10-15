"""Load the synthetic hourly dataset into plain Python structures.

Mirrors ``ft.data`` (the Clojure sub-project) so both exercises read the exact
same ``../samples/trading_data.csv`` file.
"""

from __future__ import annotations

import csv
from pathlib import Path

COLUMNS = ("timestamp", "symbol", "open", "high", "low", "close", "volume")
PRICE_FIELDS = ("open", "high", "low", "close")


def load_rows(path: str | Path) -> list[dict[str, str]]:
    """Read a CSV file into a list of dicts keyed by the header row."""
    with open(path, newline="") as fh:
        reader = csv.DictReader(fh)
        return [dict(row) for row in reader]


def symbols(rows: list[dict[str, str]]) -> list[str]:
    """Distinct symbols in file order."""
    seen: dict[str, None] = {}
    for row in rows:
        seen.setdefault(row["symbol"], None)
    return list(seen)


def series_for(rows: list[dict[str, str]], symbol: str) -> dict:
    """Return the full OHLCV series for one symbol, in file order."""
    rs = [r for r in rows if r["symbol"] == symbol]
    series: dict = {"symbol": symbol}
    series["timestamps"] = [r["timestamp"] for r in rs]
    for field in PRICE_FIELDS:
        series[field] = [float(r[field]) for r in rs]
    series["volume"] = [int(r["volume"]) for r in rs]
    return series
