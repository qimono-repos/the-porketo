# Nightly Movements · 2026-09-30

## Event

The planned $20 technology diversification deployment was executed as two separate purchases:

| Event ID | Executed Instrument | Underlying Exposure | Action | USDC | Rate | Units | Fee |
|---|---|---|---|---:|---:|---:|---:|
| TRD-0024 | TSLAB | Tesla | BUY | 15.00 | 354.992 | 0.04225446 | 0 TSLAB |
| TRD-0025 | SPCXB | SpaceX | BUY | 5.00 | 149.538 | 0.03343623 | 0 SPCXB |

**Total deployed:** 20.00 USDC  
**Total displayed transaction fees:** 0  
**Status:** executed and confirmed

## Decision Link

This execution implements the 2026-09-30 allocation decision:

- TSLA/Tesla: $15
- SPCX/SpaceX: $5

The decision intentionally used a 75/25 split, with Tesla as the higher-sensitivity/catalyst leg and SpaceX retained as the diversification leg.

## Execution Evidence

The operator supplied Binance successful-purchase confirmations for both movements.

For TSLAB, the confirmation shows 15 USDC converted into 0.04225446 TSLAB at 354.992 USDC per TSLAB, with 0 TSLAB transaction fees.

For SPCXB, the supplied confirmation shows 5 USDC converted into 0.03343623 SPCXB at 149.538 USDC per SPCXB, with 0 SPCXB transaction fees.

The exact execution timestamps were not available in the supplied confirmations and therefore are intentionally not invented.

## Deviation / Disposition

**Deviation:** the planned decision used the underlying exposure labels TSLA and SPCX, while the execution confirmations identify the Binance instruments as TSLAB and SPCXB.

**Disposition:** Accepted as an instrument-label distinction. The execution records preserve the exact broker instrument identifiers; the decision and thesis preserve the underlying company exposure.

No quantity or cash-amount deviation occurred:

- planned TSLA/Tesla amount: $15 → executed $15
- planned SPCX/SpaceX amount: $5 → executed $5
- planned total: $20 → executed $20

## Durable Reasoning

The execution preserves the original experiment structure:

**business diversification + deliberate TSLA tactical tilt + small position size.**

The journal records the reasoning, while the individual TRD records and broker confirmations remain the execution source of truth.

## Next Review

**2026-10-02**

Review Tesla after the Q3 delivery release:

1. compare the reported delivery result with the pre-event consensus used in the decision;
2. observe the initial market reaction;
3. evaluate whether the original catalyst thesis was strengthened, weakened, or unchanged;
4. do not retroactively rewrite this decision based on the result.

## Related Records

- [Decision](../../DECISIONS/investment/2026-09-30-tsla-spcx-allocation.md)
- [Trade plan](../../TRADING/trade-plans/2026-09-30-tsla-spcx.md)
- [TRD-0024](../../TRADING/entries/TRD-0024.md)
- [TRD-0025](../../TRADING/entries/TRD-0025.md)
- [Trading CSV log](../../EVIDENCE/trades/trading-log.csv)
