# Projection by Event 98 — Third Draft: The Three-Team Model

**Status:** Conceptual planning draft. This is a proposed operating model, not an execution record or a final allocation schedule.

**Planning horizon:** Event 98 / Checkpoint 98, Friday, October 30, 2026, 22:00 Halifax time.

## 1. Purpose

Evolve the $100 Trading Ticket into a dynamic 35-player squad. Each underlying asset is one player, whether exposure is held as crypto or as a tokenized stock. The model assigns players to three teams with different invested-capital targets and different allocations of analytical attention.

The Ted Lasso analogy is intentional: this is one squad with three tiers of priority, not three independent portfolios. Players can move between teams as new evidence arrives.

## 2. The 35-player roster and fixed team sizes

The planning roster contains 35 players. Team sizes remain fixed:

| Team | Number of players | Invested-capital target per player | Team target at full allocation |
|---|---:|---:|---:|
| Team A | 10 | $20 | $200 |
| Team B | 10 | $10 | $100 |
| Team C | 15 | $5 | $75 |
| **Total** | **35** | — | **$375** |

These are target levels for the conceptual model. They are not a claim that every player currently has that amount invested, nor are they a statement of current market value. The team targets total $375 when all 35 players are at their respective target levels.

Team membership is not permanently assigned today. The roster is observed over time and players are dynamically classified based on the available short-, medium-, and long-term information.

## 3. What each team means

### Team A — Core priority

- **Target:** approximately $20 invested capital per player.
- **Roster size:** 10 players.
- **Analytical attention:** highest.
- **Purpose:** give the strongest current candidates the largest allocation of capital and the deepest discussion.
- **Example:** SOL could be considered as a Team A player in an illustrative review. This is an example, not a pre-approved permanent classification.

### Team B — Intermediate priority

- **Target:** approximately $10 invested capital per player.
- **Roster size:** 10 players.
- **Analytical attention:** intermediate.
- **Purpose:** maintain meaningful exposure and analysis for players that warrant attention but are not currently in the highest-priority tier.
- **Example:** IBM could be reviewed as a Team B player in an illustrative meeting. This is not a permanent assignment.

### Team C — Exploratory / lower priority

- **Target:** approximately $5 invested capital per player.
- **Roster size:** 15 players.
- **Analytical attention:** lowest of the three teams, while still receiving a defined review.
- **Purpose:** keep emerging, less-proven, or lower-priority candidates in the squad without giving each the same capital and analytical resources as Team A.
- **Example:** ALGO could be reviewed as a Team C player in an illustrative meeting. This is not a permanent assignment.

The three targets are distinct tiers. There is no universal $10 minimum in this model: Team A targets $20, Team B targets $10, and Team C targets $5.

## 4. Dynamic promotion and demotion

Team assignment changes as information changes. Short-term performance is the preferred primary trigger for a move up or down; medium- and long-term information also informs the assessment. This draft does not impose rigid numerical performance thresholds or a formula for weighting time horizons.

Moves can be direct between any tiers. A player may move from Team C directly to Team A, or from Team A directly to Team C, when the evidence supports that decision. Passing through Team B is not mandatory.

### Fixed capacity rule

Team sizes cannot expand or contract. If a promotion enters a full destination team, the lowest-performing player in that receiving team is demoted to create room. The same fixed-capacity principle applies whenever a destination team is full.

For example, if a Team B player is promoted to Team A and all 10 Team A places are occupied, the lowest-performing Team A player must leave Team A to make room. That displaced player is assessed for the appropriate lower team. If a move requires a chain of changes across full teams, the model must preserve the fixed 10 / 10 / 15 roster sizes.

This rule is about classification and capacity, not a guarantee that any player will be promoted or demoted on a particular date.

## 5. Reclassification changes capital allocation

A team change is not merely a label change. It also changes the player's target allocation of invested capital.

- Moving from Team A to Team B changes the target from approximately $20 to $10, conceptually releasing about $10 of target allocation.
- Moving from Team B to Team A changes the target from approximately $10 to $20, conceptually requiring about $10 of additional target allocation.
- Moving from Team C to Team A changes the target from approximately $5 to $20, a target difference of about $15.
- Moving from Team A to Team C changes the target from approximately $20 to $5, a target difference of about $15.

These are differences between target allocations, not predictions of exact sale proceeds. Actual sale proceeds can differ because market prices, fees, spreads, and execution conditions vary. Any real trade must be supported by its actual broker or exchange receipt and recorded through the project's canonical event-log workflow. The conceptual model must never be treated as proof that a trade occurred.

For the thought experiment, assume the funds required by the model are available. The aim here is to define the allocation logic, not to repeatedly reopen the funding premise.

## 6. Analytical attention follows team priority

The teams control both capital targets and the share of limited research and discussion resources allocated to each player. More attention means more room to investigate evidence, compare arguments, and discuss risks. It does **not** automatically mean that an investment must be made.

The agreed illustrative attention ratio is **Team A : Team B : Team C = 4 : 2 : 1**, matching the relative capital targets of $20 : $10 : $5.

### Example: a meeting with a limited LLM-token budget

Suppose one review call has these three players on the agenda:

| Example player | Illustrative team | Capital target | Token budget | Intended depth |
|---|---|---:|---:|---|
| SOL | Team A | $20 | 2,000 tokens | Deepest review |
| IBM | Team B | $10 | 1,000 tokens | Intermediate review |
| ALGO | Team C | $5 | 500 tokens | Concise review |

The total example budget is 3,500 tokens, split 4:2:1. These budgets are ceilings for the exercise, not mandatory word counts. Each brief should use its allocation to examine relevant evidence and risks, rather than padding the answer to consume every token.

The review can use different sources according to the asset: for SOL, blockchain/network data, crypto-market research, regulatory developments, and relevant company or ecosystem announcements; for IBM, official financial results, filings, competitive developments, and independent business reporting; for ALGO, network/project documentation, ecosystem activity, governance, market data, and credible independent reporting.

The examples SOL / IBM / ALGO illustrate how the process works. They do not establish their permanent team memberships.

## 7. Information and classification process

At a review checkpoint:

1. Gather available short-term performance and news for the roster.
2. Add medium- and long-term context where relevant.
3. Assess whether any players merit promotion or demotion. Short-term performance is the preferred primary trigger, informed by the broader context.
4. Apply the fixed-capacity rule if the destination team is full.
5. Update the team classifications and their target capital allocations.
6. Estimate the resulting capital reallocation at target level.
7. Assign analytical attention using the 4:2:1 ratio.
8. Keep proposed allocations distinct from executed trades and verified balances.

This draft does not yet define a numerical scoring formula, hard promotion thresholds, a fixed review frequency, or a permanent assignment of each of the 35 players. Those details should not be invented before the project explicitly adopts them.

## 8. Relationship to earlier drafts

Draft 1 established the Event 98 projection and expanded the conceptual roster to 35 underlying-asset players by consolidating exposures to the same underlying asset.

Draft 2 explored a single approximately $10 invested-capital target for all 35 players. Draft 3 supersedes that single-floor approach with three tier-specific targets: $20 for Team A, $10 for Team B, and $5 for Team C, with fixed team sizes of 10, 10, and 15.

The prior Event 98 checkpoint remains the planning horizon. This third draft defines the conceptual team and attention rules; it does not assert that the final allocations or team memberships have already been calculated or executed.

## 9. Verification and execution discipline

This is a planning model. Keep the project's evidence hierarchy intact:

**REAL EXECUTION → SOURCE EVENT LOG → DERIVED POSITION → STRATEGY LOT → DASHBOARD**

- An actual broker or exchange receipt is the source of truth for an execution.
- Never invent fills, prices, timestamps, or market data.
- Distinguish verified execution data from workbook values, calculations, assumptions, and analysis.
- Treat the Binance lots supplied for this conceptual exercise as accepted model inputs without claiming that each movement has been independently reconciled.
- If this model is later implemented in the workbook, verify formulas and ranges after structural changes. Read the Dashboard last because it is derived from upstream data.

## 10. Summary of the model

Qimono Trading has one 35-player squad, divided into three fixed-size teams. Team A has 10 players targeting $20 each; Team B has 10 targeting $10 each; Team C has 15 targeting $5 each. Team assignments can change based on evolving evidence, with short-term performance the preferred primary trigger and medium- and long-term context also considered. Direct jumps between tiers are allowed. Full destination teams require a demotion to make room. Reclassification changes target capital allocation as well as team labels. Analytical attention follows a 4:2:1 ratio, illustrated by token budgets of 2,000 for SOL in Team A, 1,000 for IBM in Team B, and 500 for ALGO in Team C. All of this remains a conceptual planning framework until separately supported by verified execution data.
