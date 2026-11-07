# Numbers as formulas, radians and lot geometry

Design note. Started 2026-11-07 from Albert's proposal: "a formula is the best number";
store values like `sqrt(2)` or `pi/6` as text; use radians and the exponential form;
treat each lot as lines on a graph so the harvest threshold is literally a line.
Albert's framing: not *if* but *how*. This note is the how, plus where it does not help.

Prototype: [`SCRIPTS/lot_geometry.py`](../SCRIPTS/lot_geometry.py) (needs `pip install sympy`).

## 1. Two kinds of numbers

| Kind | Examples | How we store it |
|---|---|---|
| **Observed** — a venue printed it | execution price, units filled, USDC paid, fee | `Decimal128`, digit for digit as on the receipt. Never re-derived. |
| **Defined** — we decided it | investment unit, slot amount, target return, ladder steps, splits (1/3), thresholds | **formula text + its value**: `{ "expr": "2*sqrt(2)", "value": NumberDecimal("2.828427124746190097603377448419396") }` |

Why the split: a receipt is already a finite decimal (USDC has 6 decimals, Binance units 8).
The venue rounded it before we ever saw it, so no formula can recover more truth than the
receipt holds. Storing it exactly as printed is already lossless.

Defined numbers are different: `sqrt(2)`, `3/4`, `pi/6` are exact ideas. Storing them as text keeps
the idea, and the evaluated `value` (34 digits, Decimal128) keeps queries and sums cheap.
Any tool can re-evaluate `expr` to more digits when needed (sympy: unlimited).

**Intention vs execution.** When a defined amount is spent, the venue accepts a rounded amount.
Book both: `intended: {expr, value}` and the paid amount from the receipt. The difference is a
measurable rounding residue, tracked over time instead of silently lost.

Example: an investment unit of `sqrt(2)` USD is 1.41421356…, so a slot would intend
`sqrt(2)` and Binance would take 1.41 (not 1.42; 1.42 is not √2).

## 2. Beating "16 decimals"

16 significant digits is the limit of floating point (`double`). We already avoid it:
Decimal128 holds 34 digits exactly, and sympy keeps formulas exact with no digit limit until
printing. So the "16 decimals" ceiling is gone for both kinds of numbers.

## 3. Radians: where they help and where they don't

**Converting USD to radians (USD ÷ π) is not recommended.** It only rescales: it carries the same
information, turns every exact receipt amount (a fraction) into an irrational number, and every
comparison with a venue price has to convert back. More compute, no new insight.

**Radians are natural for angles, and a lot has a real angle: the profit angle.**

```
return  R = market value / anchor − 1
angle   θ = atan(R)          (radians)
θ = 0          break-even
θ = atan(r)    harvest threshold for target r (r = 1/10 → θ ≈ 0.0997 rad)
θ = π/4        +100 %
θ → −π/4       total loss
```

θ is bounded, comparable across every lot, and exact when R is a fraction
(`atan(1/10)` stays symbolic). This is the radian representation worth storing.

## 4. Exponential form

Finance already has it: the **log return** `g = ln(value / anchor)`, so `value = anchor · e^g`.
Log returns add up over time (two periods: g1 + g2), which makes them the standard for
comparing growth. Store `g` as a derived number next to θ.

For the quantum track: a lot's state can be written as `e^{iθ}` (unit phase = profit angle).
That is the same shape as a qubit phase, so if Qimono ever experiments with phase-encoded
portfolios, θ is the ready-made input. Speculative; noted, not built.

## 5. Lot geometry (the harvest line)

Normalise every lot so all lots share one picture:

```
x = price / entry price      (1 = bought price)
y = market value / anchor    (1 = break-even)
```

Every lot lies on the same line `y = x` (45°, π/4). The harvest threshold is the horizontal
line `y = 1 + r`. **Harvest when the lot's point is on or above that line.** The harvest
price is where the two lines cross: `entry × (1 + r)`.

`SCRIPTS/lot_geometry.py` prints all of this plus an ASCII chart in the console. Real lot
`TSMB@457.93` (anchor 2.25, 0.00491341 units) at 421.736, target 1/10:

```
entry price      225000000/491341  ≈ 457.93043934863974307
return           ≈ -0.0790   profit angle ≈ -0.0789 rad (threshold atan(1/10) ≈ 0.0997)
harvest price    247500000/491341  ≈ 503.72348328350371738
signal           WAIT
```

Because all lots share the same axes, every lot can go on **one** chart: points above the
harvest line are harvest candidates. That is the console/scripted view of the killer feature.

## 6. What would change in `the_porketo_db.trades` (not done yet)

Proposal, pending Albert's go:
- optional `intended: { expr, value }` on BUY/SELL events (the defined amount behind the trade);
- optional `formula` sub-documents for policy values (unit, target) in a future `policy` collection;
- θ and g stay **computed** in projections (lot views), not stored on events, per the DDD rule
  that derived values are never stored on the ledger.

Rules: formulas come only from the book or the repo, never from untrusted input (they are
parsed, so treat them like code); allowed names are `sqrt pi E exp log sin cos tan atan`.
