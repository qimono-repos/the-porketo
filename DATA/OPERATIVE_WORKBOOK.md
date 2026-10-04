# Operative Trading Workbook

## Current operative workbook

**File:** `TRADE-October-26-Sprint.xlsx`  
**Role:** Operative trading workbook / Excel snapshot registered with The-Porketo  
**Operational copy:** Microsoft 365 / OneDrive  
**GitHub repository:** `qimono-repos/the-porketo`  
**Default branch:** `trunk`  
**Registered:** 2026-10-04

### Microsoft 365 location

The operative workbook was uploaded to the OneDrive root and confirmed by Microsoft 365:

https://onedrive.live.com/personal/3513c281268a4266/_layouts/15/doc.aspx?resid=75a107fb-5673-44b2-87f3-653b6d18135f&cid=3513c281268a4266

### Registered snapshot identity

- Filename: `TRADE-October-26-Sprint.xlsx`
- Size: 127,852 bytes
- SHA-256: `8aa209c79136eb6744b43a5f85cd42cb51bf39f8d7cfa63d82acafc59afdce8f5909`

> Note: the SHA-256 above is the identity of the workbook snapshot registered from the ChatGPT conversation upload. It is used to distinguish this exact snapshot from later M365 workbook revisions.

### Workbook structure

The registered snapshot contains 12 worksheets:

1. `README`
2. `Dashboard`
3. `Sprint`
4. `Trades`
5. `Trades-October`
6. `Positions`
7. `Crypto Sprint`
8. `Crypto Trades`
9. `Crypto Positions`
10. `Sprint Backup 2026-09-08 1550`
11. `Stock Summary Positions`
12. `Crypto Summary Positions`

### Source-of-truth boundary

The workbook is an operational accounting and trading-state artifact. The-Porketo repository is the durable project knowledge layer.

The operating chain remains:

**REAL EXECUTION → SOURCE EVENT LOG → DERIVED POSITION → STRATEGY LOT → DASHBOARD**

The M365 workbook is the operational copy. GitHub records the workbook's identity and provenance rather than silently treating a GitHub snapshot as the live workbook.

When a future workbook export replaces this snapshot, register the new snapshot with its new file hash and preserve the previous record for historical traceability.

## Related project material

- Trading operating runbook: the workbook's event-sourced execution, booking, strategy-lot, and dashboard rules.
- The-Porketo `TRADING/`, `DATA/`, `OPS/`, `EVIDENCE/`, `DECISIONS/`, and `RESEARCH/` areas remain the durable project knowledge surfaces.

## Registration principle

**M365 = operative workbook.**  
**GitHub = versioned project record and provenance.**  
**Live exchange data = current market reality when execution or current pricing is required.**
