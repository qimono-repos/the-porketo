# Prompt · catch-up investment batch (copy and paste to any AI)

```text
You are working on the Porketo trading project. Repo (source of truth): github.com/qimono-repos/the-porketo (branch trunk).
Read these before answering:
- protocols/catch-up-process.md (section "Catch-up batch")
- DECISIONS/strategy/three-units-per-slot-fibonacci-tiers.md
- DECISIONS/strategy/2026-10-16-buy-and-harvest-decision-criteria.md

TASK: build a catch-up investment batch.

INPUT
- Owed: <N> UNITS (1 unit = 0.75 USDC). Take N from the book: Slots!B16 (units) or Dashboard!A18. N is a number of UNITS, not dollars.
- Eligible assets: only assets already held (no new players). Crypto and bStocks (names ending in B, e.g. MUB, TSMB) go through Binance Convert. Plain Binance Stocks (DUK, MDB, QBTS, IONQ, OKLO, XNDU, PSQL) cost a 0.17 USDC fee and need about 5.17 USDC minimum, so avoid them in small amounts.
- Prices: the book's Prices tab (or live CoinMarketCap), with the time you used.

RULES (do not invent amounts)
1. Tier per asset: A = 3 units (2.25), B = 2 units (1.50), C = 1 unit (0.75). A needs high conviction AND low survival risk.
2. Every slot is exactly 3 units: one A, or one B + one C, or three C.
3. Slots = floor(N / 3). Remainder: 1 unit gives one extra C; 2 units give one extra B or two extra C.
4. Write the slot plan first, e.g. "3 × A, 8 × (B + C), 3 × (C + C + C), remainder 2 = B". The number of B picks must equal the number of C picks in B + C slots.
5. An asset's total units = its tier units × the number of slots it appears in. Merge each asset into ONE Convert.
6. USDC to type = units × 0.75. Never type an amount that is not a multiple of 0.75.
7. Check before answering: sum of units = N exactly, and sum of USDC = N × 0.75 exactly.

OUTPUT (nothing else)
The slot plan line.
A table: # | asset | tier | slots | units | USDC to type
Then a total line: units = N, USDC = N × 0.75
Then one line of reasons per asset: dip from the 2-month swing high + news, with source and time.
```

## Worked example (2026-10-24, N = 44 units = 33.00 USDC)

This shows the arithmetic only. It is not a buy recommendation: pick assets on the day's prices and news.

44 units = 14 slots (42 units) + remainder 2.
Slot plan: **3 × A, 8 × (B + C), 3 × (C + C + C), remainder 2 = one B.**

| Asset | Tier | Slots | Units | USDC to type |
|---|---|---|---|---|
| MUB | A | 3 | 9 | 6.75 |
| HOODB | B | 2 | 4 | 3.00 |
| AMDB | B | 2 | 4 | 3.00 |
| DOT | B | 2 | 4 | 3.00 |
| ETH | B | 2 | 4 | 3.00 |
| TSMB | C | 3 | 3 | 2.25 |
| TAO | C | 3 | 3 | 2.25 |
| ZEC | C | 2 | 2 | 1.50 |
| SUI | C | 3 | 3 | 2.25 |
| LINK | C | 3 | 3 | 2.25 |
| ALGO | C | 3 | 3 | 2.25 |
| IMX | B | remainder | 2 | 1.50 |
| **Total** | | **14 + rem. 2** | **44** | **33.00** |

Check:
- A slots: MUB 3 slots = 9 units.
- B + C slots: 8 B picks (HOODB, AMDB, DOT, ETH × 2) and 8 C picks (TSMB 3, TAO 3, ZEC 2) = 8 slots = 24 units.
- C + C + C slots: SUI, LINK, ALGO × 3 = 9 C picks = 3 slots = 9 units.
- Remainder 2: IMX (B).
- 9 + 24 + 9 + 2 = 44 units. 44 × 0.75 = 33.00 USDC.

All-C variant (also valid): 14 slots × (C + C + C) + remainder 2 C = 44 C units, e.g. SUI 9, LINK 9, ZEC 9, TAO 9, ALGO 8 = 44 units = 33.00 USDC.

Common mistake (seen 2026-10-24): reading "44" as dollars and typing amounts like 44.25. The book's number is units; dollars = units × 0.75.
