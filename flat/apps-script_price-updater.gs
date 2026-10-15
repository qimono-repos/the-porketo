/**
 * The Porketo — price snapshot updater for the book (Google Sheet).
 *
 * Schedule: 03:00, 09:00, 15:00, 21:00 Halifax (1 hour before each checkpoint).
 * Each run sends at most ONE CoinGecko request (all missing coins batched) and,
 * only for coins still missing, ONE CryptoCompare request. No rapid retries.
 * If any coin is still missing, the script schedules itself again 10 minutes
 * later, up to MAX_RETRIES times (e.g. 03:10, 03:20, 03:30, 03:40), so every
 * attempt finishes well before the checkpoint at HH:00.
 *
 * Stocks: copies the live GOOGLEFINANCE value (column D) into the snapshot.
 * Column E = price snapshot, column F = timestamp. Rows with no fresh price keep
 * their old snapshot and age into "⏳ OUTDATED" after 13 h (formula in column H).
 * Every successful price is appended to "Price Log" with its source.
 *
 * Optional (recommended): free CoinGecko Demo API key in Script Properties as
 * COINGECKO_DEMO_KEY — gives this script its own quota instead of the shared one.
 *
 * Install: Extensions → Apps Script → paste → save → run setup() once.
 */

const PRICES_SHEET = 'Prices';
const LOG_SHEET = 'Price Log';
const RUN_HOURS = [3, 9, 15, 21];   // Halifax local time
const TZ = 'America/Halifax';
const RETRY_MINUTES = 10;
const MAX_RETRIES = 5;

function setup() {
  ScriptApp.getProjectTriggers()
    .filter(t => ['updatePrices', 'retryPrices'].includes(t.getHandlerFunction()))
    .forEach(t => ScriptApp.deleteTrigger(t));
  RUN_HOURS.forEach(h =>
    ScriptApp.newTrigger('updatePrices')
      .timeBased().atHour(h).everyDays(1).inTimezone(TZ)
      .create());
  updatePrices();
}

/** Scheduled run: fresh cycle, refreshes everything. */
function updatePrices() {
  PropertiesService.getScriptProperties().setProperty('RETRY_COUNT', '0');
  clearRetryTriggers_();
  run_(false);
}

/** One-off retry run: only crypto rows still missing a fresh price. */
function retryPrices() {
  clearRetryTriggers_();
  run_(true);
}

function run_(retryOnly) {
  const props = PropertiesService.getScriptProperties();
  const ss = SpreadsheetApp.getActive();
  const sh = ss.getSheetByName(PRICES_SHEET);
  const n = sh.getLastRow() - 1;
  if (n < 1) return;

  SpreadsheetApp.flush();
  const rows = sh.getRange(2, 1, n, 4).getValues();   // A Symbol, B Type, C Source ID, D Live
  const snap = sh.getRange(2, 5, n, 2).getValues();   // E Price, F Updated At
  const now = new Date();
  const cycleStart = retryOnly
    ? new Date(Number(props.getProperty('CYCLE_START')) || 0)
    : now;
  if (!retryOnly) props.setProperty('CYCLE_START', String(now.getTime()));

  // A crypto row "needs" a price if its snapshot is older than this cycle's start.
  const needs = (r, i) => r[1] === 'crypto' &&
    (!retryOnly || !(snap[i][1] instanceof Date) || snap[i][1] < cycleStart);

  const want = rows.map((r, i) => needs(r, i));
  const ids = [...new Set(rows.filter((r, i) => want[i] && r[2]).map(r => r[2]))];
  const cg = ids.length ? fetchCoinGecko_(ids) : {};
  const ccSyms = rows.filter((r, i) => want[i] && !(cg[r[2]] && cg[r[2]].usd)).map(r => String(r[0]));
  const cc = ccSyms.length ? fetchCryptoCompare_(ccSyms) : {};

  const log = [];
  let stillMissing = 0;
  rows.forEach((r, i) => {
    let p = null, src = '';
    if (r[1] === 'crypto' && want[i]) {
      if (cg[r[2]] && cg[r[2]].usd) { p = cg[r[2]].usd; src = 'CoinGecko'; }
      else if (cc[r[0]] && cc[r[0]].USD) { p = cc[r[0]].USD; src = 'CryptoCompare'; }
      else stillMissing++;
    } else if (r[1] === 'stock' && !retryOnly) {
      if (typeof r[3] === 'number' && r[3] > 0) { p = r[3]; src = 'GOOGLEFINANCE'; }
    }
    if (p) { snap[i][0] = p; snap[i][1] = now; log.push([now, r[0], p, src]); }
  });
  sh.getRange(2, 5, n, 2).setValues(snap);
  sh.getRange(2, 6, n, 1).setNumberFormat('yyyy-mm-dd hh:mm');

  let lg = ss.getSheetByName(LOG_SHEET);
  if (!lg) { lg = ss.insertSheet(LOG_SHEET); lg.appendRow(['Run at (Halifax)', 'Symbol', 'Price', 'Source']); }
  if (log.length) {
    lg.getRange(lg.getLastRow() + 1, 1, log.length, 4).setValues(log);
    lg.getRange(2, 1, lg.getLastRow() - 1, 1).setNumberFormat('yyyy-mm-dd hh:mm');
  }

  // Schedule a calm retry if anything is still missing.
  const count = Number(props.getProperty('RETRY_COUNT') || '0');
  if (stillMissing > 0 && count < MAX_RETRIES) {
    props.setProperty('RETRY_COUNT', String(count + 1));
    ScriptApp.newTrigger('retryPrices').timeBased().after(RETRY_MINUTES * 60 * 1000).create();
    console.log(stillMissing + ' coin(s) missing — retry ' + (count + 1) + '/' + MAX_RETRIES +
                ' in ' + RETRY_MINUTES + ' min');
  } else if (stillMissing > 0) {
    console.warn(stillMissing + ' coin(s) still missing after ' + MAX_RETRIES +
                 ' retries — they keep their old snapshot and will show OUTDATED after 13 h');
  }
}

function clearRetryTriggers_() {
  ScriptApp.getProjectTriggers()
    .filter(t => t.getHandlerFunction() === 'retryPrices')
    .forEach(t => ScriptApp.deleteTrigger(t));
}

function fetchCoinGecko_(ids) {
  const key = PropertiesService.getScriptProperties().getProperty('COINGECKO_DEMO_KEY');
  const url = 'https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=' +
              encodeURIComponent(ids.join(','));
  const opts = { muteHttpExceptions: true, headers: key ? { 'x-cg-demo-api-key': key } : {} };
  try {
    const res = UrlFetchApp.fetch(url, opts);
    if (res.getResponseCode() === 200) return JSON.parse(res.getContentText());
    console.warn('CoinGecko HTTP ' + res.getResponseCode());
  } catch (e) { console.warn('CoinGecko error: ' + e); }
  return {};
}

function fetchCryptoCompare_(symbols) {
  const url = 'https://min-api.cryptocompare.com/data/pricemulti?tsyms=USD&fsyms=' +
              encodeURIComponent(symbols.join(','));
  try {
    const res = UrlFetchApp.fetch(url, { muteHttpExceptions: true });
    if (res.getResponseCode() === 200) {
      const j = JSON.parse(res.getContentText());
      if (!j.Response) return j;
      console.warn('CryptoCompare: ' + (j.Message || 'error'));
    } else {
      console.warn('CryptoCompare HTTP ' + res.getResponseCode());
    }
  } catch (e) { console.warn('CryptoCompare error: ' + e); }
  return {};
}
