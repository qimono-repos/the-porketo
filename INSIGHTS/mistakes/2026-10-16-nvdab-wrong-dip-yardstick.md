# Mistake: NVDAB dip measured against the lot anchor

**Date:** 2026-10-16, ~07:00 ART. **Agent:** Claude. **Impact:** recommendation only; nothing booked wrong.

## What happened
Asked whether to put a slot into NVDAB, Claude measured the dip against the lot's buy price (anchor 224.587) and called it ~3%, recommending skip. The operator's live Binance view showed 217.653 vs a 9 Oct swing high of 235.059: a ~7.4% dip. Recommendation revised to Tier C, one unit.

## Root cause
The buy-side and harvest-side references were never written in one place. The agent reused the harvest yardstick (anchor) for a buy decision.

## Fix
- `DECISIONS/strategy/2026-10-16-buy-and-harvest-decision-criteria.md` created as single source of truth.
- Mandatory-read block added at the top of the repo README.

## Lesson
Buy = market (swing high + news). Harvest = lot (anchor). Ask "which decision am I making?" before picking a number.
