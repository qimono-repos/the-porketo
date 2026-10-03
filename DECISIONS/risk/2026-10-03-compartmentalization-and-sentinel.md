# Decision — Compartmentalized capital + an always-on sentinel (VPS as risk infrastructure)

**Date:** 2026-10-03
**Status:** Accepted (operating posture); automation phased
**Context:** Voice working session on how to operate the book day-to-day across a
disposable multi-machine fleet, and how to protect real (growing) capital.

## The risk posture

Two simple, durable ideas attacking two different axes of risk:

### 1. Compartmentalization — "don't put all the eggs in one basket"
Cap the **size of loss** (blast radius) by spreading capital across **independent
venues**, each holding a small bag:
- a small amount in **Binance** (incl. tokenized stocks — the new 24/7 element),
- a small amount in **Robinhood**,
- a small amount in a home-country **CDR** vehicle (venue deliberately unnamed here).

No single failure — a venue lockdown, a withdrawal freeze, a dead watchpost, or a
**Mantra-style ~90%-in-an-hour collapse** — can take more than its own bag. You
lose a *source*, not the *system*. This is the cheap, correct version of the
integrity problem: with small personal money you can solve by **partitioning**
what big-company critical data forces you to solve with heavy engineering.

### 2. The sentinel — an always-on watchpost
Cap the **time to detection** by moving the watch **off any machine the operator
personally depends on.** Motivation: a local-only setup ties the money's safety to
the operator's electricity and ISP. Real threats are concrete — power cuts, and
**El Niño storms in South America in the coming months**. The failure to avoid is
"broke and didn't even notice." A small cloud **VPS** has independent power and
redundant connectivity and stays awake when the operator can't.

**Together:** compartmentalization limits *how much* a failure costs; the sentinel
limits *how long* it goes unnoticed. Size-of-loss and time-to-detection, both
covered.

## The fleet context (why a VPS fits this operator specifically)
- No primary computer by design: a **fleet** of disposable machines (Windows, Mac,
  Linux; iPhone, Pixel, foldable, Android tablet, iPad), ~6-month lifespan each,
  reproduced from a **dotfiles repo**. Machines are cattle, not pets.
- The invariant is **the repos**, never a local disk. Any machine: clone,
  authenticate, work, wipe without loss.
- The VPS becomes the **one permanent member of the herd** — the stable box that
  is never wiped on the 6-month cycle, reachable identically from any device.

## Automation — phased, with partitioning preserved at the automation layer
Goal is **automation that acts** (e.g. encoding Crisis Harvest for when the
operator is unreachable). Cautions, given a risk-averse operator and real money:

- **Phase 1 — Sentinel-first.** The VPS **watches and alerts only**: refresh
  prices, evaluate harvest/crisis thresholds on schedule, notify. Read-only to
  venues, or no keys at all. Prove the thresholds and Crisis Harvest logic fire
  correctly before granting any power to act.
- **Phase 2 — Considered automation.** Only when trusted. Keys scoped as tightly
  as each venue allows; hard guardrails (Crisis Harvest rules) encoded.

**Critical constraint — bags must stay independent at the automation layer, not
just the capital layer.** Three venues driven from one VPS with all keys on one
box **re-couples** the bags: the VPS becomes a shared single point of failure. Keep
the sentinel's power to act **scoped per-venue and minimal**, so compromise of the
watchpost cannot drain every bag at once. Each venue = a separate integration with
its own API, key security, and quirks — real surface area; add them one at a time.

## The through-line (three durable ideas, one per layer)
- **Capital layer:** grandmother's baskets — compartmentalization / fault isolation.
- **Time layer:** the sentinel — always-on detection independent of the operator.
- **Truth layer:** Datomic's never-forget ledger — immutable, auditable record.

Primitive framing is a feature: these rules make **no assumption about what
fails**, so they survive novel threats by capping consequences rather than
predicting causes.

## References
- `DECISIONS/architecture/2026-10-03-access-not-intelligence-is-the-constraint.md`
- `DECISIONS/architecture/2026-10-03-databricks-as-analytics-complement.md`
- `SPECS/CRISIS_HARVEST_MECHANICS.md`
