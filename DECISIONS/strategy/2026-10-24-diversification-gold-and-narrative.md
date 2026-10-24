# Diversification: gold in, narrative input, candle alerts (2026-10-24)

**Status:** decided by Albert, 2026-10-24 (thread "harvest drought"). Background: [`PORTFOLIO/reviews/2026-10-24-harvest-drought-diagnosis.md`](../../PORTFOLIO/reviews/2026-10-24-harvest-drought-diagnosis.md).

## Why

On 24 Oct only a few assets were above their harvest threshold. The review found the portfolio is mostly one trade: high-risk growth (AI, quantum, growth stocks, alt-crypto). Only the defensive sleeve (CVX, DUK, IBM, about 9% of the money) moved against it, and it was the only one that harvested.

## Decisions

1. **PAX Gold (PAXG) enters** as a new player: the exception to "no new players since 2026-10-11". Tokenised gold on Binance Convert (24/7, no fee). Role: the hedge that rises when stocks fall, so something is harvestable on bad days.
2. **One asset goes out** to make room. Not quantum, not gaming (see below). The choice is pending Albert's pick. "Out" means **no new units**. It is sold only when it is back at or above its anchor, so no loss is locked in.
3. **Quantum stays.** Albert's view: when the quantum sector is down, the rest of the portfolio should back it up. Note from the review: quantum moved with AI in Oct (correlation 0.74), so it is a conviction sleeve, not a hedge.
4. **Gaming stays and grows, starting with GALA**, widening to other gaming ecosystems (not only Axie / Ronin / Immutable).
5. **Candles are the "gold mine".** Two changes:
   - **Alerts:** [`apps-script/candle-alert.gs`](../../apps-script/candle-alert.gs) checks every hour. It emails when a ladder step fits, or when a price moves 4% or more in an hour.
   - **Cadence:** more checkpoints per day from November. Proposal: [`2026-10-24-november-six-checkpoints-proposal.md`](2026-10-24-november-six-checkpoints-proposal.md).
   - Binance Convert *Limit* orders are allowed, but Albert prefers not to rely on them.
6. **Narrative input for long-term crypto:**
   - **Sources:** Crypto Banter (Ran Neuner) and the Paul Barron Network, on YouTube, X and forums.
   - **Weight:** added to the buy score (see [`2026-10-16-buy-and-harvest-decision-criteria.md`](2026-10-16-buy-and-harvest-decision-criteria.md), section 1).
   - **YouTube:** titles and descriptions are pulled daily into the book's `Narrative` tab by [`apps-script/narrative-feed.gs`](../../apps-script/narrative-feed.gs).
   - **X and forums:** checked by hand.

## Target sleeves (direction for November money, not a sell order)

| Sleeve | Now (approx.) | Target |
|---|---|---|
| Defensive / real assets (CVX, DUK→DUKB, IBM, PAXG) | 9% | ~20% |
| AI + quantum | 35% | ~35% |
| Crypto (majors, alts, gaming) | 42% | ~35% |
| Growth other | 14% | ~10% |
