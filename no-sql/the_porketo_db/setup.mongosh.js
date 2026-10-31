// Creates (or updates) the_porketo_db.trades with its validator and indexes.
// Safe to run more than once.
//
//   mongosh "$MONGODB_URI" --file no-sql/the_porketo_db/setup.mongosh.js
//
// Run from the repo root so the validator path below resolves.

const validator = JSON.parse(fs.readFileSync('no-sql/the_porketo_db/trades.validator.json', 'utf8'));
const db_ = db.getSiblingDB('the_porketo_db');

if (db_.getCollectionNames().includes('trades')) {
  db_.runCommand({ collMod: 'trades', validator, validationLevel: 'strict', validationAction: 'error' });
  print('trades: validator updated');
} else {
  db_.createCollection('trades', { validator, validationLevel: 'strict', validationAction: 'error' });
  print('trades: created');
}

db_.trades.createIndex({ executedAt: -1 }, { name: 'executedAt_desc' });
db_.trades.createIndex({ asset: 1, executedAt: -1 }, { name: 'asset_executedAt' });
db_.trades.createIndex({ assetClass: 1, executedAt: -1 }, { name: 'assetClass_executedAt' });
db_.trades.createIndex({ lotId: 1 }, { name: 'lotId' });
db_.trades.createIndex({ 'slots.first': 1 }, { name: 'slots_first' });
print('trades: indexes ensured');
printjson(db_.trades.getIndexes().map(i => i.name));
