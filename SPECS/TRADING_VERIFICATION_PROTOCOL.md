# QIMONO Trading Verification Protocol

**Status:** Operational protocol
**Scope:** Trading, portfolio, market-data, execution, and financial-analysis workflows
**Principle:** Never guess when missing information can change a financial decision.

## 1. Purpose

Today exposed a class of failure that is merely annoying in a software project but potentially expensive in a financial one: a model confidently operating without first establishing that it has the information required to act correctly.

The trading system therefore follows a fail-closed verification discipline.

> **VERIFY → TIMESTAMP → CALCULATE → ANALYZE → COMMUNICATE**

Not:

> **GUESS → SOUND CONFIDENT → DISCOVER LATER**

## 2. Information classes

Before answering a trading question, distinguish explicitly between:

### 2.1 Known facts

Data actually retrieved from an authoritative source.

### 2.2 Current market state

Price, volume, order book, market status, timestamps, execution quotes, and other state that can change over time. When the question depends on current state, obtain it from current market data.

### 2.3 Historical information

Clearly identify the date/time of the observation. Never present historical data as current.

### 2.4 Inference / analysis

Reasoning derived from the available data. Label it as analysis, not as a market fact.

### 2.5 Missing information

If an essential input is unavailable, stop and state what is missing rather than filling the gap with model knowledge.

## 3. Time awareness

Never confuse:

- the current time,
- the timestamp of a retrieved market observation,
- the timestamp of an execution,
- the conversation start time, or
- the market session being analyzed.

A timestamp must describe the event or observation it actually belongs to. Never fabricate a timestamp merely because one would make the answer look complete.

When current market state matters, the current observation must be distinguished from historical or workbook data.

## 4. Auditability

For consequential financial analysis, preserve the complete chain:

`SOURCE → TIMESTAMP → DATA → CALCULATION → INTERPRETATION`

Another AI teammate or human operator should be able to inspect that chain and reproduce the conclusion.

A plausible explanation without retrievable supporting data is not a verified answer.

## 5. Fail closed, not open

If essential information is missing, uncertainty reduces the scope of the answer rather than increasing model confidence.

Examples:

- A product-name error may waste research time.
- An incorrect market state can produce an incorrect position decision and financial loss.

Therefore the system must stop at the boundary of what can be established when a missing input could materially change the decision.

## 6. Retrieval failure is not evidence of absence

If an expected internal source cannot immediately be retrieved, do not conclude that the information does not exist.

Continue appropriate project archaeology across the available project surface before declaring information unavailable.

Distinguish:

- information does not exist,
- information exists but was not retrieved,
- information was retrieved but is stale,
- information was retrieved but is insufficient for the decision.

## 7. Financial market-data source protocol

For current financial market-price checks, **Yahoo Finance is the first external financial source to consult and the first source to mention explicitly in the response**.

When a current price is used, identify the source and timestamp rather than presenting the number as an unexplained fact. Use explicit wording such as:

> **Yahoo Finance:** ETP current price is **$X.XX** at **[timestamp]**.

Yahoo Finance is a market-data reference source, not execution truth. If the asset or workflow has a more authoritative execution venue, that venue remains authoritative for execution and fill details.

For the crypto trading workflow, Binance live Convert/execution data remains the execution test and the successful receipt remains execution truth. Yahoo Finance does not override a live exchange execution quote or receipt.

When useful, corroborate Yahoo Finance with another appropriate market source, but preserve the distinction between reference-market data and execution data.

## 8. Trading evidence hierarchy

When a decision depends on live execution state, use the most authoritative available execution source.

For the trading sprint, the operational runbook establishes that the broker/exchange receipt is execution truth and that the event log records reality after execution. Intended trades must not be pre-booked as if they were executions.

A workbook value is not automatically a current market fact. Current prices must be refreshed from the appropriate live source when current state matters.

For market-price reporting, apply the financial market-data source protocol in Section 7 first, then distinguish any execution-venue data used for the actual trade decision.

## 9. Calculation discipline

Do not calculate from an unverified input merely because the resulting number looks reasonable.

For every consequential calculation:

1. Identify the source of each input.
2. Record the applicable timestamp.
3. Preserve the raw value.
4. Show or preserve the calculation.
5. State the resulting interpretation separately from the raw fact.
6. Identify assumptions and unresolved uncertainty.

## 10. Multi-LLM handoff

When ChatGPT, Claude, Gemini, Grok, or another model contributes financial analysis, record:

- **What was checked**
- **What source was used**
- **What timestamp applies**
- **What raw data was retrieved**
- **What was calculated**
- **What interpretation was produced**
- **What remains uncertain**

The next model should inherit the evidence, not merely the prose.

Recommended handoff structure:

`CHECKED → SOURCE → TIMESTAMP → RAW DATA → CALCULATION → INTERPRETATION → UNCERTAINTY`

## 11. Operational gate

Before giving or executing consequential trading analysis, ask:

**Can I prove the inputs required for this decision?**

- **Yes:** proceed with calculation and analysis.
- **Partially:** constrain the answer to what the evidence supports and identify the missing inputs.
- **No, and the missing information is decision-critical:** stop and fail closed.

## 12. Relationship to the trading event model

The verification protocol complements the trading event-sourced workflow:

`REAL EXECUTION → SOURCE EVENT LOG → DERIVED POSITION → STRATEGY LOT → DASHBOARD`

Verification comes before interpretation of the event, position, strategy lot, or dashboard state.

Receipt truth remains execution truth. Derived sheets must not be treated as independent evidence when their upstream inputs are stale or unverified.

## 13. Core rule

> **Never guess when the missing information can change a financial decision.**

Confidence must be downstream of verification, never upstream of it.

## 14. Final doctrine

> **Verify → timestamp → calculate → analyze → communicate.**
>
> **Not: guess → sound confident → discover later.**

## 15. Wrapped and tokenized asset reference resolution

When a portfolio asset is represented by a wrapped, tokenized, synthetic, or otherwise platform-specific ticker, resolve the held instrument to its underlying asset before performing external market-price or reference-data lookups.

This is a **generic protocol rule for all current and future assets**, not a special case for individual tickers.

The workflow is:

`HELD / EXECUTION TICKER → INSTRUMENT IDENTIFICATION → UNDERLYING-ASSET RESOLUTION → EXTERNAL REFERENCE-PRICE LOOKUP`

The original ticker used by the exchange, wallet, or execution venue remains the **portfolio and execution identifier**. The resolved underlying ticker is used only for reference-market data and analysis where the underlying instrument is the intended reference.

Examples:

- `TSLAB → TSLA`
- `SPCXB → SPCX`

Do not substitute the wrapper's market quote for the underlying asset's reference quote merely because the wrapper is the instrument held in Binance or another wallet.

If an external provider cannot supply a verified quote for the resolved underlying asset, leave that provider unavailable rather than mixing instruments or silently substituting the wrapper quote.

The underlying-asset mapping should be treated as data that can grow as the portfolio grows. Do not encode the protocol as a finite list of today's examples.

This rule applies regardless of whether the wrapper originates from Binance, another exchange, a wallet, a tokenization platform, or another execution venue.

