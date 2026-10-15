# Trading

A model-independent trading research, knowledge, experimentation, and decision system.

## Core Principle

> The knowledge belongs to the project, not to the model.

Markdown is the durable knowledge layer.

Obsidian is the human-facing knowledge interface.

Git provides history and reversibility.

AI systems are interchangeable collaborators.

## Repository Structure

- AI/ - AI collaboration and handoff material
- MARKET/ - Market knowledge and observations
- RESEARCH/ - Research
- STRATEGIES/ - Trading and investment strategies
- WATCHLISTS/ - Active areas of interest
- THESIS/ - Investment and market theses
- RISK/ - Risk management
- PORTFOLIO/ - Portfolio structure and reviews
- TRADING/ - Trade planning and execution
- JOURNAL/ - Trading journal
- BACKTESTS/ - Backtesting
- EXPERIMENTS/ - Hypothesis-driven experiments
- DATA/ - Data
- EVIDENCE/ - Evidence supporting conclusions
- INSIGHTS/ - Durable insights and lessons
- DECISIONS/ - Important decisions and their reasoning
- SPECS/ - Specifications
- REFERENCES/ - External references
- CONVERSATIONS/ - AI conversation archive
- REPORTS/ - Periodic reports
- OPS/ - Operational tooling
- ARCHIVE/ - Historical material

## Harvest Calculator Tooling

The repository now includes a small cross-language harvest-calculation scaffold:

```text
src/
├── python/        # Python package + CLI
├── clojure/       # Clojure REPL/project
└── kotlin/        # Wear OS calculator scaffold
```

The Python and Clojure implementations share the same 50% harvest rule documented in the strategy decision. The Kotlin module provides a calculator-style Wear OS UI with:

- asset/currency selector,
- current-price input,
- position input,
- material-anchor input,
- calculation result,
- Binance Convert destination.

The Wear OS UI is deliberately a **pre-trade calculator**, not an execution client. It does not authenticate with Binance or place orders.

See `TRADING/harvest-cli.md` and `src/kotlin/README.md`.

## Crisis Harvest

The project has a formal crisis-harvest specification for anti-stagnation operation.

When the final-harvest-day condition activates, the candidate is selected at the **strategy-lot level** by the smallest **absolute USD/USDC-equivalent gap** to that lot's harvest threshold among lots that have not reached the threshold.

The crisis movement liberates **90% of the selected lot's material anchor**, leaving 10% of that anchor invested. It does not sell 90% of the aggregate wallet balance and does not merge strategy lots.

The actionable notification must identify the exact lot, calculate the native asset quantity for Binance's FROM field from the notification snapshot, and use the Binance-ready move format. If the available position at execution is smaller than the specified quantity, the remaining position is sold rather than canceling the crisis movement.

See SPECS/CRISIS_HARVEST_MECHANICS.md for the full mechanics and worked TAO example.

## Important Rule

Conversations are source material.

Extract durable knowledge from conversations rather than automatically treating conversations as the knowledge base.
