# Python harvest calculator

Package layout:

```text
src/python/
├── pyproject.toml
└── qimono_harvest/
    ├── __init__.py
    ├── calculator.py
    └── cli.py
```

Run:

```bash
cd src/python
python -m qimono_harvest.cli --harvest --to ETH --current 12345 --position 0.250 --anchor 3055.3875
```

The calculator is pre-trade only. It never submits a Binance order.
