# Decision: Execution Precedence over Book Order

- **Date:** 2026-10-09
- **Status:** Active standing rule
- **Scope:** All checkpoint investments and harvests, and every strategy-lot tab in the Trading book — in particular `Crypto Sprint` (and, by the same logic, `Sprint`).

## Decision

**Execution takes precedence over bookkeeping.**

In this micro-investment system, acting on the real-time movement at checkpoint time is what makes the system work. When a checkpoint arrives and no computer is at hand, the operator makes the move by hand on the exchange and completes the book afterwards.

As a direct consequence:

> **Row order in the `Crypto Sprint` tab carries no meaning. Completeness does.**

Rows are appended in the order they were *booked*, not the order they were *executed*. A row sitting above or below another says nothing about which trade came first.

## Date

2026-10-09 (Halifax). Stated by the operator during the Epic-column / calendar-linking session.

## Context

- The experiment runs on a fixed cadence: one investment checkpoint every 6 hours (04:00 / 10:00 / 16:00 / 22:00 Halifax), 98 checkpoints from 2026-10-06 to 2026-10-30, each with a 0.75 USDC deployment obligation.
- The value of the method comes from *keeping the pace*: buying at the checkpoint, whatever the price is doing.
- The operator is not always at a computer when a checkpoint fires. A phone and the Binance app are enough to execute; they are not a comfortable place to do the books.
- The `Crypto Sprint` tab is an append-only cockpit: one row per strategy lot, no totalizers, no derived signal column (removed 2026-10-09). Each lot's `Epic` cell links to the calendar event of the checkpoint it belongs to.

## Worked Example: ETH above SLP

| Row order in `Crypto Sprint` | Lot | Checkpoint | How it happened |
|---|---|---|---|
| upper | **ETH @ 2710.17** (CRT-0046) | Checkpoint 2 of 98 — Tue 06 Oct 22:00 | Executed **live**, together with an LLM, and booked at the moment of the trade. |
| lower | **SLP @ 0.000689617** (CRT-0045) | Checkpoint 1 of 98 — Tue 06 Oct 16:00 | Executed **by hand**, away from a computer, at checkpoint time. Booked **retroactively** afterwards. |

SLP's checkpoint came first, yet ETH sits above it. That is not a mistake: it is the visible trace of the operator choosing to execute on time and book later.

**How a future reader (human or model) should read this:** out-of-order rows reflect *how trades were executed and booked*, not an error to be "fixed". Do not reorder rows to make them chronological, and do not infer sequence from row position.

## Alternatives Considered

1. **Skip or delay the checkpoint until a computer is available**, so the book is always written in execution order. Rejected: missing the cadence breaks the method itself (and creates backlog / penalty pressure).
2. **Keep rows sorted chronologically**, re-inserting retroactive bookings in the right place. Rejected: fragile, invites accidental edits to existing rows, and adds no information that the event data doesn't already carry.
3. **Execute on time, book afterwards, ignore row order (chosen).**

## Reasoning

- Micro-investing works through regularity. A missed checkpoint costs more than an out-of-order row.
- Ordering is a *query* concern, not a *storage* concern. The book stores events; any view that needs chronology sorts by the event's own data.
- This matches the project's direction towards an event-driven store (see [[the-porketo]] — Datomic book of record first), where facts are append-only and order comes from time attributes, never from physical position.

## Where Chronology Lives

Whenever sequence matters, derive it from the data, in this order of authority:

1. The **exchange receipt** timestamp (execution truth).
2. The **event log** (`Crypto Trades` / `Trades-October`): Event ID and `Executed At`.
3. The lot's **`Epic`** link to its checkpoint calendar event.
4. Never the row number in `Crypto Sprint` / `Sprint`.

## Evidence

- `Crypto Trades` CRT-0045 (SLP, Checkpoint 1) and CRT-0046 (ETH, Checkpoint 2).
- `Crypto Sprint` row positions as of 2026-10-09 (ETH above SLP).
- Operator's account of the two executions, 2026-10-09.

## Risks

- **Late booking can be forgotten.** A hand-executed trade that is never booked leaves the book incomplete. Mitigation: track unbooked executions (pending-bookings list) and reconcile against the exchange wallet/receipts.
- **Reader confusion.** Someone may "tidy" the rows into chronological order. Mitigation: this decision record, plus a short note on the retroactively booked row.
- **Details lost from memory.** A trade booked hours later may miss exact timestamps. Mitigation: the exchange receipt remains execution truth; record what is known and mark what isn't.

## Expected Consequences

- Checkpoints keep their cadence even when the operator is away from a computer.
- `Crypto Sprint` stays a simple append-only list; completeness is the quality bar.
- Any analysis that needs order sorts by timestamp / checkpoint, never by row.

## Reversal Conditions

Revisit if the book moves to a store or view where row position is automatically derived from execution time (then the question disappears), or if late bookings start causing real reconciliation gaps that outweigh the benefit of keeping pace.

## Outcome

Pending — to be reviewed at the end of the October sprint (2026-10-30).

## Review Date

2026-10-30

## Precedence

This is an active standing rule. A later dated decision may revise or supersede it. Historical bookings remain immutable.
