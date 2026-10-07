# Project State

## Project

A personal trading, investment, and financial automation laboratory.

The project has two purposes that are treated as one unified system:

- Serve as a primary personal income resource through trading and investment activity.
- Serve as a laboratory for researching and developing automation of financial transactions, with the goal of executing transactions faster than a human can.

## The Book

As of October 3, 2026, the canonical trading workbook — referred to as "the book" — is the Google Sheet titled **TRADE-October-26-Sprint** (ID `1N_osVjWlUVElmZ8UoPUIa5aFex-gfSvy4nJ02k-_KrY`).

Whenever "the book" is mentioned anywhere in this project, it refers to this Google Sheet. It is the live workbook that is read and updated during trading sessions.

The earlier workbook, **Sep 15 Sprint - $100 Trading Ticket**, is frozen as September history and is not the live book.

## Canonical References

The canonical repository and book, plus the timezone-label convention, are
anchored in `project-links.md`. Resolve "the repository" (→ `qimono-repos/the-porketo`)
and "the book" (→ TRADE-October-26-Sprint) there before asking the user to
restate them.

## Who These Policies Bind

All operating policies in this document and in the `JOURNAL/` fatal-error reports
are **agent-neutral**. They bind every teammate on this project — all large
language models (Claude, ChatGPT, Gemini, and any other) **and** the human
operator. The standard holds regardless of who is at the keyboard. A policy
derived from one agent's failure applies to all; "the AI got it wrong" and "the
human did it by hand" are equally non-exemptions. See `project-links.md`.

## Role

The project owner is explicitly both:

- **Operator** — the person running the trading and investment activity.
- **Test Subject** — the person whose behaviour and decisions are part of the experiment.

## Recent Decisions

- **50% partial harvest policy (October 6, 2026):** from this point forward, when a strategy lot crosses its harvest criterion, the default harvest quantity is 50% of the quantity produced by the legacy harvest formula, then rounded down to Binance-compatible precision. Canonical expression: `new_harvest_quantity = ROUND_DOWN_TO_BINANCE_USDT_PRECISION(old_harvest_formula / 2)`. The strategy lot's material anchor is unchanged, the selected highest-active-rung protocol remains unchanged, and actual Binance execution remains the source of truth. See DECISIONS/strategy/2026-10-06-50-percent-partial-harvest-policy.md.

- **Policies are agent-neutral (October 6, 2026):** all project operating policies bind every teammate — every large language model and the human operator alike. A policy derived from one agent's failure applies to all; being an AI or acting by hand is not an exemption. See the "Who These Policies Bind" section above and project-links.md.

- **Contextual-disclosure discipline + timezone-label convention (October 6, 2026):** do not volunteer location, time, or country when the task does not require it. Timestamps coordinate against a GMT−3 reference clock (tracking the NYSE trading day); the city named is a readable label for that offset, not a location claim. Halifax is the warm-cycle label; Paramaribo (fixed GMT−3) is the winter catch, and the Halifax→Paramaribo switch signals the winter cycle. Greenland was dropped (it is at GMT−2 when Halifax is at GMT−4). See JOURNAL/2026-10-06-contextual-disclosure-and-timezone-convention.md.

- **Repository-identification continuity (October 6, 2026):** before asking the user to identify an established project resource, search the project context and canonical reference files. A `project-links.md` anchor now provides the explicit canonical mapping. See JOURNAL/2026-10-06-repository-identification-failure.md.

- **Claude self-report, Fatal Error Report 006 (October 6, 2026):** retrieval before interpretation, respect for settled decisions, and prompt use of known workarounds are continuity obligations binding on all teammates. See JOURNAL/2026-10-06-claude-fatal-error-report-006.md.

- **Canonical trading book identified (October 3, 2026):** "the book" refers to the Google Sheet titled TRADE-October-26-Sprint (ID 1N_osVjWlUVElmZ8UoPUIa5aFex-gfSvy4nJ02k-_KrY). It is the live workbook read and updated during trading sessions. The earlier Sep 15 Sprint workbook is frozen as September history. See the "The Book" section above.

- **Crisis Harvest mechanics formalized:** when the final-harvest-day condition activates and normal harvesting has not occurred by market close, select the open strategy lot with the smallest absolute USD/USDC-equivalent gap to its harvest threshold among lots below threshold. Liberate 90% of that lot's material anchor, leave 10% invested, preserve lot identity and anchor, and calculate the native Binance FROM quantity from the notification snapshot. If the available position at execution is smaller than the specified quantity, sell the entire remaining position rather than canceling the crisis movement.

- **Governance and journal refinement formalized:** the journal is the AI's durable memory of project reasoning, not a waiver form or replacement for source records. It uses concise AI-written reasoning by default while selectively preserving original wording when that wording carries an important conceptual insight, definition, principle, or breakthrough. The AI identifies the single best precedent for a new case; the operator is not required to formally cite or accept it during conversation and may instead overrule or distinguish it. Exceptions/deviations require a disposition, with rationale and outcome preserved. Precedents do not expire merely because time passes; they remain historical knowledge unless explicitly overruled, with applicability evaluated case by case. The first occurrence of a new case type receives full reasoning and later analogous cases may rely on it as precedent. Rule evolution must preserve prior reasoning rather than silently rewriting history. See JOURNAL/2026-09-30-governance-refinement.md.

## Last Updated

2026-10-06
