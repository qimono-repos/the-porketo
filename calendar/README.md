# Calendar events

The live checkpoint schedule is Albert's Google Calendar (primary).

- October: one event per slot, "Checkpoint N of 98" (America/Halifax), plus "Harvest N of 98" 15 min later.
- November: 6 recurring daily series (COUNT=30, America/Paramaribo) at 00, 04, 08, 12, 16 and 20.
  Slot # of 180 = (day − 1) × 6 + k.

`november-event-description.md` is the master description for the November series.
`{HH}` = hour of the series, `{K}` = slot of the day (1–6).

Links block format: label on one line, a blank line, the bare URL, a blank line.
Keep the blank lines: Google Calendar only turns a URL into a link when it stands alone.
The Google Sheet (book) link must always be present.

To change the events: edit the master here, commit to trunk, then update all 6 series
(update the series, not single occurrences) with the substituted text.
