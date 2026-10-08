/**
 * The Porketo — price snapshot updater for the book (Google Sheet).
 *
 * Writes a price snapshot into the "Prices" tab every 6 hours at
 * 03:00, 09:00, 15:00, 21:00 Halifax (1 hour before each checkpoint).
 *   - crypto rows (Type = "crypto"): CoinGecko simple/price, USD, one call
 *   - stock rows  (Type = "stock"):  copies the live GOOGLEFINANCE value in column D
 * Column E = price snapshot, column F = timestamp of that snapshot.
 * If a source fails, the old price and old timestamp are KEPT, so the row
 * ages naturally and flips to "⏳ OUTDATED" after 13 h (formula in column H).
 * Every successful price is also appended to the "Price Log" tab
 * (history for the 2-month momentum criterion).
 *
 * Install: Extensions → Apps Script → paste this file → run setup() once
 * and authorise. setup() creates the 4 daily triggers and runs one update.
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

  // ---- crypto: one CoinGecko call for all ids ----
  const ids = [...new Set(rows.filter(r => r[1] === 'crypto' && r[2]).map(r => r[2]))];
  let cg = {};
  if (ids.length) {
    const url = 'https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=' +
                encodeURIComponent(ids.join(','));
    try {
      const res = UrlFetchApp.fetch(url, { muteHttpExceptions: true });
      if (res.getResponseCode() === 200) cg = JSON.parse(res.getContentText());
      else console.warn('CoinGecko HTTP ' + res.getResponseCode());
    } catch (e) { console.warn('CoinGecko error: ' + e); }
  }

  const now = new Date();
  const log = [];
  rows.forEach((r, i) => {
    let p = null;
    if (r[1] === 'crypto') p = cg[r[2]] && cg[r[2]].usd;
    else if (r[1] === 'stock') p = (typeof r[3] === 'number' && r[3] > 0) ? r[3] : null;
    if (p) {
      snap[i][0] = p;
      snap[i][1] = now;
      log.push([now, r[0], p]);
    }                                    // else: keep old snapshot → ages into OUTDATED
  });
  sh.getRange(2, 5, n, 2).setValues(snap);

  let lg = ss.getSheetByName(LOG_SHEET);
  if (!lg) { lg = ss.insertSheet(LOG_SHEET); lg.appendRow(['Run at (Halifax)', 'Symbol', 'Price']); }
  if (log.length) lg.getRange(lg.getLastRow() + 1, 1, log.length, 3).setValues(log);
}
