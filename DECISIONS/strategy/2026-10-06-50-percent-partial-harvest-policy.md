# Decision: 50% Partial Harvest Policy

- **Date:** 2026-10-06
- **Status:** Active standing rule
- **Scope:** Crypto harvests in the Trading book, with the policy intended to govern all future harvest calculations unless explicitly overridden by a later decision.

## Decision

From this point forward, when a strategy lot crosses its harvest criterion, the project harvests **50% of the quantity produced by the legacy harvest formula**, rounded **down** to a Binance-compatible precision.

The governing rule is:

$$
H_{50}
=
\operatorname{RoundDown}_{\text{Binance}}
\left(
\frac{H_{\text{legacy}}}{2}
\right)
$$

where:

- $H_{\text{legacy}}$ is the quantity produced by the existing harvest formula.
- $H_{50}$ is the new executable target quantity.
- $\operatorname{RoundDown}_{\text{Binance}}$ means round downward, never upward, to the precision accepted for the Binance conversion.

In compact pseudocode:

```text
H₅₀ = round_down_to_binance_precision(H_legacy / 2)
```

> **The 50% rule applies to the calculated harvest quantity, not to the strategy lot's material anchor.**

This is a **quantity rule**. It does not change the harvest criterion, the material anchor, or the highest-active-rung selection protocol.

## Why 50%?

The change deliberately makes harvests more conservative.

It reduces:

- fee and friction exposure,
- quote drift between calculation and execution,
- slippage risk,
- minimum-precision / dust problems,
- accidental over-harvesting during fast market movement.

The intent is to liberate part of the excess while retaining meaningful exposure in the strategy lot.

## Formal Mechanics

Let the legacy calculation produce a quantity $H_{\text{legacy}}$.

First take exactly half:

$$
H_{\text{half}} = \frac{H_{\text{legacy}}}{2}
$$

Then apply Binance-compatible downward rounding:

$$
\boxed{
H_{\text{target}}
=
\operatorname{RoundDown}_{\text{Binance}}
\left(
H_{\text{half}}
\right)
}
$$

Therefore:

$$
\boxed{
H_{\text{target}}
=
\operatorname{RoundDown}_{\text{Binance}}
\left(
\frac{H_{\text{legacy}}}{2}
\right)
}
$$

The important ordering is:

**legacy calculation → divide by 2 → round down → Binance execution**

Never:

**legacy calculation → round → divide by 2 → round**

and never round upward merely to reach the theoretical target.

## Worked Example

Suppose the legacy formula produces:

$$
H_{\text{legacy}} = 0.02411932\ \text{AAVE}
$$

Half is:

$$
H_{\text{half}}
=
\frac{0.02411932}{2}
=
0.01205966\ \text{AAVE}
$$

The executable target is then:

$$
H_{\text{target}}
=
\operatorname{RoundDown}_{\text{Binance}}
(0.01205966)
$$

The final quantity must be checked against Binance's live conversion constraints before execution.

### Python reference implementation

Use decimal arithmetic for the calculation, not binary floating-point arithmetic:

```python
from decimal import Decimal, ROUND_DOWN

def harvest_50_percent(legacy_qty: str, binance_step: str) -> Decimal:
    qty = Decimal(legacy_qty)
    step = Decimal(binance_step)

    half = qty / Decimal("2")
    return (half / step).to_integral_value(rounding=ROUND_DOWN) * step


target = harvest_50_percent("0.02411932", "0.000001")
print(target)
# 0.012059
```

The `binance_step` value must come from the applicable live Binance market/conversion constraints. It must not be guessed.

### Clojure reference implementation

The same rule can be expressed with arbitrary-precision `BigDecimal` arithmetic:

```clojure
(import '[java.math BigDecimal RoundingMode])

(defn harvest-50-percent [legacy-qty binance-step]
  (let [qty  (BigDecimal. legacy-qty)
        step (BigDecimal. binance-step)
        half (.divide qty (BigDecimal. "2") 18 RoundingMode/HALF_UP)
        n    (.setScale (.divide half step 0 RoundingMode/DOWN) 0 RoundingMode/DOWN)]
    (.multiply n step)))

(harvest-50-percent "0.02411932" "0.000001")
;; => 0.012059
```

These snippets are **reference implementations**, not substitutes for verifying the live Binance constraints.

## Accounting Rules

1. The strategy lot's **material anchor does not change** because of a harvest.
2. The strategy lot's **remaining units decrease by the actual executed quantity**.
3. The event log records the **actual Binance execution**, not the calculated target.
4. The Binance receipt remains execution truth.
5. The calculation is a pre-trade target only.
6. The applicable Binance precision/step must be verified from the live execution context.
7. If Binance requires a smaller executable quantity, use the valid rounded-down quantity.
8. Never round upward merely to reach the calculated target.
9. A partial harvest is still a harvest. Do not create a new strategy lot.
10. Multiple active rungs continue to follow the existing **highest-active-rung** selection protocol. The 50% rule changes the quantity harvested from the selected rung; it does not change which rung is selected.
11. If the resulting quantity is below Binance's executable minimum, do not fabricate an order. Preserve the signal for a later executable opportunity.

## Historical Precedent

On 2026-10-06, the operator independently executed a conservative partial harvest of:

$$
0.02411932\ \text{AAVE}
\rightarrow
4.23045\ \text{USDT}
$$

That execution is historical execution truth and is **not retroactively rewritten** by this policy.

The new 50% rule governs future harvest calculations.

## Relationship to Fee/Friction Policy

This policy is complementary to the existing conservative-friction policy.

A 50% harvest does **not** remove the requirement to apply the project's established fee/friction treatment.

## Verification Sequence

Before proposing a harvest:

1. Verify the current strategy-lot state.
2. Verify that the harvest criterion has been crossed.
3. Calculate $H_{\text{legacy}}$ using the established formula.
4. Calculate $H_{\text{legacy}} / 2$.
5. Verify the applicable Binance precision and execution constraints.
6. Round **down** to the Binance-compatible quantity.
7. Present the target quantity and expected quote proceeds.
8. Execute only against the live Binance conversion/execution interface.
9. Treat the Binance receipt as execution truth.
10. Record actual execution data in the source event log.
11. Recalculate the derived position and strategy lot.
12. Read the Dashboard last.

## Precedence

This is an active standing strategy decision.

A later dated decision may explicitly revise or supersede it. Historical executions remain immutable.
