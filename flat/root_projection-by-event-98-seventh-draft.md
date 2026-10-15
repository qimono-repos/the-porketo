# Projection by Event 98 — Seventh Draft

**Status:** Conceptual planning. This document is not an execution record and does not define final asset assignments, model parameters, or production forecasting rules.

## Governing idea

This draft reframes the projection-by-event model as an evolving prediction laboratory in which **dimensional discovery is a primary experimental objective**.

The system should begin forecasting as soon as practical, measure its errors against realized prices, and use those errors to discover which dimensions deserve to remain, be added, be removed, or receive additional analytical resources.

The central principle is:

**INVESTMENT PROVIDES THE EXPERIMENTAL FUEL → OBSERVE → PREDICT → MEASURE → LEARN WHICH DIMENSIONS MATTER → RECALIBRATE → NEXT ITERATION**

Investment is not the output of prediction. Investment is an input to the continuing experiment. Prediction provides directional and numerical guidance about future outcomes, while realized outcomes provide evidence for evaluating and improving the prediction system.

## Prediction target

The primary prediction target is the **exact future asset price**.

The initial forecasting horizons are:

- **T+6 hours**
- **T+12 hours**
- **T+18 hours**

Additional horizons may be introduced later as the experiment develops.

A forecast is generated at time T for each selected horizon. When the corresponding future time arrives, the realized asset price becomes the reference against which the forecast is evaluated.

The system should begin producing forecasts as soon as the required verified inputs are available. Early forecasts are experimental measurements, not expected to be optimal.

## Prediction error and model evolution

The first implementation should use a simple mathematical backbone, such as linear or multivariate linear regression, to establish a measurable baseline.

The mathematical backbone may become progressively more sophisticated:

1. Linear regression as a baseline.
2. More advanced statistical or nonlinear models when justified by observed limitations.
3. Fourier analysis to investigate frequency-domain structure and periodic behavior.
4. Combined frequency-domain and predictive approaches.
5. Eventually, investigation of the **Quantum Fourier Transform (QFT)** as a candidate mathematical instrument.

The progression is experimental, not predetermined. Greater mathematical complexity must earn its place through measurable predictive usefulness.

Mean absolute error (MAE) is an appropriate initial error measure because it is interpretable. Other error measures may be introduced and compared as the system matures.

The project must distinguish:

- **forecast accuracy**, meaning how close predicted price is to realized price;
- **economic investment performance**, meaning what happened to capital deployed into the asset.

These are related but distinct measurements.

## Open-ended dimensional discovery

The **Dimensional Log** is the central mechanism of this draft.

The system deliberately does **not** begin with a permanently fixed list of prediction dimensions.

Instead, dimensions are allowed to emerge from available evidence, experimentation, domain investigation, and observed predictive behavior.

Candidate dimensions may include, but are not limited to:

- price-related characteristics,
- momentum,
- trend strength,
- trend acceleration,
- volatility,
- volume,
- sentiment,
- sentiment strength,
- news intensity,
- information quality,
- market regime,
- liquidity or execution characteristics,
- frequency-domain characteristics,
- and other measurable variables discovered during the experiment.

These examples are illustrative, not a closed feature list and not a universal formula.

The purpose of the dimensional experiment is to determine which measurable information contributes to prediction quality.

## Prediction Dimensional Log

Each forecasting experiment should maintain a dimensional record.

At minimum, the conceptual record should distinguish:

**Dimension available → Dimension used → Forecast generated → Realized outcome → Prediction error → Subsequent usefulness assessment**

A dimensional record should preserve enough context to reproduce the experiment, including:

- timestamp,
- asset,
- prediction horizon,
- dimension name,
- dimension value or representation,
- whether the dimension was available,
- whether the dimension was used by the model,
- model/version context,
- predicted price,
- realized price,
- prediction error,
- and later assessment of predictive usefulness.

The usefulness assessment must initially remain open-ended. The project should not invent a universal dimensional-contribution score before sufficient observations exist.

A dimension therefore has three distinct states:

1. **Available:** the information existed and could have been used.
2. **Used:** the model incorporated it.
3. **Useful:** subsequent evidence indicates that its inclusion contributed to predictive quality.

A dimension being available does not imply that it should be used. A dimension being used does not imply that it is useful.

This distinction is essential to preventing complexity from accumulating merely because more features are available.

## Progressive learning experiment

The first experimental iterations use the team structure as a progressively expanding information universe.

### Iteration 1 — Team A

Team A provides the initial asset universe for forecasting.

The first models generate forecasts from Team A data. Outcomes are collected, prediction errors are measured, and the dimensional log records which information was available and used.

The purpose is to establish the first baseline and begin discovering useful dimensions.

### Iteration 2 — Team A + Team B

The knowledge and model refinements from Iteration 1 are applied to an expanded universe containing Team A and Team B.

The experiment continues measuring forecast error and dimensional usefulness.

This iteration tests whether the learned structure remains useful when the information universe expands.

### Iteration 3 — Team A + Team B + Team C

The experiment expands again to Team A, Team B, and Team C.

Team C may serve as a held-out testing population for evaluating whether the prediction system generalizes beyond the data used during earlier model development.

The exact train/validation/test methodology remains subject to the temporal structure and volume of the collected data.

For financial time series, chronological ordering and information leakage must be treated explicitly. Test information must not be allowed to influence model tuning before the test is evaluated.

The A → A+B → A+B+C progression is therefore an experimental architecture, not a claim that these team partitions are universally optimal.

## Investment as experimental fuel

Investment remains a continuous experimental input.

The project does not treat investment as the result of prediction. Capital is deployed to create and observe real experimental conditions.

Different assets can receive different amounts of fuel, and their subsequent realized behavior becomes part of the evidence available to the prediction system.

The conceptual loop is therefore:

**INVEST → OBSERVE → PREDICT → WAIT → MEASURE → RECALCULATE → ADJUST INVESTMENT → OBSERVE AGAIN**

The prediction system can influence the next allocation of experimental fuel, but prediction and investment remain conceptually distinct layers.

## Fibonacci resource architecture

The Fibonacci sequence remains the common resource language:

**1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...**

For capital, the base unit remains **$0.75**:

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

Other resource dimensions may use the same Fibonacci sequence with their own base units.

Current conceptual resource units remain:

- **Capital:** $0.75 per unit.
- **Meeting time:** 2 minutes per unit.
- **Compute:** 75 tokens per unit.

Fibonacci defines the resource language. It does not dictate that every resource must use the same absolute quantity or the same mapping.

## Teams and analytical resources

The current conceptual squad remains:

- **Team A:** 10 players.
- **Team B:** 10 players.
- **Team C:** 15 players.

Higher-tier teams normally receive greater resource envelopes.

For the current three-team investment example:

- Team C winner: 1 unit = $0.75.
- Team B winner: 2 units = $1.50.
- Team A winner: 3 units = $2.25.

The model remains scalable to additional teams by extending the Fibonacci sequence rather than inventing arbitrary resource weights.

Fibonacci allocation can also govern analytical attention, compute depth, investigation, questioning, experimentation, and meeting time where those resources are applicable.

## Dynamic meeting allocation

The scheduled checkpoint remains an active investment meeting.

The normal conceptual meeting frame is 10 minutes:

- Team C: 2 minutes.
- Team B: 3 minutes.
- Team A: 5 minutes.

These are Fibonacci-structured allocations, not permanently fixed timers.

Dynamic frames can be composed while preserving Fibonacci structure. Illustrative frames include:

- C=3, B=5, A=8 → 16 minutes.
- C=5, B=8, A=13 → 26 minutes.

Information importance may temporarily change where meeting resources are concentrated. Team tier and current information priority remain distinct concepts.

## Six-hour checkpoint

Every scheduled six-hour checkpoint remains an active investment decision point.

At each checkpoint:

1. Current information and performance are assessed.
2. Candidate assets are investigated.
3. Forecasts are generated for the applicable horizons.
4. Dimensional availability and usage are recorded.
5. The current prediction model is evaluated against available realized outcomes.
6. Candidate investment opportunities are considered.
7. Exactly one asset in one team is selected for investment when a qualifying opportunity exists.
8. The investment amount follows the winning asset's team Fibonacci resource position.
9. The resulting investment becomes verified execution data for subsequent cycles.

The system must not manufacture an investment merely to satisfy the cadence.

## Missed-investment red alert and penalty

If no asset has sufficient merit for investment at a checkpoint, this is a **red alert** condition.

After three consecutive missed investment checkpoints, the existing penalty mechanism applies:

**Capital:** reduce the total available investment budget by 1 capital unit = **$0.75**.

**Time:** add 1 meeting-time unit = **2 minutes** to the next meeting.

**Compute:** add 1 compute unit = **75 tokens** to the next meeting's available compute budget.

The three-miss counter resets after the penalty is applied.

The penalty is a feedback mechanism, not a command to fabricate an investment. Allocated compute and actually consumed compute must remain distinct.

## Resource effectiveness

The project should evaluate whether additional resources improve prediction quality.

For example, additional compute, meeting time, investigation, or analytical attention should be treated as experimental resources whose effectiveness can be measured rather than assumed.

This creates another feedback loop:

**RESOURCE ALLOCATION → PREDICTION → OUTCOME → ERROR → RESOURCE EFFECTIVENESS**

The objective is not to maximize resource consumption. It is to determine whether additional resources produce better predictions.

## Evidence and execution discipline

This conceptual model remains subordinate to the project's execution-verification rules.

The operational chain remains:

**REAL EXECUTION → SOURCE EVENT LOG → DERIVED POSITION → STRATEGY LOT → DASHBOARD**

Broker/exchange receipts remain execution truth.

No fills, prices, timestamps, or market data may be invented.

The prediction system must distinguish verified execution data from workbook data, calculations, assumptions, analysis, inference, and model-generated predictions.

For crypto, verified Binance live quotes and execution receipts take precedence over stale workbook prices where current market information is required.

## Deliberate boundaries

This seventh draft does not yet define:

- a universal prediction score;
- a universal formula combining all prediction dimensions;
- a closed list of prediction dimensions;
- a universal dimensional-contribution score;
- hard thresholds for individual dimensions;
- the final train/validation/test partition methodology;
- permanent team assignments;
- future five-team roster sizes;
- a universal Fibonacci mapping for every possible resource;
- a final production model;
- or actual future orders and fills.

These require further observations, experimentation, and verification.

## Core rules

**THE DIMENSIONAL LOG IS THE EXPERIMENTAL MEMORY OF THE PREDICTION SYSTEM.**

**DIMENSIONS ARE DISCOVERED, NOT PREDECLARED AS A CLOSED LIST.**

**FIBONACCI DEFINES THE RESOURCE LANGUAGE.**

**INVESTMENT PROVIDES THE EXPERIMENTAL FUEL.**

**PREDICTION QUALITY IS MEASURED AGAINST REALIZED OUTCOMES.**

**MODEL COMPLEXITY MUST EARN ITS PLACE THROUGH MEASURABLE PREDICTIVE USEFULNESS.**

**OUTCOMES DETERMINE WHETHER THE MODEL AND ITS RESOURCES WERE EFFECTIVE.**
