# MongoDB migration scaffold

This directory is the migration boundary for the-porketo's trading book.

The intended separation is:
- GitHub: strategy, rules, formulas, decisions, and code history.
- MongoDB Atlas: canonical operational state of the trading book after cutover.
- Binance: executable market/exchange state.
- Clojure server: controlled API/data-access boundary for humans and AI agents.

The current Google Sheet remains the source of truth until migration is explicitly approved. This scaffold does not import, mutate, or replace the live book.

## Layout

nosql/
  docs/MIGRATION-STRATEGY.md
  config/.env.example
  migrations/001-create-indexes.clj
  src/porketo/mongo/config.clj
  src/porketo/mongo/db.clj
  src/porketo/mongo/schema.clj
  src/porketo/mongo/repository.clj
  src/porketo/server.clj
  deps.edn

## Run

cd nosql
cp config/.env.example .env
clojure -M:run

Required configuration: MONGODB_URI and MONGODB_DATABASE.

## Migration principle

The first production milestone is dual-read validation, not cutover:
1. Freeze/export the current Sheet.
2. Normalize into candidate Mongo documents.
3. Load into a migration database.
4. Reconcile lots, balances, anchors, trades, and event sequence.
5. Replay harvest decisions.
6. Run parallel validation for several events.
7. Explicitly approve cutover.

MongoDB Atlas application connections require TLS, a database user, and appropriate network access configuration.