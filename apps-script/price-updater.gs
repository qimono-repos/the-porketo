/**
 * The Porketo — price snapshot updater for the book (Google Sheet).
 *
 * Writes a price snapshot into the "Prices" tab every 6 hours at
 * 03:00, 09:00, 15:00, 21:00 Halifax (1 hour before each checkpoint).
 *   - crypto rows (Type = "crypto"): CoinGecko simple/price (retries on 429),
 *     then CryptoCompare by symbol for anything CoinGecko didn't return
 *   - stock rows  (Type = "stock"):  copies the live GOOGLEFINANCE value in column D
 * Column E = price snapshot, column F = timestamp of that snapshot.
 * If every source fails for a row, its old price and old timestamp are KEPT,
 * so it ages naturally and flips to "⏳ OUTDATED" after 13 h (formula in column H).
 * Every successful price is appended to the "Price Log" tab (with its source).
 *
 * Optional (recommended): free CoinGecko Demo API key, stored as a Script
 * Property named COINGECKO_DEMO_KEY (Project Settings → Script Properties).
 * Without it, Apps Script shares CoinGecko's anonymous quota with everyone
 * else on Google's servers and often gets HTTP 429.
 *
 * Install: Extensions → Apps Script → paste this file → save → run setup()
 * once and authorise. setup() creates the 4 daily triggers and runs one update.
 */

const PRICES_SHEET = 'Prices';
const LOG_SHEET = 'Price Log';
const RUN_HOURS = [3, 9, 15, 21];          // Halifax local time
const TZ = 'America/Halifax';

function setup() {
  ScriptApp.getProjectTriggers()
    .filter(t => t.getHandlerFunction() === 'updatePrices')
    .forEach(t => ScriptApp.deleteTrigger(t));
  RUN_HOURS.forEach(h =>
    ScriptApp.newTrigger('updatePrices')
      .timeBased().atHour(h).everyDays(1).inTimezone(TZ)
      .create());
  updatePrices();
}

function updatePrices() {
  const ss = SpreadsheetApp.getActive();
  const sh = ss.getSheetByName(PRICES_SHEET);
  const n = sh.getLastRow() - 1;
  if (n < 1) return;

  SpreadsheetApp.flush();                                    // let GOOGLEFINANCE settle
  const rows = sh.getRange(2, 1, n, 4).getValues();          // A Symbol, B Type, C Source ID, D Live
  const snap = sh.getRange(2, 5, n, 2).getValues();          // E Price, F Updated At

  // ---- crypto source 1: CoinGecko (one call, retries on 429 / 5xx) ----
  const ids = [...new Set(rows.filter(r => r[1] === 'crypto' && r[2]).map(r => r[2]))];
  const cg = ids.length ? fetchCoinGecko_(ids) : {};

  // ---- crypto source 2: CryptoCompare for symbols CoinGecko missed ----
  const missing = rows
    .filter(r => r[1] === 'crypto' && !(cg[r[2]] && cg[r[2]].usd))
    .map(r => String(r[0]));
  const cc = missing.length ? fetchCryptoCompare_(missing) : {};

  const now = new Date();
  const log = [];
  rows.forEach((r, i) => {
    let p = null, src = '';
    if (r[1] === 'crypto') {
      if (cg[r[2]] && cg[r[2]].usd) { p = cg[r[2]].usd; src = 'CoinGecko'; }
      else if (cc[r[0]] && cc[r[0]].USD) { p = cc[r[0]].USD; src = 'CryptoCompare'; }
    } else if (r[1] === 'stock') {
      if (typeof r[3] === 'number' && r[3] > 0) { p = r[3]; src = 'GOOGLEFINANCE'; }
    }
    if (p) {
      snap[i][0] = p;
      snap[i][1] = now;
      log.push([now, r[0], p, src]);
    } else {
      console.warn('No price for ' + r[0] + ' — keeping old snapshot');
    }
  });
  sh.getRange(2, 5, n, 2).setValues(snap);
  sh.getRange(2, 6, n, 1).setNumberFormat('yyyy-mm-dd hh:mm');

  let lg = ss.getSheetByName(LOG_SHEET);
  if (!lg) { lg = ss.insertSheet(LOG_SHEET); lg.appendRow(['Run at (Halifax)', 'Symbol', 'Price', 'Source']); }
  if (log.length) {
    lg.getRange(lg.getLastRow() + 1, 1, log.length, 4).setValues(log);
    lg.getRange(2, 1, lg.getLastRow() - 1, 1).setNumberFormat('yyyy-mm-dd hh:mm');
  }
}

function fetchCoinGecko_(ids) {
  const key = PropertiesService.getScriptProperties().getProperty('COINGECKO_DEMO_KEY');
  const url = 'https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=' +
              encodeURIComponent(ids.join(','));
  const opts = { muteHttpExceptions: true, headers: key ? { 'x-cg-demo-api-key': key } : {} };
  for (let attempt = 1; attempt <= 3; attempt++) {
    try {
      const res = UrlFetchApp.fetch(url, opts);
      const code = res.getResponseCode();
      if (code === 200) return JSON.parse(res.getContentText());
      console.warn('CoinGecko HTTP ' + code + ' (attempt ' + attempt + ')');
      if (code !== 429 && code < 500) break;
    } catch (e) {
      console.warn('CoinGecko error (attempt ' + attempt + '): ' + e);
    }
    Utilities.sleep(5000 * attempt);
  }
  return {};
}

function fetchCryptoCompare_(symbols) {
  const url = 'https://min-api.cryptocompare.com/data/pricemulti?tsyms=USD&fsyms=' +
              encodeURIComponent(symbols.join(','));
  try {
    const res = UrlFetchApp.fetch(url, { muteHttpExceptions: true });
    if (res.getResponseCode() === 200) {
      const j = JSON.parse(res.getContentText());
      if (!j.Response) return j;                 // error payloads carry a "Response" field
      console.warn('CryptoCompare: ' + (j.Message || 'error'));
    } else {
      console.warn('CryptoCompare HTTP ' + res.getResponseCode());
    }
  } catch (e) { console.warn('CryptoCompare error: ' + e); }
  return {};
}
