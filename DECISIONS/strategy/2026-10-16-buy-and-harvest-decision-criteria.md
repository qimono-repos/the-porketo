# Buy and Harvest Decision Criteria

**Status:** canonical, written 2026-10-16 at operator request. Binds every teammate (all LLMs and the operator).
**Why this exists:** on 2026-10-16 an agent measured an NVDAB "dip" against the lot anchor instead of the 2-month swing high, understating it (~3% vs ~7.4%). The two decisions use DIFFERENT references. This file says which one to look at for each. See INSIGHTS/mistakes/2026-10-16-nvdab-wrong-dip-yardstick.md.

## The one rule to remember

| Decision | Look at | Never use for this |
|---|---|---|
| BUY / INVEST (where to put a slot) | Market: swing high over last 2 months + news | The lot anchor |
| SELL / HARVEST (what to take out) | The lot: material anchor vs live price | The swing high or news narrative |

Buying asks "how far has the MARKET fallen and why?" Harvesting asks "is MY LOT above what I paid?"

## 0. Operating rule vs research direction

`INSIGHTS/Claude-Code-Team-Meeting-Insights.md` (2026-10-14) says there is "no fixed harvest rule by design" and proposes information/confidence-driven or Fourier-based triggers. That is the **research direction**, not the operating rule.

- **Operating rule (in force now):** the criteria in this file, including the 50% anchor-based harvest.
- **Research direction:** information- or Fourier-driven triggers may replace the anchor rule **only after** passing an out-of-sample, fee-inclusive backtest recorded in the repo and approved by the operator.

If any other file appears to contradict this one, this file wins until it is explicitly amended.

## 1. BUY / INVEST criteria

**Eligible universe:** assets already held (no new players since 2026-10-11), except urgent outside-crisis news.

**Score (weights):**
- Dip, 40%: (2-month swing high − live price) / swing high. Swing high = highest price in the last ~2 months, read from the live chart (e.g. Binance Convert 1W/1M view).
- Upside, 20%: analyst targets and upcoming catalysts (earnings, governance votes, buybacks).
- Volatility / beta, 10%: does it move the needle week to week.
- Momentum, 5%: last ~2 months, trend line through points 2 weeks apart.
- News research, 25%: latest meaningful news for the asset and its sector.

**Both price and news are always checked together.** Dip without news is incomplete; news without the dip number is incomplete.

**Tiering (3 units per slot, 1 unit = 0.75 USDC):**
- Team A = 3 units: high conviction (e.g. near catalyst) AND low survival risk.
- Team B = 2 units. Team C = 1 unit.
- A slot = one A, or one B + one C, or three Cs.
- Assets that could break or be hacked are capped lower even if interesting.

**Timing rules:** buy before catalysts; if the event causes a pullback, add more. Budget is finite: an asset entering the week's list pushes another out.

**Sources:** live prices from the venue (Binance/Lemon) or CoinMarketCap/Yahoo, timestamped; never the book's stale snapshot.

## 2. SELL / HARVEST criteria

**Reference:** each strategy lot's material anchor (amount actually materialised at buy). Lots are never blended.

**Trigger:** lot value (units × live price) above anchor.

**Size (50% rule):** H = (U × P − A) / (2P), rounded down to venue precision.

**Which lot:** highest active rung per market swing; lower rungs deferred.

**Hard stops:**
- A lot at or below its anchor is NOT harvested (buying more is allowed).
- A harvest that leaves a lot below anchor blocks further harvest until it is back above.
- Harvests settle into USDT.

**Forced/crisis harvest:** smallest dollar gap below threshold; forced = 50% of anchor, crisis = 90%.

**Sources:** live venue quote at execution; the receipt is execution truth.

## 3. Quick checklist before any move

1. Am I buying or harvesting? Pick the matching reference from the table above.
2. Buy: swing high read from a live chart, timestamped? News checked?
3. Harvest: lot anchor read from the book, live price timestamped, lot above anchor?
4. Record tier (buys) or lot + formula (harvests) in the booking note.
