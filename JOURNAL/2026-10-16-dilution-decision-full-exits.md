# 2026-10-16 — Dilution decision: freeze new names, full exits of SLP, AAPL and BLK

**When:** Fri 16 Oct 2026, voice call ~14:10–14:30 Halifax; executions 14:30–14:38
**Who:** Operator (Albert) + Claude (decision support, booking, journal)
**Book:** TRADE-October-26-Sprint (ID `1X5JbgerRy5gv6uttPw3dOlw3Dj-qXfmOBDKlx1vX9V0`)

## The problem

After the morning's quantum expansion the portfolio held **43 distinct assets** (18 crypto, 25 stocks) on roughly 500 USD. The operator's concern was not how many names can be watched, but **dilution: too many assets with too little money in each.** New quantum lots were ~2.2 USD each; at that size Binance's 0.17 stock fee is ~7% of a 2.25 buy and harvests are worth cents.

## Decisions (operator)

1. **No new assets for the rest of October.** Every slot goes into names already held. This reinstates the 11 Oct "no new players" rule, with an end date (31 Oct).
2. **Quantum is non-negotiable.** The full quantum basket (IONQ, QBTS, IBM, QNTB, RGTI, QUBT, INFQ, XNDU, PSQL) stays intact.
3. **Sacrifice duplicates, not themes.** Remove positions whose exposure is already covered by another holding, so variety is preserved.
4. **No losses just for housekeeping.** Only sacrifice positions that are above their anchor; a below-anchor position is kept and given time. We are not in a crisis.
5. **Full exits settle in USDC** (returned capital → next month's budget). Harvests still settle in USDT. Exception: Lemon Cash has no USDC, so Lemon exits land in USDt.
6. **Exiting is not a ban.** Selling a full position now does **not** exclude re-entering it slowly next month. AAPL, SLP and BLK are in fact **priority re-entry candidates**: they are known assets, and the exits showed we can sell above what we paid.

## Candidates discussed and outcome

| Asset | Reasoning | Outcome |
|---|---|---|
| SLP | Axie stack duplicated by AXS + RONIN; SLP is the inflationary in-game reward token | **Sold (full)** |
| AXS | Kept over SLP: governance token, less inflationary | Kept |
| ILV | Duplicates IMX (Immutable stack) but ~3 USD below anchor | Kept — no housekeeping losses; long-run speculation |
| NEAR | L1 overlap with SOL/SUI; live 4.8963 → ~13.99 vs 15 anchor | Kept (below anchor) |
| DOT | Slightly above anchor, but carries the Infra #1 / Referendum 1944 dotUSD thesis | Kept (thesis matters) |
| AAPL | "Coca-Cola" mega-cap that doesn't drive the thesis; above anchor at 343.20 | **Sold (full), Binance + Lemon** |
| CVX | Only oil exposure; useful hedge for a tech-heavy book | Kept |
| BLK | Finance still covered by HOOD/HOODB; above anchor at 1,127.53 | **Sold (Binance lot)**; Lemon BLK lots pending |

## Executions (receipts are execution truth)

| Event | Venue | Detail | Proceeds | vs anchor |
|---|---|---|---|---|
| CRT-0069 | Binance Convert | 68,191.01655653 SLP → USDC, 1 USDC = 1,753.88 SLP, fee 0 | **38.87999839 USDC** | ≈ −1.44 (anchor 40.37, partly derived; price slid into the sale) |
| STT-0051 | Binance Stocks | 0.06452369 AAPL @ 343.25, fee 0.17, order c1e562a1… | **+21.98 USDC** (settles **2026-10-19 15:00**) | ≈ +1.99 |
| STT-0052 | Binance Stocks | 0.011682287 BLK @ 1,129.76, fee 0.17, order f450a5f3… | **+13.03 USDC** (settles **2026-10-19 15:00**) | ≈ +0.52 |
| TRD-0053 | Lemon Cash | 0.373747113 AAPL @ U$342.64, fee 0.64, tx 1c806b34… | **127.37 USDt** | experiment lot a gain |

Note the SLP result honestly: it ended slightly **below** its (partly derived) anchor. AAPL and BLK are the clean "sold above buy price" demonstrations.

### Legacy AAPL found in Lemon

Lemon sold 0.373747113 AAPL, but the book only had 0.044467. The extra **0.329280113 AAPL** are leftovers from earlier generations of the experiment (the hand-made trading era). Booked as STR-0012 at mark-to-market (no fake P/L, no cash effect), so their sale becomes **new experiment capital**. Lemon USDt balance afterwards: **U$127.57 = 127.37 + 0.20** from the earlier AAPL harvest (TRD-0034) — ties out.

## Cash and budget effects

- **Binance USDC:** +38.88 now (SLP). +21.98 and +13.03 arrive at **settlement on Mon 19 Oct 15:00**. Expected USDC after settlement ≈ 177.25 + 38.88 + 35.01 = **≈ 251.14** (before any further slots).
- **Lemon USDt 127.57:** funds Lemon trading directly, **without ARS conversion**; the remainder goes to the November budget.
- **November:** the 212 USDC top-up planned this morning shrinks by the ~73.89 USDC from these Binance exits, and further by whatever Lemon USDt is left at month end.
- **Survival money:** these proceeds are mostly returned principal (plus legacy capital), not harvest profit. Track them separately from the subscription-survival USDT.

## Open items

- **Lemon BLK lots** (≈0.006444 sh, anchors 4.72 + 2.23) were on the exit list but no Lemon receipt yet.
- **Lemon "USD PayPal" balance:** the operator asked whether it can be treated as the USDC-like budget coin. Answer: PayPal USD (PYUSD) is a fully dollar-backed stablecoin, so as a store of budget value it is USDC-equivalent 1:1. Book it as its own currency line (not merged into USDC) so venue reconciliation stays exact, and watch the conversion spread whenever it is moved.
- Next sacrifices are chosen from positions that are **both redundant and above anchor**, scanned at the next price refresh.
