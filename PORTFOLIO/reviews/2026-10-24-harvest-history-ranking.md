# Which asset goes out for PAXG: harvest-history ranking (2026-10-24)

**Rule (Albert, 2026-10-24):** the asset with the fewest harvests, or the lowest harvested total, in the book's logged history goes out. Quantum and gaming are excluded. "Out" means no new units; it is sold only once it is back at or above its anchor.

**Source:** every SELL in `Trades` (Lemon), `Trades-October` and `Crypto Trades` up to 24 Oct. Full exits (SLP, AAPL, BLK) and reconciliation rows are not counted as harvests.

**Caveat:** some 14 Oct crypto sales were below anchor and are still "classification pending" (PUMP 0.80, NEAR 0.40, SUI 0.50, IMX 1.90 provisional). They are counted here as harvests.

## Zero harvests (candidates)

| Asset | Held since | Days held | Harvests | Status vs anchor (24 Oct 03:06) | Note |
|---|---|---|---|---|---|
| **OKLO** (Lemon + Binance) | 10 Sep | 44 | 0 | −35% / −30% | Nuclear power for AI. Never above anchor. Binance lot is a plain Binance Stock (0.17 fee, ~5.17 minimum). |
| **MDB** (Binance) | before 11 Oct | 13+ | 0 | −15% | Found in the wallet reconciliation, never a thesis pick. Plain Binance Stock (fee + minimum), so it is the worst wrapper for micro-harvests. |
| **HOOD / HOODB** | 10 Sep | 44 | 0 | −17% / −15% / new lot today | Three older lots, never harvested. 4.50 added today (STT-0066). |
| NVDA / NVDAB | 8 Sep | 46 | 0 | −3% to −6% | Excluded: core AI. Albert asked not to go to low AI exposure. |
| DUK | 14 Sep | 40 | 0 | above anchor | Excluded: harvestable today, and being migrated to DUKB. |
| TSMB, MUB, AMDB | 7 to 11 Oct | 13 to 17 | 0 | −1% to −20% | Too young to judge, and core AI/semis. |
| ALGO | 8 Oct | 16 | 0 | −5% to −16% | Young; already capped at tier C. |

## One harvest, smallest total

| Asset | Harvests | Total | Days held |
|---|---|---|---|
| DOT | 1 | 0.02 | 17 |
| ETH | 1 | 0.06 | 45 |
| FLKR | 1 | 0.13 | 45 |
| CVX | 1 | 0.20 | 45 |
| AVGO | 1 | 0.21 | 45 |

## Harvested most (keepers)

| Asset | Harvests | Total |
|---|---|---|
| IMX | 4 | 6.57 |
| PUMP | 2 | 5.80 |
| AXS | 3 | 3.90 |
| ZEC | 3 | 2.68 |
| AAVE | 1 | 2.60 |
| NEAR | 3 | 1.76 |
| SUI | 2 | 1.65 |
| TSLAB | 4 | 1.26 |
| IBMB | 3 | 0.92 |
| LINK | 2 | 0.94 |
| TAO | 3 | 0.83 |
| SOL | 1 | 0.72 |
| BTC | 4 | 0.55 |
| QBTS | 1 | 0.55 |
| ORCL | 1 | 0.53 |
| RONIN | 3 | 0.52 |
| SPCXB | 1 | 0.45 |

## Suggestion: 3 to go out

1. **OKLO**: 44 days, zero harvests, the deepest under anchor.
2. **MDB**: zero harvests, no thesis (a reconciliation find), and a wrapper with fees that blocks micro-harvests.
3. **HOOD / HOODB**: 44 days, zero harvests on the old lots. But a new lot was bought today, so stopping it right away is a judgement call.

If only one goes: **OKLO**. It has the strongest zero-harvest record of the three.
