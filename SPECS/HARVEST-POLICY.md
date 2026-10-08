# Harvest & booking rules — agreed 2026-10-07 (Halifax)

Operator decisions recorded after the 2026-10-07 reconciliation session.

## 1. 50% partial harvest (from the NEXT harvest on)

Applies to every harvest after CRT-0050 (IMX CRT-0049 and SUI CRT-0050 were
the last full-excess harvests).

```
U = lot units, P = live Binance price, A = material anchor, T = 0.01
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
