# Ahead / wait process (the opposite of catch-up)

Adopted: 2026-10-24.

Sometimes we invest **more** than the slots due so far, for example to clear a Binance Stocks minimum order (~5.17 USDC) or because of a conviction buy. Then the book is **ahead**.

## Rule

When `Dashboard!A18` (or `Slots!B17`) says `AHEAD · N units prepaid · WAIT: skip the next K slot(s)`:

1. **Do not invest** at the next K slots. They are already paid.
2. **Still harvest.** Harvesting runs at every slot, whatever the investment status ([`harvest-ladder.md`](harvest-ladder.md)).
3. At each skipped slot, write `prepaid` in the `Slots` notes column (I). That leaves a trace that the slot was checked, not forgotten.
4. Resume normal investing when the status says `UP TO DATE` or `CATCH UP`.

## Why

Overspending now means less to invest later. Waiting keeps the total investment on the budget line (3 units per slot × slots in the exercise) and avoids running out of budget before the month ends.

## Exceptions

An urgent crisis move (a held company breaks, a crypto is hacked) may break the wait. Record it as a deviation in `JOURNAL/` with expected, actual and difference.
