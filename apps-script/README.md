# Price worker (book `Prices` tab)

**The price worker refreshes at 03:00, 09:00, 15:00 and 21:00 Halifax, one hour before each slot (04, 10, 16, 22). So at every slot, the Prices tab is at most an hour old.**

## What it does

| | |
|---|---|
| Where | Google Apps Script bound to the book (Extensions → Apps Script) |
| When | 03:00, 09:00, 15:00, 21:00 Halifax (`atHour` triggers, timezone `America/Halifax`) |
| Crypto | One CoinGecko call for all coins (column C = CoinGecko id), price in USD |
| Stocks | Copies the live `GOOGLEFINANCE` value (column D) into the snapshot |
| Writes | Column E price, F time (Halifax), G age = 0, H `✅ FRESH`; one row per price in `Price Log` |
| If a price fails | The old price stays; age is recomputed from F; over 13 h it shows `⏳ OUTDATED` |

## Why one hour before the slot

The slot is the decision moment. Refreshing one hour earlier leaves time for a failed fetch to show up, and still means the price is at most about 1 h old when the slot opens.

## How to read freshness at a slot

- `✅ FRESH` with a time from the last run (for example 09:0x at the 10:00 slot): use it.
- Up to 13 h old still counts as fresh enough (for example a slot that is checked late).
- `⏳ OUTDATED` (over 13 h): don't harvest on it. Check the live venue price (Binance, Lemon) first.
- Column G is written as 0 on every successful run and only grows when a fetch fails. Read the age from column F against the current time.
- Prices are management snapshots, not fills. The executed Convert receipt is the truth.

## Things to know

- Weekend stock prices come from GOOGLEFINANCE and are Friday's close. bStocks on Binance can trade at a slightly different price.
- The API key lives only in the live script (or in Script Properties). Never commit it.
- `price-updater.gs` in this folder is an earlier version (retries plus a CryptoCompare fallback). The script running in the book (as of 2026-10-24) is the simpler single-call version described above. Both keep the same schedule and the 13 h rule.

## Other scripts in this folder

| File | Runs | Does |
|---|---|---|
| [`candle-alert.gs`](candle-alert.gs) | Every hour | Live prices (CoinGecko for crypto, GOOGLEFINANCE for stocks). Adds every lot's excess per asset, checks the harvest ladder (step ≤ 50% of excess), and flags a move of 4% or more in an hour. Emails the script owner and logs to the `Alerts` tab. Repeats the same alert at most every 6 h. Install: `setupAlerts()`. |
| [`narrative-feed.gs`](narrative-feed.gs) | Daily 06:00 Halifax | Reads the YouTube RSS of Crypto Banter and Paul Barron Network into the `Narrative` tab (title, held assets mentioned, link, description). Install: `setupNarrative()`. |

Paste each into the same Apps Script project as a new file. They don't share function names with the price worker.

See also: [`protocols/catch-up-process.md`](../protocols/catch-up-process.md) (step 3) and [`protocols/harvest-ladder.md`](../protocols/harvest-ladder.md).
