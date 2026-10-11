# Decision: Three Units Per Slot — Fibonacci Tier Deployment

- **Date:** 2026-10-11
- **Status:** Active standing rule
- **Scope:** Every investment checkpoint/slot from Checkpoint 20 (2026-10-11 10:00 Halifax) through Event 98 (2026-10-30 22:00 Halifax), across the whole unified squad (crypto + tokenised stocks).

## Decision

**Every slot deploys exactly 3 Fibonacci units = 2.25 USDC. No slot is left partly undeployed.**

One unit = 0.75 USDC. The 3 units can be split across tiers however the conviction falls:

- **One Team A player** = 3 units = 2.25 USDC, or
- **One Team B player + one Team C player** = 2 units + 1 unit = 2.25 USDC, or
- **Three Team C players** = 1 + 1 + 1 = 2.25 USDC.

Any combination is allowed as long as the units in the slot **sum to 3**.

## Why — the full-deployment problem

The budget was roughly doubled to ~200 USDC (CRF-0005, 2026-10-11) to fund the remaining slots to Event 98. With 79 slots left, a flat ceiling of 2.25 per slot totals 177.75, which fits.

But if some slots only spent 1 unit (0.75) or 2 units (1.50), the shortfall against the ceiling would accumulate as **uninvested capital**, which the experiment counts as lost money. The fix is to require a fixed 3-unit deployment every slot and let the **tier split**, not the total, express conviction.

This is not a general property of Fibonacci; it is simply that **3 = 2 + 1**. So the only multi-pick split that exactly fills a slot without a Team A pick is one B + one C (or three Cs). One B alone (1.50) or one C alone (0.75) underfills and is not allowed on its own.

## Tier → units → capital

| Tier | Units | USDC |
|---|---:|---:|
| Team A | 3 | 2.25 |
| Team B | 2 | 1.50 |
| Team C | 1 | 0.75 |

## Tier criterion — conviction AND survival risk

Tier is not upside alone. A player earns **Team A** only with **both**:

1. **High conviction** (e.g. a near catalyst, a dip below our cost), and
2. **Low survival risk** — low probability the player ceases to exist within the next ~6 months.

The two risks are distinct:

- **Price risk:** the asset swings. All players have it.
- **Survival risk:** the player goes to zero or near-zero — a company breaks, or a protocol is hacked / drained / broken.

**Worked contrast (2026-10-11):**

- **TSMB (Taiwan Semiconductor, tokenised):** high price risk but very low survival risk — a systemically important company, not expected to fail within six months barring a worldwide shock. With Q3 earnings on 15 Oct (revenue already reported as a beat) and trading below our cost, it qualifies as **Team A**.
- **ALGO (Algorand):** interesting, but carries **both** price risk and meaningful **survival risk** (a protocol can be hacked or broken in a way a company of TSMC's scale effectively cannot). That extra survival risk **caps** how high ALGO should ever be tiered, even when it's a reasonable buy.

This protects the capital-levelling intent: the most capital goes to the players least likely to disappear.

## Expansion rule unchanged

This rule governs **how much** and **which tier**, not **what**. The no-new-players rule still holds: deploy into existing squad members only, unless urgent outside-the-experiment news forces a crisis move (e.g. a company breaks or a crypto is severely hacked).

## Recording

Each slot's tier is recorded **at the moment of the slot** in the **Tier column** (column N) of the `Crypto Sprint` tab (and the equivalent on `Sprint`). The tier is a property of the decision at that slot, not a permanent label on the player.

## Caveats

- Leaves ~22 USDC of cushion over the 79-slot run for penalties and venue minimums (e.g. Binance Stocks ~5.29 USD floor). If a slot needs a larger minimum, that is a practical exception to note, not a silent overspend.
- Tiers can change slot to slot as conviction and evidence change.

## Precedence

Active standing rule. A later dated decision may revise or supersede it. Historical bookings remain immutable.
