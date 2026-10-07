# REMINDER — 2026-10-08 (Halifax): finish the harvest calendar events

Status: OPEN
Created: 2026-10-07 (Halifax), during the harvesting-strategy session.

## Why this exists

The harvest calendar build was paused on 2026-10-07 after reaching the
per-session limit. 51 of 98 events exist; 47 remain.

## Done (do NOT recreate — avoid duplicates)

- Harvest 1 of 98 → Harvest 51 of 98
- From Tue 2026-10-06 16:15 to Mon 2026-10-19 04:15 Halifax
- Calendar: alberto.gruning.zen@gmail.com (primary)

## To do

- Harvest 52 of 98 → Harvest 98 of 98
- From **Mon 2026-10-19 10:15** to **Fri 2026-10-30 22:15** Halifax
- Before starting: list events titled "Harvest" from 2026-10-19 onward to
  confirm 52 does not already exist.
- Create in small batches (avoid hammering the Calendar API).

## Schedule rule

- Every 6h, 15 min after each investment checkpoint.
- Slots: 04:15, 10:15, 16:15, 22:15 Halifax (America/Halifax, UTC-3).
- Harvest N pairs with Checkpoint N of 98 (investment at HH:00).
- Duration 10 min (HH:15–HH:25).

## Event template (approved 2026-10-07 — keep identical)

- Title: `Harvest N of 98 · Convert to USDT · Trading`
- Location: `Binance / Broker`
- Google Meet: auto-generated per event
- Reminder: popup at 0 min (when event starts)
- Availability: Free
- Time zone: America/Halifax
- Description (plain text; each URL alone on its own line with blank lines around it):

```
HARVEST N OF 98

Pairs with: Checkpoint N of 98 (investment, HH:00 Halifax)

Each harvest checkpoint accrues a harvest obligation, even if missed. Missed obligations carry forward.
No-go harvest (nothing harvested) triggers a forced harvest: sell 50% of the anchor of the lot with the smallest dollar gap below its harvest threshold. The lot keeps its identity and anchor.
Harvests settle into USDT.
Cadence: every 6h, 98 harvests, from 2026-10-06 16:15 Halifax to 2026-10-30 22:15 Halifax. Slots: 04:15, 10:15, 16:15, 22:15 Halifax (15 min after each investment checkpoint).

Quick links

Book (TRADE-October-26-Sprint)

https://docs.google.com/spreadsheets/d/1N_osVjWlUVElmZ8UoPUIa5aFex-gfSvy4nJ02k-_KrY/edit?gid=1297109055#gid=1297109055

Binance Convert (BTC to USDT)

https://www.binance.com/en/convert/BTC/USDT

Yahoo Finance portfolio

https://finance.yahoo.com/portfolio/p_1/view/v1

CoinMarketCap watchlist

https://coinmarketcap.com/?tableRankBy=watchlist

Repo (the-porketo)

https://github.com/qimono-repos/the-porketo

Claude project (trading)

https://claude.ai/project/01a0f176-9461-7388-85aa-cf9990c1f158

ChatGPT project (trading)

https://chatgpt.com/g/g-p-6abc2892f6f48191b4f9922cc0627e68/project

Source: Harvesting strategy agreed 2026-10-07 (pending README/repo commit). TRADE-October-26-Sprint.
```

## Harvesting rules agreed 2026-10-07 (context; still pending README commit)

- Separate harvest checkpoints, 15 min after each investment checkpoint.
- Deployment-style obligation: a no-go harvest triggers a forced harvest;
  missed obligations carry forward.
- Forced harvest = crisis-rule selection (lot with smallest dollar gap below
  its harvest threshold), selling **50%** of that lot's anchor (not 90%).
- Harvests settle into **USDT**.

## Close-out

When Harvest 98 exists, set Status to DONE and note the date.
