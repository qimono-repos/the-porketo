# Harvest CLI

The Qimono Trading harvest calculator implements the active 50% partial-harvest policy.

It is intentionally **pre-trade only**. It calculates a target and gives the Binance Convert URL. It does not place an order.

## Formula

For the selected strategy lot:

$$
V = U \times P
$$

$$
E = V-A
$$

$$
H_{\text{calc}} = \frac{E}{P}
$$

$$
\boxed{
H_{50}
=
\operatorname{RoundDown}_{\text{Binance}}
\left(
\frac{(U\times P)-A}{2P}
\right)
}
$$

Where:

- $U$ = current units in the selected strategy lot
- $P$ = verified current price
- $A$ = material anchor
- $V$ = current market value
- $E$ = excess value above the material anchor

The lot must first satisfy:

$$
U \times P \ge A + T
$$

where $T$ is the target-profit threshold, currently defaulting to $0.01$.

## Python

```bash
python3 harvest.py --harvest --to ETH --current 12345 --position 0.250 --anchor 3055.3875
```

Output is intentionally action-oriented:

```text
GO TO https://www.binance.com/en/convert/ETH/USDT
sell <quantity> ETH
expected proceeds ≈ <amount> USDT
```

The example numbers above are placeholders. A real calculation requires the selected strategy lot's **material anchor**.

## Clojure

```bash
clj -M harvest.clj --harvest --to ETH --current 12345 --position 0.250 --anchor 3055.3875
```

Both implementations use decimal / arbitrary-precision arithmetic and round downward to the supplied Binance quantity step.

**Never guess the Binance step.** The default exists only as a convenient development value. Verify the live Binance execution constraints before executing.

## Important distinction

The CLI target is a calculation.

The Binance receipt is execution truth.

If Binance displays a different executable quantity, price, proceeds, fee, or constraint, the receipt wins and the actual execution must be recorded in the source event log.
