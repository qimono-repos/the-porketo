/**
 * The Porketo — candle and harvest alert for the book (Google Sheet).
 *
 * Runs every hour. For every asset held in `Sprint` (stocks) and `Crypto Sprint`
 * (crypto) it:
 *   1. gets a live price (crypto: one CoinGecko call; stocks: GOOGLEFINANCE column D
 *      of the `Prices` tab),
 *   2. adds up the excess of every lot above its material anchor,
 *   3. checks the harvest ladder: the largest step that is at most 50% of the excess
 *      (protocols/harvest-ladder.md, amendment 2026-10-24),
 *   4. flags a candle when the price moved CANDLE_PCT or more since the last hourly run.
 * Anything new is emailed to the owner of the script and appended to the `Alerts` tab.
 * The same asset and step are not repeated within REPEAT_HOURS.
 *
 * An alert is a prompt to look, not an order: check the live venue quote, then follow
 * protocols/harvest-ladder.md. The receipt is execution truth.
 *
 * Weekend note: GOOGLEFINANCE gives Friday's close for stocks, so bStock candles on
 * Saturday/Sunday are not seen. Crypto is covered 24/7.
 *
 * Install: Extensions → Apps Script → new file `candle-alert` → paste → save →
 * run setupAlerts() once. Uses the same optional COINGECKO_DEMO_KEY Script Property
 * as the price worker. Optional ALERT_EMAIL Script Property overrides the recipient.
 */

const ALERT_PRICES_SHEET = 'Prices';
const ALERT_STOCK_SHEET = 'Sprint';          // C ticker, F anchor, G status, I units (from row 3)
const ALERT_CRYPTO_SHEET = 'Crypto Sprint';  // B asset, D anchor, E units (from row 6)
const ALERT_LOG_SHEET = 'Alerts';
const ALERT_TZ = 'America/Paramaribo'   // GMT-3 all year; same as Halifax until 1 Nov 2026 (decision 2026-10-24);
const LADDER = [0.30, 0.45, 0.75, 1.50, 2.25, 3.75, 6.00];   // USDT
const CANDLE_PCT = 4;      // % move in one hour that counts as a candle
const REPEAT_HOURS = 6;    // don't repeat the same alert sooner than this

function setupAlerts() {
  ScriptApp.getProjectTriggers()
    .filter(t => t.getHandlerFunction() === 'checkCandles')
    .forEach(t => ScriptApp.deleteTrigger(t));
  ScriptApp.newTrigger('checkCandles').timeBased().everyHours(1).create();
  checkCandles();
}

function checkCandles() {
  const ss = SpreadsheetApp.getActive();
  const props = PropertiesService.getScriptProperties();
  const now = new Date();
  const stamp = Utilities.formatDate(now, ALERT_TZ, 'yyyy-MM-dd HH:mm');

  // 1. Live prices
  const pr = ss.getSheetByName(ALERT_PRICES_SHEET);
  const pRows = pr.getRange(2, 1, pr.getLastRow() - 1, 5).getValues(); // A sym, B type, C id, D live, E snapshot
  const ids = [...new Set(pRows.filter(r => r[1] === 'crypto' && r[2]).map(r => r[2]))];
  const cg = ids.length ? alertFetchCoinGecko_(ids) : {};
  const price = {};
  pRows.forEach(r => {
    const sym = String(r[0]).trim();
    if (!sym) return;
    let p = null;
    if (r[1] === 'crypto' && cg[r[2]] && cg[r[2]].usd) p = cg[r[2]].usd;
    else if (r[1] === 'stock' && typeof r[3] === 'number' && r[3] > 0) p = r[3];
    if (p) price[sym] = p;
  });

  // 2. Lots: [symbol, anchor, units]
  const lots = [];
  const st = ss.getSheetByName(ALERT_STOCK_SHEET);
  st.getRange(3, 1, Math.max(st.getLastRow() - 2, 1), 9).getValues().forEach(r => {
    if (r[6] === 'OPEN' && r[2] && Number(r[8]) > 0) lots.push([String(r[2]).trim(), Number(r[5]), Number(r[8]), String(r[1])]);
  });
  const cr = ss.getSheetByName(ALERT_CRYPTO_SHEET);
  cr.getRange(6, 1, Math.max(cr.getLastRow() - 5, 1), 5).getValues().forEach(r => {
    if (r[1] && Number(r[4]) > 0) lots.push([String(r[1]).trim(), Number(r[3]), Number(r[4]), String(r[0])]);
  });

  // 3. Excess per asset, ladder step, candle
  const assets = {};
  lots.forEach(([sym, anchor, units, label]) => {
    const p = price[sym];
    if (!p) return;
    const a = assets[sym] || (assets[sym] = { p, excess: 0, lots: [] });
    const ex = units * p - anchor;
    if (ex > 0) { a.excess += ex; a.lots.push(label + ' +' + ex.toFixed(2)); }
  });

  const alerts = [];
  Object.keys(price).forEach(sym => {
    const p = price[sym];
    const last = Number(props.getProperty('LAST_' + sym) || 0);
    props.setProperty('LAST_' + sym, String(p));
    const a = assets[sym];
    if (a) {
      const fits = LADDER.filter(s => s <= a.excess * 0.5 + 1e-9);
      if (fits.length) {
        const step = fits[fits.length - 1];
        if (alertIsNew_(props, sym + '_H' + step, now)) {
          alerts.push([stamp, sym, 'HARVEST', p, a.excess.toFixed(2), step,
            'Step ' + step.toFixed(2) + ' USDT fits (50% of ' + a.excess.toFixed(2) + '). Lots above anchor: ' + a.lots.join(', ')]);
        }
      }
    }
    if (last > 0) {
      const pct = (p / last - 1) * 100;
      if (Math.abs(pct) >= CANDLE_PCT && alertIsNew_(props, sym + (pct > 0 ? '_UP' : '_DOWN'), now)) {
        alerts.push([stamp, sym, pct > 0 ? 'CANDLE UP' : 'CANDLE DOWN', p, a ? a.excess.toFixed(2) : '', '',
          pct.toFixed(1) + '% in about 1 h (' + last + ' → ' + p + ')' +
          (pct > 0 ? '. Check the ladder now.' : '. Possible dip entry; check the buy criteria.')]);
      }
    }
  });
  if (!alerts.length) return;

  // 4. Log and email
  let lg = ss.getSheetByName(ALERT_LOG_SHEET);
  if (!lg) {
    lg = ss.insertSheet(ALERT_LOG_SHEET);
    lg.appendRow(['At (Halifax)', 'Symbol', 'Kind', 'Price', 'Excess (USDC)', 'Ladder step', 'Detail']);
  }
  lg.getRange(lg.getLastRow() + 1, 1, alerts.length, 7).setValues(alerts);

  const to = props.getProperty('ALERT_EMAIL') || Session.getEffectiveUser().getEmail();
  const subject = 'Porketo: ' + alerts.map(a => a[2] + ' ' + a[1]).join(', ');
  const body = 'Alerts at ' + stamp + ' Halifax\n\n' +
    alerts.map(a => a[2] + ' · ' + a[1] + ' @ ' + a[3] + '\n  ' + a[6]).join('\n\n') +
    '\n\nCheck the live venue quote before acting. Book: ' + ss.getUrl();
  MailApp.sendEmail(to, subject, body);
}

function alertIsNew_(props, key, now) {
  const last = Number(props.getProperty('SENT_' + key) || 0);
  if (now.getTime() - last < REPEAT_HOURS * 3600 * 1000) return false;
  props.setProperty('SENT_' + key, String(now.getTime()));
  return true;
}

function alertFetchCoinGecko_(ids) {
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
