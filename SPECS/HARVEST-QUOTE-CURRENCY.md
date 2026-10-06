# Harvest Quote Currency

**Status:** Active rule, binding from 2026-10-06 (Halifax).
**Applies to:** all teammates — Claude, ChatGPT, Gemini, any other model, and the human operator.

## Rule

- **BUY deployments are funded from USDC.** A buy debits the USDC deployable balance.
- **HARVEST executions convert the harvested proceeds into USDT**, not USDC. A harvest credits USDT.

So the two directions use different quote currencies:

| Direction | Spends | Receives |
|---|---|---|
| BUY | USDC | the asset |
| HARVEST | the asset | USDT |

## Why

This separates deployable capital (held in USDC) from harvested proceeds (accumulated in USDT), so harvested cash is naturally distinguishable from spendable buy capital at the wallet level, not only in the book.

## Effect on bookkeeping

- Preserve each side's native wallet flow: a BUY records a USDC wallet outflow; a HARVEST records a USDT wallet inflow.
- Immutable strategy-lot material anchors are still preserved on harvest, exactly as before. Only executed units change.
- Keep separate lots separate.
- This overrides any earlier assumption that harvests settle back into USDC.
