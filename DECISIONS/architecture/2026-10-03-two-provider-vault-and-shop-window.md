# Decision — Two-provider split: Hostinger "vault" + Hetzner "shop window"

**Date:** 2026-10-03
**Status:** Accepted (Hostinger VPS purchased today; Hetzner cloud box to follow)
**Context:** Voice working session, immediately after purchasing the Hostinger VPS
(Gardisto). Question arose of whether the public dashboard and other tasks should
live on the same box as the sentinel.

## Decision

Split the infrastructure across **two providers / two boxes / two failure domains**:

- **Hostinger — the "vault" (Gardisto).** The protected, private tenant: the
  sentinel (price-watching, threshold evaluation) and, later, any Binance keys /
  automation. KVM 1, **annual** term (cheaper rate; committed infrastructure).
- **Hetzner Cloud — the "shop window."** A cheap **monthly** cloud box serving the
  **public Gold dashboard** (Nginx + HTTPS) and casual "junk-drawer" tasks. Monthly
  billing keeps the experimental, public-facing piece disposable and resizable with
  no lock-in. Entry tier (CX/CAX, ~€5.99/mo; ARM CAX best value) is ample for Nginx.

## Why two providers (two rationales converging)

1. **Resilience — "don't put all the eggs in one basket" (the grandmother rule).**
   Two providers = two independent failure domains. A provider outage, billing
   problem, or account issue takes at most one box, not the whole operation.
2. **Separation of concerns — classic web architecture.** Front end on one server,
   back end on another: decoupled tiers, each secured, scaled and deployed
   independently. Long-standing web-development practice, independent of the risk
   argument.

Both principles land on the **same** design from different directions — a strong
signal the design is sound.

## The hard line (public vs private)

The public dashboard is a **read-only, derived Gold view** — the *story* (equity
curve, P/L, harvest cadence), built from the data, published as a rendered/snapshot
view. It has **no path back** to anything that can move money.

- **Shop window (Hetzner, public):** Gold consumption view only. Safe to serve to
  the open internet — publishing R&D progress is an explicit project goal (operator
  is both Operator and Test Subject).
- **Vault (Hostinger, private):** sentinel logic and any credentials. Never exposed
  to the public web port. With the split across providers, the public port is not
  even on the same machine as the money tenant — the earlier "public port on the
  money box" concern is dissolved.

This maps onto the medallion architecture: **Gold = public consumption view**;
upstream (silver/bronze, keys, watch-logic) stays private.

## Domains

- Qimono owns **qimono.online** and **qimono.vip** (each rented ~1 year via Namecheap).
- One of them becomes the public face of the shop-window dashboard (choice pending).
- Point the domain at the Hetzner box; Nginx serves over HTTPS (Let's Encrypt).

## Consequences / next steps

- Provision a cheap **monthly** Hetzner Cloud instance for the public dashboard.
- Keep Gardisto (Hostinger) private; do not open public web ports on it.
- Decide which domain (qimono.online vs qimono.vip) fronts the dashboard.
- Even on the shop-window box, keep casual tasks from undermining the public
  service (the junk-drawer should not jeopardise the Gold view).

## References
- `OPS/gardisto.md`
- `DECISIONS/risk/2026-10-03-compartmentalization-and-sentinel.md`
- `DECISIONS/architecture/2026-10-03-access-not-intelligence-is-the-constraint.md`
- `DECISIONS/architecture/2026-10-03-databricks-as-analytics-complement.md`
