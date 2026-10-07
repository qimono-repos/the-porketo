# New investments — watchlist expansion (HEAVY PRIORITY)

Status: OPEN
Created: 2026-10-07 (Halifax)
Deadline: **before Monday 2026-10-12** (Halifax)

## Goal

Assets in the "this week" group below must be inside the experiment before
Monday 2026-10-12, with **at least 2 USD invested in each**. From now on
these have heavy priority at every investment checkpoint.

## Trigger phrase (valid until Sunday 2026-10-11)

When the operator asks **"what are my priorities for investment?"** (or
similar wording), answer from this file: list which assets are still below
2 USD, how much each still needs, and propose the next checkpoint buy from
them. Research live prices (CoinMarketCap / Yahoo Finance) before proposing.

From **Monday 2026-10-12** the full scoring round applies to all eligible
assets (held + watchlist), using the weights below.

## Scoring weights (full round from 2026-10-12)

| Criterion | Weight |
|---|---|
| Dip below the 2-month swing high | 40% |
| Upside (analyst targets, catalysts) | 20% |
| Volatility / beta | 10% |
| Momentum — 2-month trend, 4 points two weeks apart | 5% |
| Full information: research call on latest meaningful news | 25% |

Operator note (2026-10-07): week-to-week volatility matters most in
practice, because positions are worked every 6 hours.

Eligible universe: held assets + this watchlist.

## Checkpoint budget this week

- CP4 → CP22 of 98 (2026-10-07 10:00 → 2026-10-11 22:00 Halifax) = 19 × 0.75 = 14.25 USDC.
- **IonQ 5.17 USDC counts fully** (operator decision 2026-10-07): covers
  CP4–CP9 (6 × 0.75 = 4.50) + 0.67 credit toward CP10.

### Top-up pot (operator decision 2026-10-07)

- Source: **43.00529321 USDC** — the only part of the Lemon Cash IONQ sale
  that stayed in the experiment (arrived in Binance Spot 2026-10-07).
- Use: **2.25 USDC per asset** at the slots the IonQ prepayment covered, so
  each asset reaches ≥2 in one buy.

| Slot (Halifax) | Asset | Amount | Status |
|---|---|---|---|
| CP5 — Wed 07 Oct 16:00 | AMDB | 2.25 | ✅ DONE — 0.00348042 AMDB @ 646.472 (screen 643.829, ~0.4% spread) |
| CP6 — Wed 07 Oct 22:00 | **TSMB** (replaced NVDAB, operator decision 2026-10-07) | 2.25 | TO DO |
| CP7 — Thu 08 Oct 04:00 | L1: CC (Canton), if on Convert | 2.25 | TO DO |
| CP8 — Thu 08 Oct 10:00 | Infra #1: DOT (Polkadot), if on Convert | 2.25 | TO DO |
| CP9 — Thu 08 Oct 16:00 | back to normal 0.75 cadence | — | — |

Pot after the four buys: 43.00529321 − 9.00 = **34.00529321 USDC**.

## Split (confirmed 2026-10-07; NVDAB out, TSMB in)

### This week — before Monday 2026-10-12

| Asset | Type | Invested so far | Notes |
|---|---|---|---|
| IonQ | Binance Stocks (direct) | 5.17 USDC, 2026-10-07 14:45:52 | ✅ ≥2 met — checkpoint budget (CP4–CP9) |
| AMDB (AMD) | bStock | 2.25 USDC, 2026-10-07 ~16:00 | ✅ ≥2 met — top-up pot |
| TSMB (TSMC) | bStock | 0.00 | CP6 from top-up pot. Thin volume — check spread vs TSM live price |
| MUB (Micron) | bStock | 0.00 (unconfirmed — see USDC gap below) | Checkpoint budget |
| L1 #1 — CC (Canton) | crypto | 0.00 | CP7 from top-up pot; check Convert availability |
| Infra #1 — DOT (Polkadot) | crypto | 0.00 | CP8 from top-up pot; check Convert availability |

### Out / deferred past Monday

| Slot | Candidates | Status |
|---|---|---|
| NVDAB (Nvidia) | — | OUT this week — replaced by TSMB (same AI-chip trade; NVDA already held) |
| Gaming #1 | none yet (Crypto Banter list has no gaming picks) | DEFERRED |
| Gaming #2 | none yet | DEFERRED |
| Rigetti | RGTIB not verified on Binance | DEFERRED |
| Infra #2 | HYPE, ENA, JTO | DEFERRED |

## TSMB vs DOT investigation (2026-10-07, horizon to 2026-12-31)

Estimated scores on the weights above: **DOT ≈ 5.0 vs TSMB ≈ 4.1**.
DOT wins on volatility and upside; TSMB on business quality and news.
Neither had a real dip on 2026-10-07 (TSM ~3% below its 487.47 record;
DOT ~4–5% below its 2-month high after a +45% September).
Key dates: TSMC September sales 2026-10-08, Q3 results 2026-10-15;
Polkadot Referendum 1944 (dotUSD) still deciding on 2026-10-06.
Operator chose to include TSMB anyway (conviction), dropping NVDAB.

## Wallet check 2026-10-07 (Halifax, afternoon)

- Binance Spot USDC: 107.66510093 before AMDB → **105.41510093** after.
- Expected before AMDB from known moves: 108.41510093.
- Gap: **0.75000000** — exactly one checkpoint buy; receipt not yet seen.

## Execution notes

- Binance Stocks (direct stock product): minimum order ≈ 5 USDC + 0.17
  USDC flat fee (3.4% on a 5.17 order). Overshoots a 0.75 checkpoint; when
  used, the excess prepays following checkpoints.
- Binance Convert bStocks ([ticker]B): no displayed fee, ~0.4–0.8% spread
  baked into the rate; works at 0.75.

## Close-out

When every "this week" row shows ≥ 2.00 invested (or is explicitly
dropped), set Status to DONE and note the date.
