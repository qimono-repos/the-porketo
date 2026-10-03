# Decision — Public dashboard (shop window) on AWS Lightsail

**Date:** 2026-10-03
**Status:** Accepted (box not yet created)
**Context:** Voice working session, same day the Hostinger vault (Gardisto) was
purchased. Shopping for the public-facing dashboard host.

## Decision

Host the public **Gold dashboard** (the "shop window") on **AWS Lightsail**, the
$5/month dual-stack (IPv4+IPv6) Linux nano bundle. **Hetzner is shelved** for now.

## Why Lightsail, why now

- **Learning value is the real driver.** Operator spent most of his career on
  **Azure**; trying AWS from the inside broadens cloud fluency to the other major
  provider — same rationale as keeping Databricks sharp and trying Hetzner. This is
  the legitimate motive, not impulse shopping.
- **Available today.** The cheap Hetzner Cost-Optimized line (CX23 ~€5.99, etc.) was
  entirely **"not available"** (out of stock — Hetzner's limited older-hardware
  supply). Lightsail can be created right now.
- **Free for 3 months.** New Lightsail customers get the first 3 months free on
  select bundles (Linux $5–$12), one bundle per account. A no-regret way to learn AWS.
- **Predictable, VPS-like.** Lightsail is AWS's deliberately-simple fixed-price VPS
  (bandwidth included), the Linode/DigitalOcean-like experience wanted — NOT bare EC2
  with its à-la-carte billing maze. 30–50% cheaper than equivalent EC2 for small loads.

## Pricing (2026, verified)

- **$3.50/mo** — IPv6-only Linux nano: 512 MB RAM, 2 vCPU, 20 GB SSD, 1 TB transfer.
- **$5/mo** — dual-stack (public IPv4 + IPv6) nano. **Chosen** — a public dashboard
  wants IPv4.
- Raw EC2 t4g.nano is ~$3.07/mo list but adds storage + IPv4 + bandwidth separately →
  Lightsail is the better call.

## Why geographic distribution matters less here

The earlier Boston-vs-Central-Europe reasoning (Hetzner in Germany, away from the
Boston vault) mattered most when the second box would hold **money**. For a
**public, read-only Gold view**, continent separation matters far less. Keep the
geographic-distribution principle in reserve for a future split of the *vault* itself.

## One dashboard, one box

Do NOT run both Hetzner and Lightsail for the same dashboard — that's two bills for
one job, not "baskets." Baskets apply to capital and to the money-bearing tenants,
not to a single read-only display.

## Guardrails (because it is still AWS)

- **The free 3 months auto-converts to paid.** Set an AWS billing alarm AND a
  calendar reminder at creation time, or it starts charging silently.
- **Pick a Lightsail bundle, not a bare EC2 instance** — keep the fixed predictable
  price; do not wander into EC2 à-la-carte billing.
- The box is the **shop window**: serves the read-only Gold dashboard only. No keys,
  no money-moving logic — those stay on the private Hostinger vault (Gardisto).

## References
- `DECISIONS/architecture/2026-10-03-two-provider-vault-and-shop-window.md`
- `OPS/gardisto.md`
- `DECISIONS/risk/2026-10-03-compartmentalization-and-sentinel.md`
