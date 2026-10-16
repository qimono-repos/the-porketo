# 2026-10-16 — October survival threshold crossed

**When:** Fri 16 Oct 2026, ~08:00 Halifax (GMT−3)
**Who:** Operator (Albert) + Claude, voice session

## The milestone

Binance wallet USDT = **24.05355463**, read aloud by the operator and matched to the book to the last digit.

The experiment has to pay for its own tools at the end of each month:

| Subscription | USD/month |
|---|---|
| Claude | 10 |
| ChatGPT | 10 |
| **Total** | **20** |

24.05 USDT ≥ 20 → **the October bills are covered, ~4.05 to spare, with two weeks of the sprint still left.** The experiment survives into **November**.

## How the USDT got here (book = wallet)

- 23.72355463: reconciled at ~06:22 (includes CRR-0010 +0.70, not yet attributed)
- +0.24 TSLAB harvest (STT-0044)
- +0.02 IBMB harvest (STT-0045)
- +0.05 SLP harvest (CRT-0067)
- +0.02 DOT harvest (CRT-0068)
- **= 24.05355463** ✔ exact

Today's four harvests were done live by voice, one at a time, entering the USDT amount from the 50% rule. BLK and DUK are waiting for the US market open.

## Honest caveat (keep both views)

- **Operator view, adopted for survival:** cash on hand in USDT covers the bills. This is the practical test: can the experiment pay for itself this month?
- **Stricter view, still open:** the Claude Code meeting defined survival as ~$20/month of *realised after-fee profit*. Part of the USDT balance is returned principal (the 14 Oct below-anchor exits: IMX, NEAR, PUMP, SUI) and an unattributed +0.70. Realised October profit has not been computed yet. → TODO: build the realised-profit metric so November can be judged on both views.

## What it means

- Month 1 of self-funding: passed.
- November is unlocked. Every harvest from now to 31 Oct widens the margin.
- Paying the bills from USDT reduces the harvest reserve. Book the payment as a withdrawal when it happens.

## November plan (decided 2026-10-16)

**Mechanics unchanged:** every checkpoint deploys the full **3 units × 0.75 = 2.25 USDC**. Tiers (A/B/C) decide how a slot's 3 units are split across players. They never reduce the slot. Missed checkpoints or over/under-deployment are evened out in the following checkpoints.

**Budget math:**

| Item | USDC |
|---|---|
| November slots: 30 days × 4 checkpoints = 120 × 2.25 | **270.00** |
| USDC now (after STT-0042/0043) | 191.17 |
| Rest of October: ~59 slots × 2.25 | −132.75 |
| Carry-over into November | ≈ 58.42 |
| **New funding needed** | **≈ 212** |

**Actions:**

1. **In the last days of October, add 212 USDC** of fresh investment budget (operator). Book it as a FUND row when it lands.
2. **November calendar events:** checkpoints every 6h, 04:00 / 10:00 / 16:00 / 22:00 GMT−3, from 1 Nov 04:00 to 30 Nov 22:00 (120 slots). Created 2026-10-16.
3. Subscriptions ($20) continue to be paid from USDT harvests, not from the 212.
