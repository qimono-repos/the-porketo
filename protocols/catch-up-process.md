# Catch-up process (checkpoint slots)

Adopted: 2026-10-24. Use this at **every** checkpoint, whoever runs it: Albert, ChatGPT, Claude or any other agent.

## The 5 steps

1. **Time.** Write down the current Halifax time (GMT-3) and the current slot #. The book shows both: `Slots!B13` and `Slots!B14`.
2. **Latest move.** Look at the last rows of `Trades-October`, `Crypto Trades` and `Trades`, and at `Slots!B19` (the last slot with an investment logged). If a real fill is missing from the book, book it first. The wallet is the truth. If the book and the wallet disagree, stop and reconcile before investing.
3. **Harvest first.** Run [`harvest-ladder.md`](harvest-ladder.md) on the book's **`Prices` tab**. The price worker (`apps-script/`) refreshes it at 03:00, 09:00, 15:00 and 21:00 Halifax, one hour before each slot. `✅ FRESH` (under 13 h) is good enough; `⏳ OUTDATED` means check the live venue price first. Use each lot's **current units** (after earlier harvests), check every lot of the asset, and add their excess together. Never harvest more than 50% of the excess (ladder amendment 2026-10-24). Every lot is either harvested or noted "no step fits".
4. **Invest.** Read the status on `Dashboard!A18` (same as `Slots!B17`):
   - `UP TO DATE`: invest this slot's 3 units (2.25 USDC).
   - `CATCH UP · N units`: invest N units, in **one batch** if that's practical (precedent: the 19 Oct batch, 65 units). Fill it by tier ([`three-units-per-slot-fibonacci-tiers.md`](../DECISIONS/strategy/three-units-per-slot-fibonacci-tiers.md)) and the buy criteria ([`2026-10-16-buy-and-harvest-decision-criteria.md`](../DECISIONS/strategy/2026-10-16-buy-and-harvest-decision-criteria.md)).
   - `AHEAD · WAIT`: do not invest. Follow [`ahead-wait-process.md`](ahead-wait-process.md).
5. **Log the slot.** Book each fill in its trade tab, with the slot # in the trade row's slot column. Then in `Slots`, on the row of the slot window the money was spent in, type the USDC paid (fee included) in column F, the event IDs in G and the harvest result in H. The status updates by itself.

## Rules

- The price worker refreshes at 03:00, 09:00, 15:00 and 21:00 Halifax, one hour before each slot (04, 10, 16, 22). So at every slot, the Prices tab is at most an hour old. Details: [`apps-script/README.md`](../apps-script/README.md).
- A slot is 3 units of 0.75 = 2.25 USDC. Missed slots carry forward. They are never forgiven silently.
- Slot N's window runs from its time until the next slot (04:00, 10:00, 16:00, 22:00 Halifax).
- The full amount paid, including the fee, counts against the slots.
- Only real fills count. A plan, a calendar event or a note is not proof.
- Don't recompute history from notes. The `Slots` tab is the single place where slot status is derived.

## How many turns does a catch-up take?

A "turn" is one working pass with an AI. A typical catch-up needs:

- 1 turn to check the latest move against the wallet (step 2),
- 1 turn to harvest and invest the batch (steps 3 and 4),
- then 1 turn per slot to stay on the cadence.

## Precedent

2026-10-24: the book claimed slots were covered through CP62, but its rows only covered up to part of CP58. Binance USDC (unchanged since 20 Oct) proved there were no unbooked buys. Root cause: slot coverage lived only in free-text notes. Fix: the `Slots` tab and this process. Report: `/mnt/project-files/reconciliation/2026-10-24-checkpoint-reconciliation.md` (project files).
