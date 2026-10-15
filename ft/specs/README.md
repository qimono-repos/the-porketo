# FT — Agile Project Charter

This folder specifies the **ft** sub-project as a small agile effort. The point
is not ceremony; it is to make the work reproducible: we write a spec, build the
smallest slice that satisfies it, verify it with a test, then write the next
spec. Specs and code advance together — spec → feature → spec → feature —
until the project is done.

## Vision

> Given a synthetic hourly price series for a set of assets, produce a
> short-horizon price forecast using a Fourier (frequency-domain) model, and
> score that forecast honestly on a held-out window.

Success = a reader can clone the repo, run one command, and see forecasts plus
error metrics for `AAPL`, `IBM`, `BTC-USD`, and `SOL-USD`.

## Personas

- **Operator / Researcher** — runs the forecast, reads the report.
- **Contributor** — adds features; must keep `clojure -M:test` green.
- **AI collaborator** — see `../agents/`; works from the backlog and specs.

## Iteration model

Each iteration is a time-boxed slice with:

- a **goal** (one sentence),
- **user stories** ("As a …, I want …, so that …"),
- **acceptance criteria** (Given/When/Then),
- **tasks**, and
- a **review** recording what actually shipped and what changed.

We iterate: a story that turns out underspecified is refined *in the next
spec*, not silently re-scoped in code. Deviations are recorded in the
iteration's review section (this mirrors the parent repo's governance habit of
preserving expected-vs-actual reasoning).

## Definition of Ready (DoR)

A story may enter an iteration only when it has acceptance criteria and a
verification method (a test or a command with an observable output).

## Definition of Done (DoD)

A story is done when:

1. acceptance criteria are met;
2. `clojure -M:test` passes;
3. `clojure -M:run` produces a forecast for every symbol without error;
4. the relevant doc in `../docs/` is updated if the interface changed.

## Ceremonies (lightweight)

- **Refinement** — before an iteration, write/refresh the spec file.
- **Daily** — not used (solo/asynchronous project).
- **Review** — at the end, fill the iteration's Review section.
- **Retrospective** — captured as "What changed" + "Backlog impact".

## Artefacts in this folder

| File | Purpose |
|---|---|
| `BACKLOG.md` | Ordered list of epics and user stories with status |
| `iterations/iteration-0N-*.md` | Per-iteration spec + review |
| `TRACEABILITY.md` | Story → code → test mapping |

## Shared definition of "data"

The dataset in `../../samples/trading_data.csv` is **synthetic** and is the
only input. No network, no real market data, no order placement.
