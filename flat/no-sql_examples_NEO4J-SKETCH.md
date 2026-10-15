# Neo4j sketch of the lot model

Written 2026-09-30. Third option alongside `LOT-ORCL-1.md` (MongoDB) and `DATOMIC-SKETCH.md` (Datomic).

## The shift in shape

Mongo asks *what is a lot?* Datomic asks *what facts are true about a lot, and when?* Neo4j asks *what is a lot connected to?*

The consequence: things that were **fields** become **nodes**. `ticker`, `sprintId` and `thesis` were attributes inside the lot document. In a graph they are first-class nodes, and the meaning moves into the relationships between them.

## Node labels

- `(:Lot)` — the aggregate, as before: `id`, `entryPrice`, `openedDate`, `materialAnchor`, `targetProfit`, `netUnits`, `status`
- `(:Asset)` — `ticker`, `name`, `assetClass` (stock / crypto)
- `(:Sprint)` — `id`, `startDate`, `endDate`, `budget`
- `(:Event)` — `id`, `executedAt`, `action`, `units`, `cashFlow` — the ledger rows from `stock-trades.json`
- `(:Thesis)` — `name` ("Earnings exposure", "AI infrastructure", "Musk-linked tech")
- `(:Sector)` — `name` (quantum computing, energy, utilities, …)
- `(:Mark)` — `price`, `markedAt`, `source`

## Relationships

```
(:Lot)-[:TRACKS]->(:Asset)
(:Lot)-[:BELONGS_TO]->(:Sprint)
(:Lot)-[:OPENED_BY]->(:Event)
(:Lot)-[:AFFECTED_BY]->(:Event)
(:Lot)-[:MARKED_AT]->(:Mark)
(:Lot)-[:JUSTIFIED_BY]->(:Thesis)
(:Asset)-[:IN_SECTOR]->(:Sector)
(:Asset)-[:CORRELATED_WITH {coefficient}]->(:Asset)
```

`CORRELATED_WITH` is the one that does not exist in either other model, and it is the reason to consider a graph at all — see "diversification" below.

## Creating ORCL Lot 1

```cypher
MERGE (a:Asset {ticker: "ORCL"})
MERGE (s:Sprint {id: "SPRINT-2026-09-15"})
MERGE (t:Thesis {name: "Earnings exposure"})

CREATE (l:Lot {
  id: "LOT-ORCL-1",
  label: "ORCL Lot 1 @ 157.18",
  entryPrice: 157.18,
  openedDate: date("2026-09-10"),
  materialAnchor: 15.00,
  targetProfit: 0.10,
  netUnits: 0.092152,
  status: "OPEN"
})

CREATE (l)-[:TRACKS]->(a)
CREATE (l)-[:BELONGS_TO]->(s)
CREATE (l)-[:JUSTIFIED_BY]->(t)
```

The natural key still lives as three indexed properties — `TRACKS` gives the ticker, plus `entryPrice` and `openedDate` on the node.

## Queries

### The groupings, unchanged in spirit

```cypher
// first three ORCL lots by date
MATCH (l:Lot)-[:TRACKS]->(:Asset {ticker: "ORCL"})
RETURN l ORDER BY l.openedDate ASC LIMIT 3

// ORCL lots near 157
MATCH (l:Lot)-[:TRACKS]->(:Asset {ticker: "ORCL"})
WHERE l.entryPrice >= 149.0 AND l.entryPrice <= 165.0
RETURN l
```

Comparable to Mongo. No advantage here.

### What only a graph makes easy

```cypher
// every lot opened for the same reason, across tickers
MATCH (l:Lot)-[:JUSTIFIED_BY]->(t:Thesis {name: "AI infrastructure"})
MATCH (l)-[:TRACKS]->(a:Asset)
RETURN a.ticker, l.id, l.materialAnchor

// the Musk sleeve: how TSLA and SPCX connect
MATCH path = (a:Asset {ticker: "TSLAB"})-[*1..3]-(b:Asset {ticker: "SPCXB"})
RETURN path

// concentration risk: am I accidentally over-exposed to one sector?
MATCH (l:Lot {status: "OPEN"})-[:TRACKS]->(:Asset)-[:IN_SECTOR]->(s:Sector)
RETURN s.name, sum(l.materialAnchor) AS exposure
ORDER BY exposure DESC

// diversification: assets NOT correlated with anything I already hold
MATCH (held:Asset)<-[:TRACKS]-(:Lot {status: "OPEN"})
MATCH (candidate:Asset)
WHERE NOT (candidate)-[:CORRELATED_WITH]-(held)
  AND NOT (candidate)<-[:TRACKS]-(:Lot {status: "OPEN"})
RETURN candidate.ticker
```

That last query is the live research question in `PROJECT_STATE.md` — *find stock names uncorrelated with AI* — expressed directly as a traversal.

## Honest assessment

**For**
- Turns the diversification and correlation questions into queries rather than judgement calls.
- Thesis and sector become navigable, connecting decisions across tickers and time.
- Natural fit for the knowledge-graph side of the project, where CONVERSATIONS, DECISIONS and INSIGHTS already cross-reference each other.
- Neo4j supports vector indexes, so semantic search is possible in the same store.

**Against**
- **Weakest of the three as a ledger.** No immutability guarantee, no `as-of`. History must be modelled by hand — the opposite of Datomic's main strength.
- Aggregate boundaries blur. It is easy to write a query that quietly spans lots and breaks the "never blend material anchors" rule.
- Correlation data must come from somewhere; the `CORRELATED_WITH` edges need computing and maintaining.
- Heavier to operate than Atlas for a single-operator project.

## The three compared

| | MongoDB Atlas | Datomic | Neo4j |
|---|---|---|---|
| Aggregate fit | Excellent — document = aggregate | Good | Blurry |
| Ledger / audit | Manual (append-only by discipline) | **Built in** — nothing overwritten | Weak |
| Time travel | Hand-rolled snapshots | **`as-of`, free** | Hand-rolled |
| Grouping by ticker / price / date | Good | Good | Good |
| Relationship questions | Awkward | Awkward | **Excellent** |
| Semantic / vector search | **Atlas Vector Search** | None built in | Vector indexes |
| Effort for one operator | **Lowest** | Highest | Medium-high |

**Reading:** the three optimise for different things this project genuinely wants — Atlas for low effort plus semantic search, Datomic for the immutable audited ledger, Neo4j for correlation and diversification reasoning. A plausible end state is Atlas or Datomic as the book of record, with a graph derived from it for research questions rather than as the primary store.
