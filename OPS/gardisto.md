# Gardisto — the sentinel VPS

**Name:** Gardisto (Esperanto, "guard / one who guards," from *gardi*, to guard).
Chosen per the Qimono Esperanto naming convention (same tradition as RAKONTU).
**Date named:** 2026-10-03
**Status:** Planned — provisioning (Hostinger KVM VPS, yearly plan under evaluation).

## What Gardisto is

Gardisto is the **always-on sentinel** for the porketo book: the one permanent
member of the otherwise-disposable machine fleet. It stands watch while the
operator — and every one of the operator's devices — may be offline. It exists to
cap **time-to-detection** of risk events (see the risk decision note).

## Role (phase 1 — sentinel-first)

- **Watches:** refreshes prices and evaluates harvest / Crisis Harvest thresholds
  on a schedule (e.g. the 2-hour checkpoint rhythm).
- **Alerts:** notifies the operator when a line is crossed. It does **not** trade.
- **Access:** read-only to venues, or no venue keys at all (fed prices only).
- **Purpose:** ensure the operator can never be "broke without noticing" during a
  power cut, ISP outage, storm (El Niño risk), or a Mantra-style sudden collapse.

## Role (phase 2 — considered automation, later)

- May be granted **scoped, minimal** power to act on clear-cut rules (e.g. Crisis
  Harvest) when the operator is unreachable — only once trusted.
- **Constraint:** power to act must be **scoped per-venue and minimal** so that
  compromise of Gardisto cannot drain every compartmentalized bag at once. The
  capital-layer partitioning must be preserved at the automation layer.

## Why a permanent box for a disposable fleet

The operator runs no primary computer — a fleet of ~6-month-lifespan machines
reproduced from dotfiles, plus multiple phones/tablets. The invariant is the
repos, never local disk. Gardisto is the stable exception: never wiped on the
6-month cycle, reachable identically from any device.

## References
- `DECISIONS/risk/2026-10-03-compartmentalization-and-sentinel.md`
- `SPECS/CRISIS_HARVEST_MECHANICS.md`
