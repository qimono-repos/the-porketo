# Intraday Harvesting and Cadence as a Core Design Objective

**Project:** Qimono Trading / the-porketo  
**Category:** INSIGHTS  
**Recorded:** 2026-10-16

## Core insight

The Porkito project is an **intraday investment-and-harvesting system**. Its long-term design objective is to progressively reduce the time interval, or cadence, between eligible investment and harvesting movements.

In practical terms, the system should aim to become capable of identifying, evaluating, and executing valid opportunities on increasingly shorter time horizons as its data, decision logic, execution reliability, and risk controls improve. The intended direction is toward a tighter feedback loop: observe market conditions, evaluate an opportunity, act when justified, record the real execution, update the derived position and strategy lot, and learn from the result.

## What “ever-decreasing cadence” means

Here, cadence means the elapsed time between eligible decision or investment/harvesting events. The ambition is for that interval to decrease over the system's evolution, rather than remain fixed at a slow, predetermined schedule.

This is a **design objective, not a promise that every trade interval must shrink forever**. The system should only increase event frequency when the data quality, market conditions, expected edge, execution costs, liquidity, and risk controls support doing so. Faster activity without a verified advantage can increase fees, slippage, noise sensitivity, and operational errors.

## Implications for system design

1. **Short feedback loops:** Minimize unnecessary delay between observation, decision, execution, and recording.
2. **Event-driven decisions:** Use market and portfolio events to trigger evaluation where appropriate, rather than relying only on a fixed clock.
3. **Evidence before action:** More frequent checks do not imply more frequent trades. A movement is eligible only when verified data and the strategy's rules justify it.
4. **Execution truth:** Record actual broker/exchange receipts as the authoritative evidence of fills. Never infer a fill from a signal, quote, or intended order.
5. **Auditable feedback:** Preserve the chain from real execution to source event log, derived position, strategy lot, and dashboard.
6. **Adaptive cadence:** Evaluate whether a shorter cadence improves net results after fees, spread, slippage, latency, and risk. Keep slower intervals when they produce better decisions.
7. **Safety constraints:** Maintain position, exposure, liquidity, and operational limits regardless of how fast the system becomes.

## Measurement

Track cadence as an explicit metric, including:
- Time between market observation and decision.
- Time between decision and confirmed execution.
- Time between eligible harvesting opportunities.
- Net result per harvesting event after transaction costs.
- Missed or rejected opportunities, false signals, slippage, and operational failures.

Compare these metrics over time. A shorter interval is beneficial only when it improves the system's risk-adjusted, after-cost performance and reliability.

## Guiding principle

**Reduce the time between valid opportunities and verified action, not the time spent on necessary verification.**

The destination is a progressively more responsive intraday harvesting system whose cadence can contract as its capabilities mature, while every action remains evidence-based, auditable, and risk-controlled.
