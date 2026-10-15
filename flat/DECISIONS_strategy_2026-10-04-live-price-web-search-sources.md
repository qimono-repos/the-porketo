# Decision: Live Decision-Reference Prices Come From a Web Search (Named Aggregator Sources)

- **Date:** 2026-10-04
- **Status:** Active standing rule
- **Scope:** Decision-reference ("directional context") prices only. Booked
  execution values are unaffected — they still come ONLY from the real Binance
  receipt for the instrument actually traded.

## Decision

When a live price is needed for decision reference (deciding or monitoring), and
no Binance MCP / connector is wired in yet, the price is obtained via a **web
search**, not a direct exchange feed. The search returns public aggregator /
exchange pages. The audit trail must record that the figure came from a web
search and name the source used, with its URL.

## Sources seen in the web-search results

These are the aggregator and exchange pages the web search surfaces for a crypto
live price. Any figure used for a decision must cite which one it came from:

- CoinMarketCap — https://coinmarketcap.com/currencies/near-protocol/
- CoinGecko — https://www.coingecko.com/en/coins/near
- Coinbase — https://www.coinbase.com/price/near-protocol
- Binance — https://www.binance.com/en/price/near-protocol
- Kraken — https://www.kraken.com/prices/near-protocol
- Yahoo Finance — https://finance.yahoo.com/quote/NEAR-USD/
- CoinDesk — https://www.coindesk.com/price/near-protocol
- TradingView — https://www.tradingview.com/symbols/NEARUSD/
- CoinCodex — https://coincodex.com/crypto/near-protocol/
- Crypto.com — https://crypto.com/en/price/near-protocol

(The NEAR URLs above are the concrete example; the same providers serve other
tickers at the equivalent path.)

## Why

- Honesty of the audit chain: SOURCE -> TIMESTAMP -> DATA -> CALCULATION ->
  INTERPRETATION. "Web search" is a materially weaker source than a direct
  exchange feed and must be labelled as such, never passed off as a live Binance
  mark.
- The aggregators **disagree**, sometimes widely. In the 2026-10-04 NEAR check,
  most sources clustered ~4.63–4.81 USD (CoinGecko 4.63, CoinMarketCap 4.64,
  Coinbase 4.76, Kraken 4.81), while outliers (CoinCodex 1.89, CoinDesk 2.59 as
  a stale 2026-09-16 print, Binance page 5.38) sat far off. The decision-maker
  must take the cluster, treat outliers with suspicion, and record which figure
  was used.
- Fail closed: if the sources cannot be reconciled into a confident figure and
  the number would change the decision, do not book or act on it — wait for a
  trustworthy price.

## Related

- DECISIONS/strategy/2026-10-03-price-reference-protocol.md — the parent protocol
  (two uses of price; Yahoo now / Binance later; drop-the-trailing-B mapping).
  This record supplies the concrete source list and URLs for the "web search"
  step named there.
