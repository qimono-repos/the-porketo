/**
 * Price refresher for the trading book (Google Sheet TRADE-October-26-Sprint, tab "Prices").
 * Rebuilt 2026-10-20: the new book (link changed 2026-10-16) had no bound script and no triggers,
 * so prices froze and every row showed OUTDATED.
 *
 * SETUP (Extensions > Apps Script in the book):
 * 1. Paste this file into Code.gs and save.
 * 2. Put the CoinGecko Demo key in CG_KEY (coingecko.com > developer dashboard >
 *    floating ☰ button bottom-right > "Claves de API" > copy icon). NEVER commit the real key.
 * 3. Run installTriggers once (approve permissions: Advanced > Go to project > Allow).
 * 4. Run refreshPrices once to test. Execution log should show "200 {...}".
 *
 * Prices tab columns: A Symbol | B Type (crypto/stock) | C Source ID | D Live (GOOGLEFINANCE)
 *                     E Price (snapshot) | F Updated At (Halifax) | G Age (h) | H Status
 * Crypto: CoinGecko simple/price by Source ID (needs the Demo key header; without it Google IPs get no data).
 * Stocks: copies the GOOGLEFINANCE live value from column D.
 * Older than 13h => OUTDATED. Every fresh price is appended to "Price Log".
 */

const SHEET = 'Prices';
const LOG = 'Price Log';
const TZ = 'America/Halifax';
const CG_KEY = 'PASTE_YOUR_COINGECKO_DEMO_KEY_HERE'; // do not commit the real key

function refreshPrices() {
  const ss = SpreadsheetApp.getActive();
  const sh = ss.getSheetByName(SHEET);
  const rows = sh.getRange(2, 1, sh.getLastRow() - 1, 8).getValues();
  const now = new Date();
  const stamp = Utilities.formatDate(now, TZ, 'yyyy-MM-dd HH:mm');

  // Crypto: one CoinGecko call for all ids
  const ids = rows.filter(r => r[1] === 'crypto' && r[2]).map(r => r[2]);
  let cg = {};
  if (ids.length) {
    const url = 'https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=' + ids.join(',');
    const res = UrlFetchApp.fetch(url, {muteHttpExceptions: true, headers: {'x-cg-demo-api-key': CG_KEY}});
    Logger.log(res.getResponseCode() + ' ' + res.getContentText().slice(0, 200));
    cg = JSON.parse(res.getContentText());
  }

  const log = [];
  rows.forEach((r, i) => {
    const [sym, type, id, live] = r;
    let price = null, src = '';
    if (type === 'crypto' && cg[id] && cg[id].usd) { price = cg[id].usd; src = 'CoinGecko'; }
    if (type === 'stock' && typeof live === 'number' && live > 0) { price = live; src = 'GOOGLEFINANCE'; }
    if (price !== null) {
      sh.getRange(i + 2, 5, 1, 4).setValues([[price, stamp, 0, '✅ FRESH']]);
      log.push([stamp, sym, price, src]);
    } else {
      // keep old price, recompute age from Updated At
      const t = r[5] instanceof Date ? r[5] : new Date(String(r[5]).replace(' ', 'T'));
      const age = isNaN(t) ? 999 : Math.round((now - t) / 36e5 * 10) / 10;
      sh.getRange(i + 2, 7, 1, 2).setValues([[age, age > 13 ? '⏳ OUTDATED' : '✅ FRESH']]);
    }
  });

  if (log.length) {
    const lg = ss.getSheetByName(LOG);
    lg.getRange(lg.getLastRow() + 1, 1, log.length, 4).setValues(log);
  }
}

// Runs refreshPrices at 03:00, 09:00, 15:00, 21:00 Halifax (1h before each checkpoint).
function installTriggers() {
  ScriptApp.getProjectTriggers().forEach(t => ScriptApp.deleteTrigger(t));
  [3, 9, 15, 21].forEach(h =>
    ScriptApp.newTrigger('refreshPrices').timeBased().atHour(h).everyDays(1).inTimezone(TZ).create());
}
