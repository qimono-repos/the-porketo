# Team Meeting Insights

**Project:** Qimono Trading  
**Research case:** Apple (AAPL) product-release event study  
**Prepared:** 2026-10-14  
**Status:** Research specification only. No market-data pull or return calculation has been completed in this document.

## Shared objective

Study whether an identifiable Apple product announcement is associated with a measurable change in AAPL price behavior, and test how that behavior differs across forecast horizons. The working principle is **asset × event × horizon**: a company need not have one universally appropriate trading horizon.

## Evidence gate: verify the event first

The conversation refers to an Apple smart-home display announcement on 2026-10-13, described as “HomeView,” with a 7-inch display, Siri AI integration, a US$299 price, and shipping beginning 2026-11-13. These details are **unverified leads from the conversation**, not established facts in this research record.

Before using the event as a catalyst:
1. Locate a primary Apple announcement or another reliable, independently verifiable source.
2. Record the exact publication/announcement timestamp, time zone, source URL, and retrieval time.
3. Confirm the product name, announcement date, preorder status, price, and availability.
4. If the event or timestamp cannot be verified, stop the event-specific analysis and document the limitation. Do not invent or infer an exact timestamp.

## Data requirements

- Obtain genuine AAPL intraday OHLCV data from a documented data provider.
- Record provider, endpoint or dataset, retrieval time, timezone, interval, and any licensing/availability limitations.
- Preserve raw source data unchanged; keep cleaned/derived data separate.
- Align the verified announcement timestamp with the market session and the provider's timestamp convention.
- Explicitly handle regular trading hours, pre-market/after-hours trading, market closures, missing bars, and daylight-saving/time-zone conversions.
- Do not fill missing observations with fabricated values. Do not use future information in features or predictions.

## Measurements to compute

For the verified event, report the data and exact observation windows used before calculating:

1. Price and volume behavior before and after the event.
2. Returns over candidate horizons supported by the available data, such as 30 minutes, 1 hour, 2 hours, 6 hours, and 1 trading day.
3. Volatility and volume relative to a clearly defined pre-event baseline.
4. If feasible, AAPL performance relative to an appropriate market benchmark over the same windows.
5. Sensitivity to the chosen event timestamp and window boundaries.

For every metric, state the formula, units, sample count, data source, and whether the value is observed or derived. Distinguish clock time from trading time; a six-hour calendar window may cross a market closure.

## Evaluation and controls

- Compare event-window behavior with comparable non-event periods and, where feasible, similar historical events.
- Define the baseline and evaluation procedure before inspecting results to reduce selection bias.
- Evaluate each horizon independently. Do not assume a product announcement causes a price move merely because the two coincide.
- Include transaction costs, spread, slippage, and execution constraints before drawing any trading conclusion.
- Keep descriptive event analysis separate from out-of-sample predictive performance.
- No trade recommendation follows from this specification alone.

## Division of work

The agents may work in the same repository branch, but should use **separate files** to reduce merge conflicts.

- **ChatGPT workstream:** event-study specification, data-quality checks, calculation definitions, and review of reproducibility.
- **Claude workstream:** independently verify event sources and investigate suitable intraday data-provider options, documenting source quality and constraints.
- Each agent should record findings in its own file and link to evidence. Integrate conclusions only after both workstreams' sources and assumptions have been reviewed.

Suggested separate outputs:
- `INSIGHTS/Team Meeting Insights.md` — shared scope, verification gates, and method.
- `INSIGHTS/AAPL_Event_Source_Review.md` — event verification and source evidence.
- `INSIGHTS/AAPL_Intraday_Data_Review.md` — provider assessment, schema, and data-quality notes.

Do not overwrite another agent's file. Coordinate before editing the shared specification.

## Acceptance criteria

The study is ready for analysis only when:
- the event and timestamp are independently verified;
- the source and retrieval metadata for the intraday series are recorded;
- raw data are preserved and timestamp alignment is checked;
- calculations can be rerun from documented inputs and code;
- results clearly separate observed facts, derived metrics, assumptions, and interpretation.

## Initial decision

**Next step:** verify the alleged 2026-10-13 product announcement from primary or reliable sources, then choose and document an intraday data source. No price-impact conclusion is made here.
