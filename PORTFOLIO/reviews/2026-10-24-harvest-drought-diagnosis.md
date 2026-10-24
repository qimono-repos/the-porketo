# Why so few assets were harvestable (2026-10-24)

Question (Albert, 24 Oct): after 3 days without action, only a few tickers were above the harvest threshold. Is it lack of diversity, the global market, or something else? And should we rotate an asset out to diversify?

Data used: the book's `Price Log` (56 price-worker runs, 8 Oct 03:00 to 24 Oct 03:06 Halifax), `Sprint` and `Crypto Sprint` lots against their anchors. No outside news was used, so this explains *what* moved, not *why* the market moved.

## 1. The short answer

The symptom is real, and **it is diversification, but not in the number of tickers**. We hold ~60 tickers, yet about 90% of the money sits in **one trade**: high-beta, risk-on growth (AI, quantum, growth stocks, alt-crypto). When that trade sells off, everything goes under its anchor at the same time. The only things above anchor today are the ones *outside* that trade.

## 2. Evidence

**Since 21 Oct (last harvest day), 43 of 47 tracked assets fell.** The 4 that rose:

| Asset | 3-day move | Distance from its 16-day high |
|---|---|---|
| DUK (utility) | +3.6% | −0.3% |
| CVX (energy) | +2.8% | at the high |
| AAPL (sold) | +1.1% | −0.1% |
| IBM (post-earnings) | +0.8% | −0.1% |

**Group behaviour, 6-hour returns, 8 to 24 Oct:**

| Group | Move since 8 Oct | Correlation with AI/semis |
|---|---|---|
| AI / semis (NVDA, AMD, TSM, MU, AVGO, ORCL, MDB) | −14.8% | 1.00 |
| Growth other (HOOD, TSLA, SpaceX, OKLO, Korea) | −14.4% | 0.94 |
| Quantum (IONQ, QBTS: the two with full history) | −23.9% | 0.74 |
| Crypto L1 / DeFi | −11.6% | 0.43 |
| Crypto gaming / meme | −20.1% | 0.38 |
| Crypto BTC / ZEC / TAO | −6.8% | 0.40 |
| **Defensive (CVX, DUK, IBM, AAPL, BLK)** | **+8.9%** | **−0.41** |

The crypto groups correlate 0.89 to 0.94 with **each other**, so 10 alt-coins behave like one coin.

**Your rotation thesis, tested:**
- *"When AI is bearish, money goes to quantum."* **Not in this window.** Quantum fell with AI (correlation 0.74) and fell harder. The newer quantum names fell 4 to 10% in the last 3 days too (PSQL −9.7%, XNDU −7.0%, INFQ −5.7%, QNTB −5.6%). Quantum trades as *leveraged AI*, not as a hedge.
- *"When stocks fall, gold rises."* We can't test it: we hold no gold. The defensive group (energy, utility, IBM) is the only sleeve with **negative** correlation to AI, and it is the only one that was harvestable.

## 3. Our exposure (material anchors, approximate)

| Sleeve | Anchor (USDC) | Share |
|---|---|---|
| AI / semis | ~100 | 17% |
| Quantum | ~103 | 18% |
| Growth other | ~81 | 14% |
| Crypto alts (L1, DeFi, AI, privacy) | ~103 | 18% |
| Crypto gaming / meme | ~88 | 15% |
| Crypto majors (BTC, ETH, SOL) | ~50 | 9% |
| **Defensive (CVX, DUK, IBM)** | **~52** | **9%** |

So only ~9% of the portfolio is in the sleeve that harvests when the risk trade sells off. And DUK, a third of that sleeve, is being sold for the DUKB migration.

## 4. Three reasons, in order of weight

1. **One-factor portfolio.** See above. It is the main cause.
2. **Entry timing.** Most stock lots were bought near the 8 to 13 Oct highs (NVDA 225, MU 1,056 to 1,088, AMD 646, TSM 457 to 477, IONQ 39 to 42, QBTS 16 to 17, OKLO 37 to 40). They are 10 to 35% underwater. No harvest is possible until each one recovers *above* its anchor, which can take weeks.
3. **Mechanics: small lots need big moves.** Under the ladder (amendment 2026-10-24), a harvest needs at least **0.60 USDC of excess** on the asset. Example:
   - one 2.25 lot needs **+27%** to get there on its own;
   - a 0.75 lot needs **+80%**.

   Catch-up batches create many small lots, so many of them will rarely harvest by themselves. That's fine, since they add up per asset, but it explains why "slow growers" rarely show up.

## 5. Catching candles (the BTC lesson)

Last week's BTC harvest worked because the candle was still there at a slot. BTC peaked at 84,700 (21 Oct 15:30) and is 80,657 now. With checks only every 6 hours, a candle that reverses within 6 hours is missed.

**Fix:** use Binance **Convert → Limit** (visible on every Convert screen) as a standing harvest order. For each asset close to threshold, place a limit sell at the price where the excess reaches the next ladder step. Size it to that step (e.g. 0.30 or 0.45 USDT). The order catches the candle while nobody is looking. This keeps the 50% rule intact, because the limit price is computed from the rule.

## 6. Recommendations

**Now (this weekend):**
- **Harvest candidates (check the live price first):**
  - **CVX** (Lemon): excess ≈ 0.90, so the 0.45 step fits.
  - **IBMB**, counting all 3 lots: excess ≈ 0.80 at 250, so the 0.30 step fits.
- **Remaining 15 units (11.25 USDC):** tilt them toward the uncorrelated sleeve with assets we already hold:
  - IBMB;
  - DUKB on Monday, as part of the migration;
  - optionally CVX on Lemon.
  - Keep a small share for one AI name at a deep dip (AMDB −20% from its high, MUB −19%), so the AI exposure is not abandoned.
- **DUK:** keep the migration. The point is to *keep* utility exposure in a harvest-friendly wrapper (DUKB, 24/7, no fee), not to leave it. Buy DUKB the same day the sale fills.

**Next (November budget):**
- **Target sleeves:** defensive / real assets ~20% (from 9%), AI + quantum core ~35%, crypto ~35%, growth other ~10%. This does not mean selling AI. It means pointing new units at the thin sleeve.
- **One in, one out (needs Albert's approval, because it breaks "no new players"):**
  - **In:** tokenized gold, e.g. PAXG on Binance Convert (24/7, no fee). It is the cleanest version of the "stocks down, gold up" hedge, and it would be harvestable on the days everything else isn't.
  - **Out candidate:** the gaming / meme cluster: 15% of the money, 6 tokens that move as one, and the worst group (−20%). The cheapest exit is to **stop feeding it** (no new units), not to sell below anchor. If one must go, PUMP (meme, −44% vs anchor) has the weakest thesis.
- **Quantum:** keep it as a conviction sleeve, but stop counting it as diversification away from AI.

## 7. Open questions for Albert

1. Approve one new player for diversification (gold), or stay with held assets only?
2. Stop new units into the gaming / meme cluster?
3. Set up Convert Limit harvest orders on the 5 to 6 assets closest to threshold?
