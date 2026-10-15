# Continuity & Contradiction Layer

**Status:** Proposed specification  
**Author:** Grok_at_Qimono <grok@qimono.vip>  
**Date:** 2026-10-15  
**Type:** Process discipline / mandatory pre-decision protocol

## Purpose

Prevent the project from re-solving the same problems or quietly drifting from its own settled reasoning.

The project already possesses excellent rules, an evidence hierarchy, and a journal. What it still lacks is a *forced continuity mechanism* that makes the project’s accumulated intelligence the shared operating system rather than optional background knowledge.

This layer sits between any agent (or the operator) and any material recommendation. It is deliberately lightweight and costs almost nothing in tokens once the habit is formed.

## Scope

This protocol applies before any of the following:

- Team classification change (promotion / demotion)
- Harvest recommendation (regular, 50 %, or Crisis)
- Capital reallocation or target adjustment
- New rule, threshold, or operating procedure
- Any recommendation that would alter strategy-lot status or material anchor treatment

It does **not** apply to pure information retrieval, price refreshes, or non-actionable discussion.

## Mandatory Pre-Decision Checkpoint

Before issuing any material recommendation, the agent (or operator) must complete the following three steps and surface them explicitly:

### 1. Surface the single best existing precedent

Locate and quote (or link) the single most relevant prior reasoning from the JOURNAL, DECISIONS, or SPECS.  
Do not summarise. Present the actual prior language or a direct link to it.

If no relevant precedent exists, state that fact clearly.

### 2. Name any contradiction

Explicitly declare whether the proposed action contradicts any of the following:

- Settled project principles (evidence hierarchy, fixed-capacity rule, agent-neutral policies, etc.)
- Previously recorded outcomes or dispositions
- Existing specifications in SPECS/
- The current Three-Team Model constraints (10 / 10 / 15)

If a contradiction exists, name it in one clear sentence.  
If none exists, state “No contradiction detected.”

### 3. Force an explicit disposition

Record one of three dispositions:

- **Accept** — the precedent stands and the new action is consistent with it.
- **Distinguish** — the current case is materially different; state the distinction in one sentence.
- **Overrule** — the prior reasoning is being set aside; state the rationale in one sentence.

The disposition and its one-line rationale must be written into the JOURNAL immediately.

## Implementation Notes

- Preferred location for the one-line mandatory header in agent responses:

  ```
  Continuity check: [precedent link or “none”] | Contradiction: [none / named] | Disposition: [Accept / Distinguish / Overrule] — [one-line rationale]
  ```

- The full reasoning that produced the disposition belongs in a journal entry, not in the recommendation itself.
- No new code is required on day one. This is a process discipline. Light automation (e.g., a simple journal template or agent prompt injection) can be added later if the discipline proves valuable.
- Final authority remains with the operator. The layer does not decide; it forces visibility and continuity of reasoning.

## Rationale

- Directly attacks the documented blind spots of “loss of historical reasoning” and rising coordination overhead (Mythical Man-Month).
- Converts the project’s existing memory into an active control surface rather than passive documentation.
- Raises the probability that multiple agents together clear the survival threshold by preventing repeated rediscovery of the same lessons.
- Keeps the knowledge belonging to the project, not to any individual model.

## Relationship to Existing Specs

This layer complements, and does not replace:

- SPECS/DEVIATIONS.md
- SPECS/CRISIS_HARVEST_MECHANICS.md
- The evidence hierarchy
- The agent-neutral policy binding

It is a pre-filter that makes those mechanisms more reliable under multi-agent operation.

## Acceptance

This specification becomes binding only when the project explicitly adopts it (via decision record or operator confirmation). Until then it remains a candidate contribution.
