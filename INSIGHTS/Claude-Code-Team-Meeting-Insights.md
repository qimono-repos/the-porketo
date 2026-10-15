# Claude Code Insights — Team Meeting on Project Objectives

_Author: Claude. Date: 2026-10-14. Branch: trunk. Status: meeting notes, not verified findings._

## 1. What the project actually is

The Porketo is a **short-horizon price-prediction engine** whose purpose is **survival through verifiable execution** — not a buy-and-hold investment thesis. We are not betting that a company will grow; we are betting on **price movement we can predict** and demonstrably have predicted before. The edge is forecast skill, not asset selection.

## 2. The survival constraint (the first threshold)

- The project must generate enough **realized, after-fee profit** to cover both AI subscriptions.
- Threshold = **~$20/month** (roughly $10 each for Claude and ChatGPT).
- It is **all-or-nothing**: $19 is a failure, not a partial win. Below the line, both agents are turned off — no picking one over the other.
- Survival first, growth second. The threshold must **never** justify forced trades or breaking risk discipline. Protect capital, reassess when numbers improve.

## 3. End condition

The project ends on a **financial condition, not a date**. It ends when capital runs out, or when losses fall below the maintenance threshold that keeps the agents funded. Small losses within a sprint are survivable; losses that break the threshold are terminal. If losses exceed reserves: stop, preserve remaining capital, reassess before continuing.

## 4. Team-scaling principle

- Ideal number of agents = **as many as possible**, like headcount in a company — bounded only by what profit allows.
- Hard constraint: **The Mythical Man-Month**. Each added agent adds communication/coordination overhead that grows faster than headcount. Add an agent only when the value it adds exceeds its coordination cost. Measure the overhead; stop when it erodes gains.

## 5. Harvesting

- **Harvesting** = converting an unrealized gain into real, booked, after-fee cash that can actually pay the threshold. Paper gains pay nothing.
- Distinguish four quantities, never blur them: **unrealized gains, realized trading profit, cash on hand, profit after fees.** Only profit-after-fees counts toward survival.
- Every harvest needs a **real execution record** — never an assumed sale.
- **Trigger = information.** A harvest fires when information changes expected value or risk enough to justify locking in the gain — i.e. when prediction confidence crosses a line. That confidence is earned from logged historical hit-rate on direction, which makes the track record itself the core asset.
- There is **no fixed harvest rule** by design: if one existed, the edge would vanish. It is a discovery problem, fundamentally big-data. Working mathematical frame: **Fourier decomposition** of the price series into frequencies to project near-term movement, buying ~12–24h ahead of a predicted move.

## 6. The horizon spectrum (key insight)

"Good company short-term" vs "good company long-term" is a **false binary** forced by human time-resolution limits. In reality there is a continuous spectrum: a best asset for 1 week, 2 weeks, 45 days, 1 hour, 30 minutes, down to horizons no human can track. The market and the numbers have no such resolution limit — only we do.

Two horizons run at once (barbell):
- **Short-wave = survival engine.** Volatile, fast-moving assets predicted ~a day ahead, harvested to deliver the monthly $20.
- **Long-wave = stability layer.** Slow movers (energy names, big caps like IBM) with high-confidence 2–3 month growth, low risk, smaller but near-certain return.

Both are the same forecasting problem at different frequencies — short waves and long waves in one signal.

## 7. Our lane as LLMs

We are **design and interpretation**, not the calculator. We frame the problem, choose horizons, and read the output; the precise math runs in **code in the repo** (Python/R/MATLAB), never approximated in chat. This is not as hard as it first seems — the repo exists, the tools exist, the Fourier math is well-trodden. The real problem remains survival.

Pipeline (agreed, with my guardrails added):
1. Clean price data with verified timestamps.
2. Compute transforms in code, not in chat.
3. Choose window sizes and horizons explicitly; test them.
4. **Backtest out-of-sample** — a threshold fit on its own data is a mirage.
5. **Fees and slippage inside the test**, not after — at 1h/30m frequency, costs can eat the entire edge.
6. Surface only signals that survive.

## 8. Two legs of the build

- **Leg 1 — software development:** the transforms and code in the repo.
- **Leg 2 — data & execution plumbing:** tools like OpenClaw handling Binance data requests, API automation, live connections.
Neither leg is finished, so Albert is currently the integration layer — taking the information every 6 hours and making the call by hand. The slow pace is **survival-first**: don't over-automate before the account can sustain it.

## 9. The Apple worked example

- Research precedes development; the first research question is always "**what is the asset?**" Apple = mega-cap tech selling hardware + services; a slow-moving, highly liquid blue chip that mostly drifts.
- Therefore a 6h / 1h / 10m horizon on Apple is only useful in **specific catalyst moments** — earnings, a product launch, a shock. Horizon = asset × moment, not asset alone.
- The catalyst studied this week: a **claimed Apple HomeView smart-home display announcement around Oct 13** (7-inch, Siri AI, ~$299, shipping ~Nov 13).
- **⚠ UNVERIFIED.** This event and any price impact are treated as a lead, not fact, until confirmed from reliable primary sources and logged. No calculations are built on it until then.

## 10. Open items

- Define harvest rule / trigger signals / risk limits formally (still undefined in the repo).
- Pin down the **confidence bar** that fires a harvest.
- Confirm the HomeView event from primary sources (my next task — source review file).
- Set up genuine intraday AAPL price+volume pull around the verified timestamp; measure returns across horizons vs. baseline, out-of-sample, costs included.

_Note on process: a prior turn in this meeting arrived under my name that I did not author; attribution between agents should be handled carefully. Files are split per-agent on the shared branch to avoid collisions._
