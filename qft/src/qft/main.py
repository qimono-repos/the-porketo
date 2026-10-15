"""CLI: forecast each symbol with the quantum-Fourier model and score it on a holdout."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

from . import data, metrics, predict, quantum

DEFAULTS = {
    "data": "../samples/trading_data.csv",
    "window": 512,
    "horizon": 24,
    "k": 8,
    "shots": 0,
    "out": None,
}


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="qft",
        description="Quantum-Fourier price-prediction exercise (Qiskit).",
    )
    p.add_argument("--data", default=DEFAULTS["data"], help="path to the CSV dataset")
    p.add_argument("--window", type=int, default=DEFAULTS["window"], help="power-of-two window")
    p.add_argument("--horizon", type=int, default=DEFAULTS["horizon"], help="forecast horizon (hours)")
    p.add_argument("--k", type=int, default=DEFAULTS["k"], help="number of spectral bins to keep")
    p.add_argument("--shots", type=int, default=DEFAULTS["shots"], help="if >0, also report shot-sampled top states")
    p.add_argument("--out", default=DEFAULTS["out"], help="write a JSON report to this path")
    return p


def _r6(x: float) -> float:
    return round(float(x), 6)


def analyse(opts: dict, series: dict) -> dict:
    """Evaluate one symbol: holdout errors on the last ``horizon`` points, plus a
    genuine forward forecast refit on the most recent ``window`` points."""
    window = opts["window"]
    horizon = opts["horizon"]
    k = opts["k"]
    close = np.asarray(series["close"], dtype=float)
    total = close.size

    split = total - horizon
    train = close[split - window : split]
    test = close[split:total]
    model = predict.fit(train, k)

    holdout = predict.predict_series(model, window, horizon)

    recent = close[total - window : total]
    fmodel = predict.fit(recent, k)
    forecast = predict.predict_series(fmodel, window, horizon)

    result = {
        "symbol": series["symbol"],
        "samples": int(total),
        "window": window,
        "horizon": horizon,
        "qubits": quantum.n_qubits(window),
        "k": k,
        "trend_per_hour": _r6(model.b),
        "top_components": [
            {"k": b["k"], "period_hours": _r6(b["period"]), "mag": _r6(b["mag"])}
            for b in model.bins
        ],
        "holdout": {
            "mae": _r6(metrics.mae(test, holdout)),
            "rmse": _r6(metrics.rmse(test, holdout)),
            "mape_pct": _r6(metrics.mape(test, holdout)),
            "last_actual": _r6(test[-1]),
            "last_predicted": _r6(holdout[-1]),
        },
        "forecast_next_hours": [_r6(v) for v in forecast],
    }

    if opts["shots"] > 0:
        counts = quantum.sample_qft(predict.detrend(recent), shots=opts["shots"], seed=1234)
        top = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:5]
        result["sampled_top_states"] = [
            {"state": s, "bin": int(s, 2), "count": c} for s, c in top
        ]
    return result


def main(argv: list[str] | None = None) -> int:
    opts = vars(build_parser().parse_args(argv))
    if not quantum.is_power_of_two(opts["window"]):
        print(f"error: --window must be a power of two, got {opts['window']}", file=sys.stderr)
        return 2

    print("QFT — Quantum Fourier Transform price-prediction exercise")
    print(
        f"data: {opts['data']} | window: {opts['window']} "
        f"({quantum.n_qubits(opts['window'])} qubits) | horizon: {opts['horizon']} | k: {opts['k']}"
    )
    print()

    rows = data.load_rows(opts["data"])
    results = [analyse(opts, data.series_for(rows, s)) for s in data.symbols(rows)]

    for r in results:
        print(
            f"{r['symbol']:<8}  holdout MAE={r['holdout']['mae']:<10} "
            f"RMSE={r['holdout']['rmse']:<10} MAPE={r['holdout']['mape_pct']:<7}%  "
            f"trend/h={r['trend_per_hour']}"
        )
        print("          top periods (h): " + ", ".join(f"{c['period_hours']}" for c in r["top_components"]))
        print(f"          forecast next {r['horizon']} h: {r['forecast_next_hours']}")
        if "sampled_top_states" in r:
            states = ", ".join(f"{s['state']}(bin {s['bin']}, n={s['count']})" for s in r["sampled_top_states"])
            print(f"          sampled top QFT states: {states}")
        print()

    if opts["out"]:
        report = {"model": "qiskit-qft", "results": results}
        Path(opts["out"]).write_text(json.dumps(report, indent=2) + "\n")
        print(f"wrote JSON report -> {opts['out']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
