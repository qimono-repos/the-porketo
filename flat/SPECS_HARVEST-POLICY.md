# Harvest & booking rules — agreed 2026-10-07 (Halifax)

Operator decisions recorded after the 2026-10-07 reconciliation session.

## 1. 50% partial harvest (from the NEXT harvest on)

Applies to every harvest after CRT-0050 (IMX CRT-0049 and SUI CRT-0050 were
the last full-excess harvests). First 50%-rule harvest: CRT-0052 (NEAR).

```
U = lot units, P = live Binance Convert rate, A = material anchor, T = 0.01
Eligible when  U × P ≥ A + T
E      = U × P − A
H_50   = E / (2 × P)
H_final = RoundDown_Binance(H_50)      ← native units to sell
Expected USDT ≈ H_final × P            ← actual proceeds come from the receipt
```

The 50% applies to the calculated excess, never to the whole position.
Lot selection: highest active rung per market (lot above threshold with the
highest entry). Harvests settle into USDT.

## 2. Below-anchor lots are frozen for harvest

If a harvest leaves a lot below its anchor (e.g. PUMP after CRT-0047, anchor
15.00), that lot is not harvested again until its value is back above anchor +
0.01. Buying more of the asset is still allowed.

## 3. Blended top-up anchors (Oct 3 top-ups CRT-0039…CRT-0044)

Top-ups "toward a 15 USDC anchor" blend into the existing lot:

| Lot | Anchor | Units (2026-10-07) |
|---|---|---|
| ILV | 15 | 3.50209731 |
| SLP (original lot) | 15 | 20630.36983 |
| GALA | 15 | 5960.600446 |
| NEAR | 15 | 3.19627575 |
| SUI (first lot, CRT-0015) | 2 + 11 = 13 | 12.04880717 |
| PUMP | 15 | 2129.94 (after CRT-0047) |

## 4. [ticker]B tokens are stock-side

Every Binance asset named [ticker]B (IBMB, HOODB, AMDB, TSMB, MUB…) is booked
in the stock chart (Trades / Positions / Sprint), never crypto. Verify the
underlying first — a trailing B alone is not proof (BNB, OKB). Planned: unify
crypto and stock into one chart later.

## 5. USDT = initial capital + harvests only

USDT present in the wallet before the harvest flow is initial capital, booked
once as a reconciliation (CRR-0004, 4.23045 USDT, so book = wallet =
14.16586201 after CRT-0050). From now on USDT only grows through harvests.

## Also agreed earlier on 2026-10-07

- Harvest checkpoints every 6 h, 15 min after each investment checkpoint;
  rule active from Harvest 6 (2026-10-07 22:15 Halifax), no backlog for 1–5.
- A no-go harvest triggers a forced harvest: sell 50% of the anchor of the lot
  with the smallest dollar gap below its threshold.
- A harvest done early may cover a later harvest slot (one harvest = one slot).

---

## Worked example — CRT-0052, NEAR (2026-10-08 ~05:35 Halifax)

First harvest under the 50% rule. Covers **Harvest 8 of 98** (Thu 10:15 slot,
harvested early). Use this as the template for every harvest.

### Step 0 — pick the lot (and why AAVE was skipped)

The Crypto Sprint signals (live prices from the Prices tab, CoinGecko
snapshot 05:20) ranked AAVE @ 125.58 first (excess ≈ 7.36). On the Convert
screen the wallet showed **0.13388068 AAVE** while the book lot says
**0.158 AAVE** → 0.02411932 AAVE was sold earlier and never booked. Selling the
book-computed 0.0213 would have pushed the real lot **below its anchor**
(≈ 19.38 vs 19.84). **AAVE frozen until reconciled.** Next candidate: NEAR.

### Step 1 — verify wallet units = book units

| | Value |
|---|---|
| Book lot | NEAR @ 4.6930 (CRT-0012 + CRT-0042 top-up, blended) |
| Book units U | 3.19627575 NEAR |
| Wallet balance on Convert screen | 3.19627575 NEAR ✅ match |
| Anchor A | 15.00 USDC · threshold 15.01 |

If wallet ≠ book: **stop**, reconcile first.

### Step 2 — use the Convert rate, not the chart

Screen showed chart price 5.222 but Convert rate **1 NEAR ≈ 5.315 USDT**.
The executable rate is P.

### Step 3 — compute

```
V      = 3.19627575 × 5.315          = 16.99
E      = 16.99 − 15.00               = 1.99   (eligible: 16.99 ≥ 15.01)
H_50   = 1.99 / (2 × 5.315)          = 0.187
H_final = RoundDown(0.187)           = 0.18 NEAR
Expected ≈ 0.18 × 5.315              = 0.957 USDT
Kept   = 3.01627575 NEAR × 5.315     ≈ 16.03 (above 15.01 ✅)
Cancel condition: quote below 0.95 USDT (spread > ~1%)
```

### Step 4 — execute and read the receipt

| Receipt field | Value |
|---|---|
| Sold | 0.18 NEAR |
| Received | **0.95669263 USDT** |
| Displayed rate | 1 USDT = 0.188148 NEAR (≈ 5.3149) |
| Fee | 0 USDT |
| Method | Binance Convert · Spot Wallet + Funding wallet |

### Step 5 — book it

- Crypto Trades: **CRT-0052** NEAR SELL, quote USDT, 0.95669263, price
  5.314879, units 0.18, USDC wallet flow 0, USDT wallet flow +0.95669263.
- Crypto Sprint: NEAR units 3.19627575 → **3.01627575**; anchor unchanged 15.00.
- USDT book: 14.16586201 → **15.12255464**.
- Lot still shows ⚡ HARVEST afterwards — expected under the 50% rule (half
  the excess stays invested).

### Checklist (copy for every harvest)

1. Lot = highest active rung; not frozen (below-anchor) and not under reconciliation.
2. Wallet units on Convert screen = book units. Mismatch → stop.
3. P = Convert rate (not chart).
4. H_final = RoundDown((U×P − A) / (2P)); confirm kept value ≥ A + 0.01.
5. Cancel if quote < expected × 0.99.
6. Book receipt: Crypto Trades row + Crypto Sprint units + USDT check vs wallet.
