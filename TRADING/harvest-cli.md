# Harvest CLI

The Qimono Trading harvest calculator implements the active 50% partial-harvest policy.

It is intentionally **pre-trade only**. It calculates a target and gives the Binance Convert URL. It does not place an order.

## Formula

For the selected strategy lot:

$$
V = U \\times P
$$

$$
E = V-A
$$

$$
H_{\\text{calc}} = \\frac{E}{P}
$$

$$
\\boxed{
H_{50}
=
\\operatorname{RoundDown}_{\\text{Binance}}
\\left(
\\frac{(U\\times P)-A}{2P}
\\right)
}
$$

The lot must first satisfy:

$$
U \\times P \\ge A + T
$$

where $T$ is the target-profit threshold, currently defaulting to $0.01$.

## CLI

The repository includes a small launcher so the intended interface is:

```bash
./the-porketo --harvest --to ETH --current 12345 --position 0.250 --anchor 3055.3875
```

The placeholder values above intentionally produce:

$$
\\frac{(0.250\\times12345)-3055.3875}{2\\times12345}
=0.00125\\ \\text{ETH}
$$

So the action-oriented output is:

```text
GO TO https://www.binance.com/en/convert/ETH/USDT
sell 0.00125 ETH
expected proceeds ≈ 15.43125 USDT
```

Note the important unit distinction: **you sell ETH; the proceeds are USDT.** The command must therefore say `sell 0.00125 ETH`, not `sell 0.00125 USDT`.

The material anchor is required because current price and position alone are insufficient to calculate the harvest quantity.

Make the launcher executable after cloning:

```bash
chmod +x the-porketo harvest.py
```

## Python

The underlying implementation is also directly runnable:

```bash
python3 harvest.py --harvest --to ETH --current 12345 --position 0.250 --anchor 3055.3875
```

It uses `Decimal` and rounds downward to the supplied Binance quantity step.

## Clojure

The same calculation is available as a REPL-friendly Clojure program:

```bash
clj -M harvest.clj --harvest --to ETH --current 12345 --position 0.250 --anchor 3055.3875
```

It uses arbitrary-precision `BigDecimal` arithmetic.

Both implementations accept either `--harvest` or `-harvest`.

## Binance precision

The `--step` argument represents the executable quantity step that must be verified against the live Binance execution context.

The development default is `0.000001`, but **never treat that default as authoritative for a live trade**.

If Binance displays a different executable quantity, price, proceeds, fee, or constraint, the Binance receipt wins and the actual execution must be recorded in the source event log.

## Safety boundary

This CLI does **not** connect to Binance, authenticate, submit orders, or mutate the trading book.

It is a deterministic pre-trade calculator:

**strategy data → calculation → Binance URL + target quantity → human verification → actual Binance execution → receipt → book**
