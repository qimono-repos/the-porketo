# Gemini Market Intelligence Inbox

**Owner / contributor:** Gemini  
**Project:** Qimono / the-porketo  
**Prepared by:** ChatGPT from Albert's supplied ticker universe  
**Date initialized:** 2026-11-02  
**Purpose:** A durable research handoff for Gemini contributions that ChatGPT can ingest, validate, and relay to GitHub and Slack.

> **Source-of-truth boundary:** This is a research watchlist, not a holdings ledger. The supplied prices, lot labels, exchange annotations and repeated entries were intentionally removed. Each symbol appears once. Do not infer current holdings, position sizes, average costs or transaction status from this list.

## 1. Research universe

### Equities, ETFs and equity-linked / tokenized instruments (29 unique tickers)

`AAPL, IONQ, ORCL, AVGO, QBTS, FLKR, NVDA, CVX, OKLO, HOOD, BLK, DUK, TSLAB, SPCXB, IBMB, QBTSB, DUKB, HOODB, TSMB, MUB, NVDAB, QNTB, RGTI, QUBT, INFQ, XNDU, PSQL, AMDB, MDB`

### Cryptoassets (19 unique tickers)

`ETH, LINK, AAVE, IMX, RONIN, TAO, PUMP, ZEC, BTC, SOL, SUI, NEAR, SLP, GALA, ILV, DOT, ALGO, AXS, SAND`

**Total coverage: 48 unique symbols.**

## 2. Gemini's research responsibilities

For each research cycle, prioritize useful new information rather than repeating unchanged data.

### A. YouTube creator and video intelligence

Find relevant, credible YouTube channels and videos covering the stock, company, ETF, token, protocol or sector represented by the watchlist.

For each useful video, capture:

- Ticker(s) and company/project covered.
- Video title, creator/channel, publication date and direct URL.
- Relevant timestamps and transcript excerpts or accurate paraphrases.
- Main thesis, expected catalyst, time horizon and stated risks.
- Whether the creator is reporting facts, offering analysis, speculating, promoting a position, or disclosing sponsorship/holdings.
- What is genuinely new versus what is already known.
- Any material disagreement with other creators or Qimono's existing research.

Prefer recent, substantive videos and primary-source recordings (earnings calls, investor presentations, interviews, conference talks and technical demonstrations). Include independent creators where their analysis adds value. Do not rank credibility by views or subscriber count alone. Do not treat a creator's prediction as verified fact.

Avoid producing one low-value video summary per ticker merely to fill coverage. Prioritize videos with meaningful catalyst or thesis relevance, and explicitly report when no useful recent video is found.

### B. Google Finance and Yahoo Finance

For every supported listed security or fund, check Google Finance and Yahoo Finance where available.

Capture:

- Exact instrument identity, exchange and currency.
- Latest displayed price and percentage change.
- Quote timestamp or page/update timestamp, with timezone when available.
- Volume and market capitalization where the source provides them.
- Relevant performance period (1D, 5D, 1M, 6M, YTD, 1Y, etc.).
- Direct source URL.
- Differences or data gaps between Google Finance and Yahoo Finance.

Do not claim that a value is real-time unless the source explicitly identifies it as real-time. Record delayed quotes as delayed. Never invent a missing quote or market metric.

### C. Instrument identity and symbol validation

Some supplied tickers may be tokenized stock wrappers, exchange-specific instruments, ETFs, funds or ambiguous symbols.

For each symbol, resolve:

- Full issuer / asset name.
- Instrument type.
- Primary listing or underlying reference, if any.
- Exchange and currency.
- Whether Google Finance supports it.
- Whether Yahoo Finance supports it.
- Whether a Binance wrapper or other tokenized instrument is involved.

Never assume that a ticker with a suffix is the same security as the unsuffixed ticker. Never silently map an unsupported wrapper to an underlying share. If an instrument cannot be identified confidently, mark it **unresolved** and explain why.

For cryptoassets, identify the network / project and the quote currency. Use Google Finance or Yahoo Finance only where the asset is genuinely supported; otherwise identify the source gap and use a reputable direct market-data source as a clearly labelled fallback.

## 3. Recommended report structure

Each update should begin:

`## YYYY-MM-DD HH:MM UTC | Gemini Market Intelligence Update`

Then include:

1. **Executive summary:** 3–7 genuinely new or decision-relevant findings.
2. **YouTube intelligence:** creator/video summaries with timestamps and links.
3. **Finance-source snapshot:** Google Finance and Yahoo Finance observations, clearly timestamped.
4. **Ticker identity exceptions:** unsupported, ambiguous, wrapped or mismatched symbols.
5. **Catalysts and calendar:** upcoming earnings, events, unlocks, economic releases or other dated catalysts.
6. **Bull / bear disagreement:** strongest supporting and opposing evidence.
7. **Qimono decision relevance:** what changed, what might matter, and what would invalidate the thesis. Do not issue an automatic buy/sell instruction.
8. **Cross-model handoff:** what ChatGPT, Grok or Claude should investigate next.
9. **Sources:** direct URLs and publication / observation timestamps.

Use tables where they improve comparison. Keep the raw source evidence separate from Gemini's interpretation.

## 4. Update and relay protocol

This inbox is intended to be updated by Gemini. Add new dated sections; do not overwrite previous updates.

When Gemini adds a meaningful update:

1. Mark the section clearly as authored by Gemini.
2. Include source URLs, timestamps and ticker references.
3. Distinguish new facts from previously reported information.
4. State any uncertainty or source conflict.
5. Identify the intended recipient and the next action.
6. Preserve earlier entries.

**ChatGPT relay workflow:** When a new Gemini update becomes available through a connected and authorized shared source, ChatGPT should read it, validate material factual claims and links, append a clearly attributed Gemini handoff to the shared Qimono conversation log in GitHub, and post a concise Slack relay in `#trading` (channel `C0CD1U79YTH`) under the active daily thread. ChatGPT must identify itself as the relayer, preserve Gemini's authorship, link the source document and GitHub commit, and never make a post appear to have been written by Gemini if ChatGPT sent it.

If a Google Drive document is used as the source, retain its canonical link in each relay. If Drive access is unavailable to ChatGPT, Gemini should additionally publish or copy the dated handoff into an agreed accessible bridge (GitHub or Slack) so the relay does not depend on manual transcription.

Do not relay unchanged sections, duplicate updates or unsupported claims. Do not infer trades or holdings from this research watchlist.

## 5. Initial ticker deduplication record

The source lists supplied by Albert included repeated symbols from multiple lots, price references and exchange annotations. These were consolidated by ticker only:

- Equity / ETF / equity-linked list: 29 unique symbols.
- Crypto list: 19 unique symbols.
- Total: 48 unique symbols.

Prices, lot labels, and annotations such as `(Binance)`, `(recon)` and `(Lemon)` were excluded from the research universe. They are not current quote data and must not be reused as such.

## 6. Current setup status

- Research universe deduplicated and initialized.
- GitHub interim inbox established.
- Slack relay to be announced in the active `#trading` daily thread.
- Google Drive / Google Docs source document: **not yet created from ChatGPT**, because the Google Drive connector is disabled by workspace administration in this environment.
- Next step: Gemini creates the Google Doc in its connected Google environment (or Albert enables an authorized Drive connector for ChatGPT), then the canonical document link is added here and used for subsequent ingestion and relays.


## 7. Required Drive-to-Slack ingestion bridge

The Google Doc should remain Gemini's canonical working document. Do not make it public solely to enable ChatGPT ingestion.

Because ChatGPT's Google Drive connector is currently disabled by workspace administration, Gemini must mirror every meaningful dated research update into the active daily thread in Slack #trading (channel C0CD1U79YTH), along with the canonical Google Doc link and update timestamp. Include enough of the actual research findings, source URLs, quote timestamps and YouTube timestamps in Slack for ChatGPT to validate and ingest the update; a private Drive link alone is not sufficient.

After the Slack mirror appears, ChatGPT can:
1. Read the Gemini-authored Slack update.
2. Preserve Gemini's attribution and source evidence.
3. Validate material claims and quote timestamps.
4. Append a dated, clearly attributed Gemini section to this inbox / shared GitHub conversation log.
5. Post a concise relay/confirmation in the same Slack thread with the GitHub commit link.

This is the intended operating loop until an authorized Google Drive connector becomes available to ChatGPT. Never grant public Drive access merely for convenience. Keep Drive sharing limited to the intended Qimono collaborators.
