# Fatal Error Report 005 — Contextual Disclosure & Timezone-Label Convention

**Failure class:** Contextual disclosure / unnecessary geographic detail / continuity
**Affected workflow:** Trading project conversation and AI-teammate continuity
**Reference clock:** GMT−3 (anchored to the New York trading day)
**Warm-cycle label:** Halifax (Atlantic Daylight Time = GMT−3)
**Winter-cycle label:** Paramaribo (Suriname, fixed GMT−3 year-round)
**Corrective principle:** Minimise unnecessary contextual disclosure; never volunteer location, time, or country when the task does not require it.

## Incident Summary

This report records a contextual-disclosure issue in which the assistant
surfaced geographic/time context that the user had not asked for. The correct
behaviour is to avoid volunteering location, timezone, or country when it is not
needed for the task.

The user established a presentation convention for this workflow built around a
**reference time zone**, not a physical location claim.

## Corrective Rule — Disclosure Discipline

Do not surface internal geographic context merely because it is available. When
location is not necessary to the task, say nothing about location. Context
availability does not imply disclosure permission.

## The Timezone-Label Convention

The project coordinates timestamps against a **reference clock**, in the same
spirit that aviation uses UTC as "Zulu" and finance uses UTC as "Greenwich".
This is a convention for unambiguous time coordination, **not** a claim about the
user's physical location.

- **The true anchor is the offset: GMT−3**, chosen to stay as close as possible
  to the New York Stock Exchange trading day.
- The city named is a **readable label** for that offset, not a location claim.

### Nearest-first fallback chain

Labels are chosen nearest-first to New York, and each is used only while it is
actually at GMT−3:

1. **Halifax** — closest; use whenever it is at GMT−3 (its daylight-saving
   period, roughly March–November). This is the default, warm-cycle label.
2. **Paramaribo** (Suriname) — fixed GMT−3 year-round, no daylight saving,
   Northern Hemisphere. Used the moment Halifax falls back to GMT−4.

Greenland was considered as an intermediate nearest step but **dropped**: when
Halifax is at GMT−4, Greenland is at GMT−2 (not GMT−3), so it never actually
satisfies the GMT−3 test when needed. Including it would only muddy the signal.

### The label as a seasonal signal

The switch from **Halifax → Paramaribo** is itself a meaningful signal. The day
the assistant stops saying "Halifax" and starts saying "Paramaribo", the user
knows immediately that the clock has fallen back to the winter cycle. The facade
therefore doubles as a seasonal indicator.

## Primary Lesson

Context availability does not imply disclosure permission. Project continuity
includes presentation conventions as well as technical resources. The GMT−3
reference clock is the durable anchor; the city label is a readable,
signal-bearing stand-in for that offset and must persist across turns and across
AI teammates.
