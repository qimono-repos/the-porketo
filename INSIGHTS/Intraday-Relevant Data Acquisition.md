# Intraday-Relevant Data Acquisition Is a Priority

**Project:** Qimono Trading / the-porketo  
**Category:** INSIGHTS  
**Recorded:** 2026-10-16

## Core insight

Data acquisition must give special, explicit priority to information that is useful for **intraday trading**. The system should not merely accumulate information; it should acquire, timestamp, preserve, and evaluate the information that can materially improve a near-term investment or harvesting decision.

## Data priorities

- **Live market state:** current and recent prices, bid/ask spread where available, volume, liquidity, volatility, and intraday price structure.
- **Execution context:** actual orders, fills, fees, timestamps, rejections, and exchange/broker status. Execution receipts remain the source of truth for completed trades.
- **Market-moving events:** earnings releases, guidance, macroeconomic announcements, central-bank decisions, company news, regulatory developments, and relevant sector or peer movements.
- **Cross-market context:** broad-market and sector direction, correlated assets, futures or benchmark moves where relevant, and changes in risk appetite.
- **Data freshness and quality:** source identity, event time, retrieval time, update frequency, missing values, delays, and conflicting observations.

## Operational rules

1. **Relevance before volume:** prioritize data according to whether it can change an intraday decision, risk estimate, or harvesting opportunity.
2. **Timestamp everything:** distinguish when an event occurred from when the system learned about it.
3. **Respect source authority:** use exchange/broker receipts for actual executions; label quotes, third-party feeds, calculations, and interpretations separately.
4. **Preserve history:** retain event logs so decisions can be reconstructed and later evaluated.
5. **Match acquisition cadence to the decision horizon:** fast-changing market data may require frequent refreshes, while slower-moving fundamentals can be stored and consulted when relevant.
6. **Fail closed on critical uncertainty:** if a required price, timestamp, execution, or other decision-critical input cannot be verified, do not fabricate it or treat it as confirmed.
7. **Measure usefulness:** assess whether each data source improves decision quality and net results after costs, rather than assuming that more data is better.

## Relationship to the cadence objective

The project's ambition to shorten the interval between valid investment and harvesting events depends on timely, decision-relevant data. Better acquisition can reduce avoidable delay, but faster ingestion alone does not establish a trading edge. Data latency, completeness, accuracy, and the cost of acting on it must be evaluated together.

## Guiding principle

**Acquire the right information at the speed the decision requires, preserve its provenance, and act only when the evidence is sufficient.**
