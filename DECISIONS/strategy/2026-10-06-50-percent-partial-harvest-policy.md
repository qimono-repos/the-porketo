# Decision: 50% Partial Harvest Policy

- **Date:** 2026-10-06
- **Status:** Active standing rule
- **Scope:** Crypto harvests in the Trading book, with the policy intended to govern all future harvest calculations unless explicitly overridden by a later decision.

## Decision

From this point forward, when an open strategy lot crosses its harvest criterion, the project harvests **50% of the calculated excess position**, rounded **down** to a Binance-compatible executable precision.

The calculation is expanded explicitly from the strategy-lot quantities and current market price.

Let:

- $U$ = current units held in the selected strategy lot
- $P$ = verified current market price of the asset in the strategy lot's quote currency
- $A$ = material anchor of the selected strategy lot
- $V$ = current market value of the lot

First calculate current market value:

$$
V = U \times P
$$

Then calculate the excess value above the material anchor:

$$
E = V - A
$$

Therefore:

$$
E = (U \times P) - A
$$

Convert that excess value back into asset units:

$$
H_{\text{calc}}
=
\frac{E}{P}
$$

Substituting the expanded expression for $E$:

$$
H_{\text{calc}}
=
\frac{(U \times P)-A}{P}
$$

which is equivalently:

$$
H_{\text{calc}}
=
U - \frac{A}{P}
$$

The new 50% harvest target is therefore:

$$
\boxed{
H_{50}
=
\operatorname{RoundDown}_{\text{Binance}}
\left(
\frac{1}{2}
\left[
\frac{(U \times P)-A}{P}
\right]
\right)
}
$$

or, in its simplified form:

$$
\boxed{
H_{50}
=
\operatorname{RoundDown}_{\text{Binance}}
\left(
\frac{U - A/P}{2}
\right)
}
$$

This is the canonical harvest formula.

### Trigger condition

The quantity calculation is performed only after the strategy lot has crossed its documented harvest criterion:

$$
V \geq A + T
$$

where $T$ is the strategy lot's target-profit threshold.

Equivalently:

$$
U \times P \geq A + T
$$

The target-profit threshold determines **when a lot becomes harvest-eligible**. It is not subtracted from the excess quantity being harvested.

## Operational Sequence

The complete calculation is:

$$
\boxed{
\text{Units}
\rightarrow
\text{Market Value}
\rightarrow
\text{Excess Value}
\rightarrow
\text{Excess Units}
\rightarrow
50\%
\rightarrow
\text{Round Down}
\rightarrow
\text{Binance}
}
$$

More explicitly:

$$
U
\xrightarrow{\times P}
V
\xrightarrow{-A}
E
\xrightarrow{/P}
H_{\text{calc}}
\xrightarrow{/2}
H_{50}
\xrightarrow{\operatorname{RoundDown}_{\text{Binance}}}
H_{\text{target}}
$$

The order matters.

Do not round before dividing by two.

Do not round upward.

Do not calculate 50% of the material anchor.

Do not change the material anchor.

## Worked Example: AAVE

For the AAVE strategy lot:

$$
U = 0.158\ \text{AAVE}
$$

$$
A = 19.84164\ \text{USDC}
$$

Using a verified market price of approximately:

$$
P = 179.13\ \text{USDT/AAVE}
$$

First calculate market value:

$$
V = 0.158 \times 179.13
$$

$$
V = 28.30254\ \text{USDT}
$$

Then calculate excess value:

$$
E = 28.30254 - 19.84164
$$

$$
E = 8.46090\ \text{USDT}
$$

Convert the excess back into AAVE:

$$
H_{\text{calc}}
=
\frac{8.46090}{179.13}
$$

$$
H_{\text{calc}}
\approx 0.04723329\ \text{AAVE}
$$

Apply the new 50% rule:

$$
H_{50}
=
\frac{0.04723329}{2}
$$

$$
H_{50}
\approx 0.02361665\ \text{AAVE}
$$

The actual executable quantity is then:

$$
H_{\text{target}}
=
\operatorname{RoundDown}_{\text{Binance}}
(0.02361665)
$$

The final precision/step must come from the live Binance execution context.

## Reference Implementations

### Python

Use decimal arithmetic for financial quantities rather than binary floating-point arithmetic:

```python
from decimal import Decimal, ROUND_DOWN

def round_down_to_step(quantity: Decimal, step: Decimal) -> Decimal:
    return (quantity / step).to_integral_value(
        rounding=ROUND_DOWN
    ) * step


def harvest_50_percent(
    units: str,
    price: str,
    material_anchor: str,
    binance_step: str,
) -> Decimal:
    U = Decimal(units)
    P = Decimal(price)
    A = Decimal(material_anchor)
    step = Decimal(binance_step)

    market_value = U * P
    excess_value = market_value - A
    calculated_harvest = excess_value / P
    half_harvest = calculated_harvest / Decimal("2")

    return round_down_to_step(half_harvest, step)


target = harvest_50_percent(
    "0.158",
    "179.13",
    "19.84164",
    "0.000001",
)

print(target)
```

### Clojure

Use arbitrary-precision `BigDecimal` arithmetic:

```clojure
(import '[java.math BigDecimal RoundingMode])

(defn round-down-to-step [quantity step]
  (let [n (.divide quantity step 0 RoundingMode/DOWN)]
    (.multiply n step)))

(defn harvest-50-percent
  [units price material-anchor binance-step]
  (let [U    (BigDecimal. units)
        P    (BigDecimal. price)
        A    (BigDecimal. material-anchor)
        step (BigDecimal. binance-step)

        market-value
        (.multiply U P)

        excess-value
        (.subtract market-value A)

        calculated-harvest
        (.divide excess-value P 18 RoundingMode/HALF_UP)

        half-harvest
        (.divide calculated-harvest
                 (BigDecimal. "2")
                 18
                 RoundingMode/HALF_UP)]

    (round-down-to-step half-harvest step)))

(harvest-50-percent
  "0.158"
  "179.13"
  "19.84164"
  "0.000001")
```

These are reference implementations. The applicable Binance precision, step size, minimum executable quantity, and live conversion constraints must always be verified before execution.

## Accounting Rules

1. The strategy lot's **material anchor does not change** because of a harvest.
2. The strategy lot's **remaining units decrease by the actual executed quantity**.
3. The event log records the **actual Binance execution**, not the calculated target.
4. The Binance receipt remains execution truth.
5. The calculation is a pre-trade target only.
6. $P$ must come from a verified current market-price source appropriate to the screening stage.
7. Binance execution constraints must be verified at execution time.
8. If Binance requires a smaller executable quantity, use the valid rounded-down quantity.
9. Never round upward merely to reach the calculated target.
10. A partial harvest is still a harvest. Do not create a new strategy lot.
11. Multiple active rungs continue to follow the existing **highest-active-rung** selection protocol. The 50% rule changes the quantity harvested from the selected rung; it does not change which rung is selected.
12. If the resulting quantity is below Binance's executable minimum, do not fabricate an order. Preserve the signal for a later executable opportunity.

## Historical Precedent

On 2026-10-06, the operator independently executed a conservative partial harvest of:

$$
0.02411932\ \text{AAVE}
\rightarrow
4.23045\ \text{USDT}
$$

That execution is historical execution truth and is **not retroactively rewritten** by this policy.

The new formula governs future harvest calculations.

## Relationship to Fee/Friction Policy

This policy is complementary to the existing conservative-friction policy.

A 50% harvest does **not** remove the requirement to apply the project's established fee/friction treatment.

## Verification Sequence

Before proposing a harvest:

1. Verify the current strategy-lot state and selected rung.
2. Verify that the harvest criterion has been crossed.
3. Verify the current price $P$.
4. Calculate market value $V=U\times P$.
5. Calculate excess value $E=V-A$.
6. Calculate excess units $H_{\text{calc}}=E/P$.
7. Divide the calculated quantity by 2.
8. Verify the applicable Binance precision and execution constraints.
9. Round **down** to the Binance-compatible quantity.
10. Present the target quantity and expected quote proceeds.
11. Execute only against the live Binance conversion/execution interface.
12. Treat the Binance receipt as execution truth.
13. Record actual execution data in the source event log.
14. Recalculate the derived position and strategy lot.
15. Read the Dashboard last.

## Precedence

This is an active standing strategy decision.

A later dated decision may explicitly revise or supersede it. Historical executions remain immutable.
