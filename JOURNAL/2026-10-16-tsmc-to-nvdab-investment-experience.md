# Experience: from TSMC case study to NVDAB investment

**Date:** 2026-10-16, ~03:00–07:30 ART (GMT−3). **Operator:** Albert. **Agents:** ChatGPT (research), Claude (review, criteria, booking).
**Outcome:** successful end-to-end investment mechanics, wallet verified.

## 0. The proxy chain (purpose of this exercise)

**TSMB → TSMC → NVDA**

- TSMB is a proxy for TSMC (tokenized stock → underlying).
- TSMC is a proxy for NVIDIA (TSMC fabs NVIDIA's chips; NVIDIA is its largest AI customer).
- The investigation started at TSMB/TSMC and followed the chain to NVIDIA, ending in the NVDAB investment.

Recorded in the book: `Positions!V` ("Proxy For") — TSMB row = `TSMB + TSMC + NVDA`, NVDAB row = `NVDAB + NVDA`.

**Why it matters (operator intent):** discovering proxies is the point of these manual exercises. Later in the experiment the same work is to be done not by hand but with **correlations** and **dimension discovery with big data** — finding which assets move together and which hidden factors drive them. Each hand-discovered chain is a labelled example to test those methods against.

## 1. Starting point: TSMC (ChatGPT)
- ChatGPT wrote `INSIGHTS/Case Study TSMC.md` (commit baba15e, 03:05Z).
- Facts: TSMC Q3 revenue US$46.72bn (+41.2% YoY), net income NT$763.06bn (+68.7%), GM 66.4%, NPM 51.1%; Q4 guide US$52.3–54.3bn (~14.1% sequential at midpoint, verified); node mix 3nm 33%, 5nm 28%, 7nm 10%, 2nm 8%.
- Verdict: positive fundamentals, no confirmed intraday buy signal.
- The study used NVDA as the intraday proxy (scenario table keyed off NVDA prior low 212.85, 15 Oct close 217.23) — the second link of the chain.

## 2. Claude's review of the study
- Strength: separates facts, calculations and inferences; no fabricated URLs.
- Gaps: (a) analysed NVDA while our money sits in TSMB (lots @476.77 and @457.93, ~8–11.5% under anchor), so the pre-catalyst-pullback rule on TSMB was missed; (b) attributed the drop to "valuation/risk appetite" instead of rates and funding (Sept CPI 3.7%, 10-yr ~5.09%, failed AI-infra IPO, bank limits on AI loans); (c) opening-range timing does not fit 6-hourly 24/7 bStocks slots; (d) file name has spaces.

## 3. Market context used
- Oct 13–15 selloff driven by rates and funding, not AI demand: Kospi −5.5% / −8%, BTC sub-$80k leverage flush then >$82.5k, MU record revenue and HBM sold out through 2027, TSMC record Q3 yet stock slipped.
- NVDA news: Huang on not backstopping CoreWeave, inside the AI-funding worry.

## 4. The NVDAB decision and the mistake
- First call: skip NVDAB. Dip measured against the lot anchor (224.587) looked ~3%.
- Operator's live Binance convert screen (07:07): NVDAB/USDC 217.653, past week −7.40%, 9 Oct high 235.059, 15 Oct low 214.065.
- Measured against the swing high (the correct investment yardstick), the dip is ~7.4%. Call revised: **Tier C, one unit (0.75 USDC)**; remaining two units to TSMB as Tier B.
- Watch levels: break and hold below 214 = upgrade to Tier B next slot; reclaim ~225 = dip gone, don't add.
- Mistake logged in `INSIGHTS/mistakes/2026-10-16-nvdab-wrong-dip-yardstick.md`.

## 5. Process fix
- Created `DECISIONS/strategy/2026-10-16-buy-and-harvest-decision-criteria.md` (commit 10d7c8b): Investment = market (swing high + news); Harvest = lot (anchor vs live price).
- Mandatory-read block at top of README (commit 2e599f2).
- Section 0 added: 50% anchor rule is the operating rule; information/Fourier triggers are research until backtested (commit 8e1e57d).
- Read all of INSIGHTS and reconciled it with the criteria.
- Naming rule from operator: in this project, buy = **investment**, sell = **harvest**.

## 6. Execution (investment)
- Binance Convert confirm screen: **0.75 USDC → 0.00343728 NVDAB**, rate 218.196 USDC, fee 0, Spot + Funding wallet.
- Prior holding 0.01001839 NVDAB (lot STT-0037 @224.587).
- Expected after: 0.01345567 NVDAB ≈ $2.93.
- **Wallet verified by operator: 0.01345567 NVDAB, $2.93. Exact match.**
- New lot: NVDAB @218.196, anchor 0.75, Tier C. Book entry pending; replace confirm-screen data with the receipt.

## 7. What worked
- Live venue screen as price truth instead of the book's stale prices.
- Operator challenge caught the agent's wrong yardstick before money moved.
- Pre-computing the expected wallet balance made verification instant.
- Following the proxy chain end to end, by hand.

## 8. Next
- TSMB investment, 1.50 USDC (Tier B), to complete the slot.
- Harvest review with live P/L screen.
- Positions numeric columns for TSMB/NVDAB wait on the Trades-October → Positions feed fix.
