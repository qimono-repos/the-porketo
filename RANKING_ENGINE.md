# Ranking Engine

**Status:** Functional specification / fixed-universe exercise  
**Purpose:** Define a deterministic, explainable ranking function that selects ten investment-opportunity candidates for a Polly poll.  
**Scope:** Ranking logic and poll payload design only. Live market-data ingestion, dynamic universe churn, scheduling, and Polly API calls are deliberately deferred.

## 1. Objective and rationale

The engine answers:

> Given an eligible candidate universe, which ten assets currently present the strongest observable trading opportunities?

This is an opportunity-screening and human-preference collection system. It is not a portfolio allocator, execution engine, personalized financial adviser, or prediction guarantee. A high score means the observed signals look comparatively attractive under the configured model. It does not mean the asset is safe, undervalued, or certain to rise.

Every Polly poll is a time-stamped snapshot. We create a new poll on each run and preserve previous polls and their results. This makes it possible to compare participants' preferences across successive snapshots without destroying history.

## 2. Fixed exercise universe

For the Polly functionality exercise, use this fixed set of ten symbols selected from the supplied Porketo portfolio:

| Symbol | Asset family | Inclusion rationale |
|---|---|---|
| BTC | Crypto / large-cap | Liquid crypto-market benchmark and reference asset |
| ETH | Crypto / large-cap | Major smart-contract ecosystem exposure |
| SOL | Crypto / large-cap | Higher-beta smart-contract ecosystem exposure |
| LINK | Crypto / infrastructure | Oracle and interoperability infrastructure exposure |
| TAO | Crypto / AI | AI-related crypto narrative and higher-volatility exposure |
| AVGO | Equity / semiconductors | Technology infrastructure and semiconductor exposure |
| NVDA | Equity / semiconductors | AI compute and semiconductor exposure |
| IONQ | Equity / quantum computing | Publicly traded quantum-computing exposure |
| QBTS | Equity / quantum computing | Publicly traded quantum-computing exposure |
| RGTI | Equity / quantum computing | Publicly traded quantum-computing exposure |

This is a **deliberately selected test basket**, not a claim that these are the ten highest-scoring assets under current market conditions. No live market data is used for this exercise. The basket gives the Polly workflow a stable mix of asset families so that poll creation, choice formatting, and result retrieval can be designed independently of live candidate churn.

For this fixed exercise, the universe contains exactly these ten assets, so all ten are poll choices in the listed order. When dynamic selection is introduced, expand the universe to the broader portfolio list and apply the same scoring interface to choose the top ten.

### Symbol normalization

Keep a canonical portfolio symbol internally and an explicit provider-symbol mapping for each market-data source. A provider may represent an asset as a pair, with a venue suffix, or with a different equity class notation. Never silently assume that the provider symbol is identical to the portfolio ticker.

## 3. Scoring model

The opportunity score is a weighted sum of six normalized features. Each feature is in the range 0–100, where higher means more attractive under this model.

| Feature | Weight | Rationale |
|---|---:|---|
| Short-term momentum | 25% | Finds assets already moving over actionable short horizons |
| Relative strength | 20% | Distinguishes assets outperforming the relevant market benchmark |
| Volume acceleration | 20% | Looks for increasing participation behind a move |
| Trend confirmation | 15% | Rewards agreement across short and medium lookbacks |
| Liquidity | 10% | Favours assets that can be entered/exited with less friction |
| Risk quality | 10% | Avoids automatically rewarding disorderly or extreme volatility |
| **Total** | **100%** | |

Momentum receives the largest weight because the stated objective is trading opportunity rather than long-term fundamental quality. Relative strength and volume acceleration help distinguish a broadly rising market from an asset-specific move with participation. Trend confirmation reduces dependence on a single candle or interval. Liquidity and risk quality act as practical constraints.

These weights are initial policy choices, not proven predictive coefficients. They must be tested against historical data and adjusted only through recorded, out-of-sample evaluation.

### 3.1 Raw input measures

Use consistent windows and data definitions across candidates:

- `r4h`: log return over the latest four-hour interval.
- `r24h`: log return over the latest 24 hours.
- `r7d`: log return over the latest seven days.
- `benchmark-r24h`: benchmark log return over the latest 24 hours.
- `volume-ratio`: recent rolling volume divided by the comparable historical baseline.
- `adv`: average daily traded notional, or a documented provider-equivalent liquidity measure.
- `spread-bps`: estimated bid/ask spread in basis points.
- `realized-vol`: realized volatility over a fixed recent window.

Log return is defined as `ln(close_now / close_then)`. Missing or stale measurements must not be replaced with zero. Zero means neutral performance; missing means unknown.

### 3.2 Normalization

Raw data uses different units and distributions. Convert it to a common 0–100 scale before applying weights.

For a feature where larger values are better, use its percentile rank among the eligible candidates:

`score(x) = 100 * percentile_rank(x)`

For a feature where smaller values are better:

`score(x) = 100 * (1 - percentile_rank(x))`

Use average ranks for ties, and define percentile-rank behaviour consistently in every implementation. These scores are relative to the current candidate universe. They are not probabilities and are not comparable across universes without qualification.

Suggested first-version feature construction:

- **Momentum (M):** percentile score of `0.6 * r4h + 0.4 * r24h`.
- **Relative strength (RS):** percentile score of `r24h - benchmark-r24h`.
- **Volume acceleration (VA):** percentile score of `ln(volume-ratio)`. A ratio above 1 means volume is above baseline.
- **Trend confirmation (TC):** `100 * (number of positive returns among r4h, r24h, r7d) / 3`. This simple rule gives 0, 33.3, 66.7, or 100.
- **Liquidity (LQ):** average of the percentile score of `ln(adv)` and the inverse percentile score of `spread-bps`.
- **Risk quality (RQ):** start with the inverse percentile score of realized volatility, after applying a hard maximum-volatility eligibility rule. A later version may use a preferred volatility band rather than assuming lower is always better.

Momentum and relative strength are correlated by construction. Their separate weights are intentional: one rewards absolute movement, the other rewards movement beyond the benchmark. This relationship should be checked during calibration to avoid excessive double-counting.

### 3.3 Composite score

For each eligible asset `i`:

`score(i) = 0.25*M(i) + 0.20*RS(i) + 0.20*VA(i) + 0.15*TC(i) + 0.10*LQ(i) + 0.10*RQ(i)`

All components are in `[0, 100]`, so the composite score is also in `[0, 100]`.

Sort by:
1. Composite score descending.
2. Liquidity feature descending.
3. Canonical symbol ascending.

Take the first ten eligible candidates. The final alphabetical tie-break makes the same data and configuration produce the same ordered result in every implementation.

### 3.4 Eligibility filters

Apply eligibility rules before ranking. Example rules:

- Required price or candle data is missing or stale.
- Asset is suspended, inactive, or unavailable on the configured venue.
- Liquidity is below a configured minimum.
- Bid/ask spread exceeds a configured maximum.
- Realized volatility exceeds a configured risk ceiling.
- Provider-symbol mapping is ambiguous.
- Data-quality checks detect invalid prices, duplicate candles, or timestamp inconsistencies.

Do not silently fill the top ten with ineligible assets. If fewer than ten pass, return the available set with status `insufficient-eligible-assets`. The publishing policy must explicitly decide whether to skip that poll or publish fewer than ten choices.

## 4. Clojure-friendly configuration

Keep weights and field names as plain data so the implementation can be translated to Clojure, EDN, JSON Schema, or another schema-oriented language.

### 4.1 Configuration

```clojure
(def ranking-config
  {:version "1.0"
   :objective :trading-opportunity
   :selection-count 10
   :weights
   {:momentum          0.25
    :relative-strength 0.20
    :volume-accel      0.20
    :trend-confirm     0.15
    :liquidity         0.10
    :risk-quality      0.10}
   :tie-breakers [:score-desc :liquidity-desc :symbol-asc]})
```

### 4.2 Candidate data shape

Separate raw observations, normalized features, eligibility, and presentation fields:

```clojure
{:symbol "BTC"
 :asset-class :crypto
 :price nil
 :change-24h-pct nil
 :observed-at nil
 :raw
 {:return-4h nil
  :return-24h nil
  :return-7d nil
  :benchmark-return-24h nil
  :volume-ratio nil
  :average-daily-notional nil
  :spread-bps nil
  :realized-volatility nil}
 :features
 {:momentum nil
  :relative-strength nil
  :volume-accel nil
  :trend-confirm nil
  :liquidity nil
  :risk-quality nil}
 :eligible? false
 :exclusion-reasons []
 :score nil
 :rank nil}
```

Nil values in this schema are intentional placeholders. A production run must populate or explicitly reject missing values. Do not coerce them to zero.

### 4.3 Composite formula in Clojure

```clojure
(def required-features
  [:momentum :relative-strength :volume-accel
   :trend-confirm :liquidity :risk-quality])

(defn valid-features? [features]
  (every?
    (fn [k]
      (let [v (get features k)]
        (and (number? v) (<= 0.0 (double v) 100.0))))
    required-features))

(defn composite-score [weights features]
  (when-not (valid-features? features)
    (throw (ex-info "Missing or invalid ranking feature"
                    {:features features})))
  (reduce
    (fn [total feature]
      (+ total (* (double (get weights feature))
                  (double (get features feature))))
    0.0
    required-features))
```

Selection can then be expressed as a pure transformation:

```clojure
(defn rank-candidates [candidates config]
  (->> candidates
       (filter :eligible?)
       (map (fn [candidate]
              (assoc candidate :score
                     (composite-score (:weights config)
                                      (:features candidate)))))
       (sort-by (fn [c]
                  [(- (:score c))
                   (- (get-in c [:features :liquidity]))
                   (:symbol c)]))
       (take (:selection-count config))
       vec))
```

The pure function makes the model straightforward to unit-test. Data retrieval, timestamp validation, normalization, persistence, and Polly publishing remain outside the scoring function.

## 5. Schema contract

A JSON Schema or equivalent validator should enforce:

- `symbol`: non-empty string.
- `assetClass`: enumerated string.
- `observedAt`: ISO-8601 timestamp.
- `price`: positive number when market data is available.
- `change24hPct`: number when market data is available.
- Every normalized feature: number in `[0, 100]`.
- `eligible`: boolean.
- `exclusionReasons`: array of strings.
- `score`: number in `[0, 100]`, present only after valid feature calculation.
- Config weights: non-negative numbers summing to 1 within a defined floating-point tolerance.
- `selectionCount`: positive integer.

Keep the schema language-neutral. Clojure maps, JSON payloads, and database records should share the same semantic fields even if their naming conventions differ.

## 6. Polly choice formatting

The ranking engine returns structured candidates. The Polly adapter converts each candidate into a choice string. Do not fabricate prices for the fixed exercise.

Static exercise format:

`BTC | price: pending | 24h: pending`

Future live-data format:

`BTC | $67,420 | +2.4%`

The numbers above are illustrative only. All choices in one poll must use the same quote currency and the same percentage-change window. Include the observation time in the poll question or description so participants know when the snapshot was taken.

Suggested question:

`Which asset presents the most interesting opportunity right now?`

Suggested initial poll settings:

- Single choice for a clean signal of each participant's strongest preference.
- Disable voter-added choices because the candidate set is controlled by the ranking engine.
- Comments off initially; enable them later only if qualitative explanations are useful.
- Create a new poll on each run; do not overwrite prior poll snapshots.
- Preserve the poll ID and the exact choices sent to Polly.

If the intended question changes to “which assets interest you?”, multiple choice may be appropriate. That produces a different measurement: multi-select interest rather than a single strongest pick.

## 7. Poll-run history

Persist each run independently. A run record should include:

- `pollRunId`
- `createdAt` and `observedAt`
- `rankingConfigVersion`
- Universe identifier and universe snapshot
- All eligible candidate features, scores, and ranks
- Selected ten symbols and exact display strings
- Display price and 24-hour change, when available
- Polly poll ID and Slack channel ID
- Poll settings and publish status
- Results and result-retrieval timestamp

Store all scored candidates, not only the ten published choices. This supports later investigation of near-misses, ranking stability, and selection bias.

Votes and market performance are separate measurements. Votes capture participant preference; forward returns capture subsequent market behaviour. Do not treat poll popularity as proof of predictive quality.

## 8. Evaluation and calibration

When historical/live data is introduced, evaluate the model with walk-forward testing:

1. Calculate each historical ranking using only information available at that timestamp.
2. Measure subsequent returns over fixed horizons such as 4h, 24h, and 7d.
3. Compare top-ten results with the eligible universe and a relevant benchmark.
4. Track volatility, maximum adverse excursion, turnover, and concentration by asset family.
5. Check risk-adjusted outcomes, not only upside outliers.
6. Version every weight change and evaluate it out of sample before adoption.

Avoid look-ahead bias: a ranking at time `t` must not use information published after `t`. Include fees, spreads, and realistic execution assumptions in return evaluation.

## 9. Polly integration boundary

For this phase, Polly is the publishing and voting interface, not the ranking engine.

The adapter needs to:

1. Create a new poll from the fixed ordered list of choice strings.
2. Record the returned Polly poll ID and Slack destination.
3. Retrieve results for that specific poll.
4. Store results alongside the corresponding ranking snapshot.

The four-hour scheduler, live candidate churn, data provider selection, and exact production API/MCP implementation are outside this specification. Before implementing the adapter, verify Polly's actual choice limits, choice schema, publishing confirmation flow, recurring-poll behaviour, and result response shape against the connected workspace. Do not assume a separate visual category field exists if the API accepts only choice text.

## 10. Fixed exercise state

- Universe: BTC, ETH, SOL, LINK, TAO, AVGO, NVDA, IONQ, QBTS, RGTI.
- Selection: fixed; no live re-ranking.
- Price and percentage change: pending placeholders; no fabricated market values.
- Poll creation: new poll per run.
- Four-hour automation: intended design, not activated here.
- Dynamic universe churn: explicitly deferred to a separate design conversation.
- Weights: initial model requiring empirical calibration.

This fixed fixture isolates Polly's creation, display, publishing, and results functionality from market-data engineering.