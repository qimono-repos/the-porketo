# Projection by Event 98 — Sixth Draft

**Status:** Conceptual planning. This document is not an execution record and does not define final asset assignments.

## Governing idea

This draft extends the projection-by-event model from a trading strategy into a multi-dimensional resource-allocation architecture for a prediction system.

The central principle is:

**PREDICTION → RESOURCE ALLOCATION → DECISION → EXECUTION / NO-EXECUTION → OUTCOME → EVALUATION → NEXT PREDICTION**

Fibonacci is the common resource language. The Fibonacci sequence is preserved; the project defines a base unit for each resource dimension.

## Fibonacci resource architecture

The Fibonacci sequence is:

**1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...**

For capital, the base unit is **$0.75**:

- 1 = $0.75
- 2 = $1.50
- 3 = $2.25
- 5 = $3.75
- 8 = $6.00
- 13 = $9.75
- 21 = $15.75
- 34 = $25.50
- 55 = $41.25
- 89 = $66.75

The same Fibonacci sequence can govern other applicable resources, but each resource may have its own base unit.

Current conceptual resource units:

- **Capital:** $0.75 per unit.
- **Meeting time:** 2 minutes per unit.
- **Compute:** 75 tokens per unit.

Fibonacci values represent quantities of units. The $0.75 capital unit is not a modification of the Fibonacci sequence; it is the project's capital scale.

## Teams

The current conceptual squad remains three teams:

- **Team A:** 10 players.
- **Team B:** 10 players.
- **Team C:** 15 players.

Team tiers remain resource envelopes. Higher-tier teams normally receive greater capital, compute, analytical attention, and time through Fibonacci allocation.

For the current three-team investment example:

- Team C winner: 1 unit = $0.75.
- Team B winner: 2 units = $1.50.
- Team A winner: 3 units = $2.25.

The model is scalable. If additional teams are introduced, the Fibonacci sequence extends rather than arbitrary resource weights being invented.

## Dynamic meeting allocation

The scheduled checkpoint is an investment meeting, not merely a review meeting.

The normal meeting frame is 10 minutes:

- Team C: 2 minutes.
- Team B: 3 minutes.
- Team A: 5 minutes.

These are Fibonacci-structured team allocations, not permanently fixed timers.

The allocation can be dynamically composed while preserving Fibonacci structure. Illustrative frames include:

- C=3, B=5, A=8 → 16 minutes.
- C=5, B=8, A=13 → 26 minutes.

Information importance can temporarily change where meeting resources are concentrated. Team tier and current information priority are distinct concepts.

## Six-hour investment checkpoint

Every scheduled six-hour checkpoint is an active investment decision point.

At the checkpoint:

1. Current information and performance are assessed.
2. Candidate assets are investigated.
3. The opportunities compete for the checkpoint's investment.
4. Exactly one asset in one team is selected for investment, when a qualifying opportunity exists.
5. The investment amount is determined by the winning asset's team Fibonacci resource position.
6. The resulting investment is executed and becomes verified execution data for subsequent cycles.

Capital reallocation and investment decisions are checkpoint-driven. Streaming capital reallocation is outside this mechanism.

The system must not manufacture an investment merely to satisfy the six-hour cadence.

## Missed-investment red alert and penalty

If no asset has sufficient merit for investment at a checkpoint, this is a **red alert** condition.

Consecutive missed-investment checkpoints are counted:

- First missed investment: red alert.
- Second consecutive missed investment: red alert continues.
- Third consecutive missed investment: penalty is triggered.

After three consecutive missed investments, the penalty applies across three resource dimensions:

**Capital:** reduce the total available investment budget by 1 capital unit = **$0.75**.

**Time:** add 1 meeting-time unit = **2 minutes** to the next meeting. A normal 10-minute meeting therefore becomes 12 minutes.

**Compute:** add 1 compute unit = **75 tokens** to the next meeting's available compute budget.

The three-miss counter resets after the penalty is applied. A later sequence of three consecutive missed investments can therefore trigger another penalty.

The penalty is not intended to force an investment. It is a feedback mechanism: repeated inability to identify a qualifying opportunity costs capital while increasing analytical resources for the next checkpoint.

Allocated compute and actually consumed compute must be distinguished.

## Prediction-oriented objective

The objective is not to maximize the number of investments. The objective is to improve prediction quality.

Not investing can therefore be the correct decision when no asset merits investment. Repeated failure to identify an investment is itself information about the prediction process and triggers the defined feedback mechanism.

The system should evaluate whether additional resources actually improve prediction accuracy. Resource allocation and resource effectiveness are therefore coupled.

The conceptual feedback loop is:

**Prediction → decision → investment / no investment → outcome → evidence → resource adjustment → next prediction.**

## Prediction dimensions

Sentiment is introduced as a measurable prediction dimension, not as a standalone verdict.

Positive sentiment is not automatically a bullish investment signal. Sentiment must be evaluated alongside other dimensions, including price tendency and potentially other measurable characteristics.

The architecture may eventually include dimensions such as:

- sentiment strength,
- price direction,
- momentum,
- trend strength,
- trend acceleration,
- volatility,
- volume,
- news intensity,
- information quality,
- and other measurable features.

These are candidate dimensions, not yet a finalized universal formula.

The system should eventually evaluate which dimensions contribute useful predictive information rather than assuming any single dimension is always dominant.

## Evidence and execution discipline

This conceptual model remains subordinate to the project's execution-verification rules.

The operational chain remains:

**REAL EXECUTION → SOURCE EVENT LOG → DERIVED POSITION → STRATEGY LOT → DASHBOARD**

Broker/exchange receipts remain execution truth. No fills, prices, timestamps, or market data may be invented.

The projection model must distinguish verified execution data from workbook data, calculations, assumptions, analysis, and inference.

## Deliberate boundaries

This sixth draft does not yet define:

- a universal prediction score,
- a universal formula combining all prediction dimensions,
- hard thresholds for sentiment, trend, or momentum,
- permanent team assignments,
- future five-team roster sizes,
- a universal Fibonacci mapping for every possible resource,
- exact measurement methods for prediction accuracy,
- or actual future orders and fills.

Those require further decisions and verification.

## Core rule

**FIBONACCI DEFINES THE RESOURCE LANGUAGE.**

**PREDICTION QUALITY DETERMINES HOW RESOURCES ARE DEPLOYED.**

**OUTCOMES DETERMINE WHETHER THOSE RESOURCES WERE EFFECTIVE.**
