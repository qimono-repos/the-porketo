/**
 * The Porketo — narrative feed for the book (Google Sheet).
 *
 * Once a day, reads the public YouTube RSS feed of each channel in CHANNELS
 * (no API key needed) and appends new videos to the `Narrative` tab:
 * published time, channel, title, which held assets the title or description
 * mentions, link, and the start of the description.
 *
 * Purpose: the "narrative" input of the crypto buy score
 * (DECISIONS/strategy/2026-10-24-diversification-gold-and-narrative.md).
 * Titles and descriptions are a starting point, not a buy signal on their own.
 *
 * X.com and forums have no free feed; check them by hand and note source + time.
 *
 * Install: Extensions → Apps Script → new file `narrative-feed` → paste → save →
 * run setupNarrative() once. If a channel shows "HTTP 404" in the log, its channel
 * ID is wrong: open the channel on YouTube → About → Share → Copy channel ID.
 */

const NARRATIVE_SHEET = 'Narrative';
const NARRATIVE_TZ = 'America/Halifax';
const NARRATIVE_HOUR = 6;   // Halifax, before the 10:00 slot
const CHANNELS = [
  ['Crypto Banter (Ran Neuner)', 'UCN9Nj4tjXbVTLYWN0EKly_Q'],
  ['Paul Barron Network', 'UC4VPa7EOvObpyCRI4YKRQRw'],
];

function setupNarrative() {
  ScriptApp.getProjectTriggers()
    .filter(t => t.getHandlerFunction() === 'updateNarrative')
    .forEach(t => ScriptApp.deleteTrigger(t));
  ScriptApp.newTrigger('updateNarrative').timeBased().atHour(NARRATIVE_HOUR).everyDays(1)
    .inTimezone(NARRATIVE_TZ).create();
  updateNarrative();
}

function updateNarrative() {
  const ss = SpreadsheetApp.getActive();
  let sh = ss.getSheetByName(NARRATIVE_SHEET);
  if (!sh) {
    sh = ss.insertSheet(NARRATIVE_SHEET);
    sh.appendRow(['Published (Halifax)', 'Channel', 'Title', 'Held assets mentioned', 'Link', 'Description (start)']);
  }
  const seen = new Set(sh.getLastRow() > 1
    ? sh.getRange(2, 5, sh.getLastRow() - 1, 1).getValues().map(r => r[0]) : []);

  // Held assets: symbol + CoinGecko id from the Prices tab (e.g. LINK / chainlink).
  const pr = ss.getSheetByName('Prices');
  const terms = pr.getRange(2, 1, pr.getLastRow() - 1, 3).getValues()
    .filter(r => r[0])
    .map(r => [String(r[0]).trim(), [String(r[0]).trim(), String(r[2]).replace(/-/g, ' ')]
      .filter(t => t.length >= 3)]);

  const atom = XmlService.getNamespace('http://www.w3.org/2005/Atom');
  const media = XmlService.getNamespace('media', 'http://search.yahoo.com/mrss/');
  const out = [];
  CHANNELS.forEach(([name, id]) => {
    const res = UrlFetchApp.fetch('https://www.youtube.com/feeds/videos.xml?channel_id=' + id,
      { muteHttpExceptions: true });
    if (res.getResponseCode() !== 200) { console.warn(name + ': HTTP ' + res.getResponseCode()); return; }
    XmlService.parse(res.getContentText()).getRootElement().getChildren('entry', atom).forEach(e => {
      const link = e.getChild('link', atom).getAttribute('href').getValue();
      if (seen.has(link)) return;
      const title = e.getChildText('title', atom);
      const group = e.getChild('group', media);
      const desc = group ? (group.getChildText('description', media) || '') : '';
      const text = (title + ' ' + desc).toLowerCase();
      const hits = terms.filter(([, ts]) => ts.some(t =>
        new RegExp('(^|[^a-z0-9])' + t.toLowerCase().replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '([^a-z0-9]|$)').test(text)))
        .map(([sym]) => sym);
      const pub = new Date(e.getChildText('published', atom));
      out.push([Utilities.formatDate(pub, NARRATIVE_TZ, 'yyyy-MM-dd HH:mm'), name, title,
                [...new Set(hits)].join(', '), link, desc.slice(0, 500)]);
    });
  });
  if (!out.length) return;
  out.sort((a, b) => a[0] < b[0] ? -1 : 1);
  sh.getRange(sh.getLastRow() + 1, 1, out.length, 6).setValues(out);
}
