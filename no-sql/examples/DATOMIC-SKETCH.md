# Datomic sketch of the lot model

Written 2026-09-30, comparing MongoDB Atlas against Datomic (the Clojure/Datalog database, acquired by Nubank) as the backbone for this project. Companion to `LOT-ORCL-1.md` and `LOT-IDENTITY-AND-GROUPING.md`.

## The shift in shape

In MongoDB the lot is a **document** you read, mutate and write back.

In Datomic there is no lot document at all. You assert **facts** — `[entity attribute value transaction]` datoms — and the "lot" is simply the entity those facts hang off. Nothing is ever overwritten: asserting a new value for `:lot/net-units` does not erase the old one, it adds a fact that supersedes it as of that transaction.

The consequence for this project is large: **the `mark` almost disappears.** In Mongo we embed `{price, markedAt, source}` because the document only knows "now". In Datomic the price at a moment *is* what the database says as of that moment. You do not store a snapshot; you ask the database as of a point in time.

## Schema

Attributes, not tables. Each is declared once.

```clojure
[{:db/ident :lot/id
  :db/valueType :db.type/string
  :db/cardinality :db.cardinality/one
  :db/unique :db.unique/identity}

 {:db/ident :lot/ticker
  :db/valueType :db.type/string
  :db/cardinality :db.cardinality/one
  :db/index true}

 {:db/ident :lot/entry-price
  :db/valueType :db.type/bigdec
  :db/cardinality :db.cardinality/one
  :db/index true}

 {:db/ident :lot/opened-date
  :db/valueType :db.type/instant
  :db/cardinality :db.cardinality/one
  :db/index true}

 {:db/ident :lot/material-anchor
  :db/valueType :db.type/bigdec
  :db/cardinality :db.cardinality/one}

 {:db/ident :lot/target-profit
  :db/valueType :db.type/bigdec
  :db/cardinality :db.cardinality/one}

 {:db/ident :lot/net-units
  :db/valueType :db.type/bigdec
  :db/cardinality :db.cardinality/one}

 {:db/ident :lot/status
  :db/valueType :db.type/keyword
  :db/cardinality :db.cardinality/one}

 {:db/ident :lot/sprint
  :db/valueType :db.type/ref
  :db/cardinality :db.cardinality/one}

 {:db/ident :lot/thesis
  :db/valueType :db.type/string
  :db/cardinality :db.cardinality/one}]
```

Note `:db/unique :db.unique/identity` on `:lot/id`, and indexes on the three natural-key components — ticker, entry price, opened date — for the same reason as in Mongo: grouping by different criteria must stay cheap.

`bigdec` is the correct choice for money and units, matching the `$numberDecimal` decision already made for `stock-trades.json`.

## Asserting ORCL Lot 1

```clojure
[{:lot/id              "LOT-ORCL-1"
  :lot/ticker          "ORCL"
  :lot/entry-price     157.18M
  :lot/opened-date     #inst "2026-09-10"
  :lot/material-anchor 15.00M
  :lot/target-profit   0.10M
  :lot/net-units       0.095432M
  :lot/status          :status/open
  :lot/thesis          "Earnings exposure"}]
```

The later harvest (TRD-0009) is a separate transaction:

```clojure
[[:db/add [:lot/id "LOT-ORCL-1"] :lot/net-units 0.092152M]]
```

The 0.095432 fact is **not deleted**. It remains true as of its transaction. This is the property that makes the event log and the lot projection collapse into one thing — there is no separate "rebuild from events" step, because history is the database.

## Queries

Current open lots for a ticker:

```clojure
[:find ?id ?units ?anchor
 :in $ ?ticker
 :where
 [?l :lot/ticker ?ticker]
 [?l :lot/status :status/open]
 [?l :lot/id ?id]
 [?l :lot/net-units ?units]
 [?l :lot/material-anchor ?anchor]]
```

First three ORCL lots by date, lots near a price, lots opened in a date range — all the groupings from `LOT-IDENTITY-AND-GROUPING.md` are ordinary Datalog clauses over the indexed attributes, plus predicates like `[(>= ?price 149.0M)]`.

### Time travel — the reason to consider this at all

```clojure
;; what the book looked like on 15 September
(d/as-of db #inst "2026-09-15")

;; every value :lot/net-units has ever held, with timestamps
[:find ?units ?tx-time
 :where
 [[:lot/id "LOT-ORCL-1"] :lot/net-units ?units ?tx]
 [?tx :db/txInstant ?tx-time]]
```

`as-of` returns an immutable database value you query exactly like the present one. No special "history table", no snapshot discipline to maintain by hand. `d/since` and `d/history` give the complementary views.

## Honest assessment

**For this project**
- Immutable ledger, nothing overwritten — matches the event-sourcing design already chosen.
- `as-of` is the snapshot philosophy, built in rather than hand-rolled.
- Auditability: every fact carries the transaction that asserted it and when.
- Nubank — a bank — acquired Datomic outright. Strong signal for financial use.
- Clojure is the operator's favourite language.

**Against**
- Datalog and Clojure are a steeper climb than Mongo queries.
- Hosting is more involved than Atlas.
- **No built-in semantic/vector search.** Atlas Vector Search covers the AI side in one system; with Datomic that needs a second store.
- Smaller ecosystem, fewer off-the-shelf integrations.

**The trade, stated plainly:** Datomic wins on time travel and auditability; Atlas wins on semantic search and lower effort. Choose based on which of those two the project needs first.
