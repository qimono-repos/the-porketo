# Operative Trading Workbook

## Current HEAD

**HEAD file:** `TRADE-October-26-Sprint.xlsx`  
**HEAD role:** Current operative trading workbook  
**Current operating surface:** Microsoft 365 / OneDrive  
**GitHub repository:** `qimono-repos/the-porketo`  
**Default branch:** `trunk`  
**HEAD registered:** 2026-10-04

### The baton model

The operative workbook is not permanently tied to Microsoft 365.

The project uses a **moving HEAD / baton** model:

**Excel → LibreOffice/OpenDocument → Google Drive → ...**

At any given moment, one chosen working surface holds the operational baton. That surface is **HEAD** for the current work period.

Today, the baton is held by **Microsoft Excel / Microsoft 365**.

When the workbook is deliberately exported or handed off to another platform, the receiving platform becomes HEAD. The previous platform becomes the predecessor state. The handoff must preserve the workbook state and identify the new HEAD explicitly.

GitHub does not become the operational editor merely because it records the state. GitHub is the durable project record that lets The-Porketo know **which platform currently owns the baton and what exact workbook state was handed over**.

### Microsoft 365 HEAD location

The current HEAD workbook was uploaded to the OneDrive root and confirmed by Microsoft 365:

https://onedrive.live.com/personal/3513c281268a4266/_layouts/15/doc.aspx?resid=75a107fb-5673-44b2-87f3-653b6d18135f&cid=3513c281268a4266

### HEAD identity

- Filename: `TRADE-October-26-Sprint.xlsx`
- Size: 127,852 bytes
- SHA-256: `8aa209c79136eb6744b43a5f85cd42cb51bf39f8d7cfa63d82acafc59afdce8f5909`
- Status: **CURRENT HEAD**
- Platform: **Microsoft Excel / Microsoft 365**

This hash identifies the exact workbook state registered at the moment the baton was assigned to Excel.

### Workbook structure

The HEAD workbook contains 12 worksheets:

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

The workbook is the operative accounting and trading-state artifact while it holds the baton.

The-Porketo repository is the durable project knowledge and provenance layer.

The trading execution chain remains:

**REAL EXECUTION → SOURCE EVENT LOG → DERIVED POSITION → STRATEGY LOT → DASHBOARD**

The current workbook HEAD is therefore the authoritative **bookkeeping state for this handoff**, while live exchange data remains authoritative for current executable market conditions.

### Handoff rule

When the baton moves:

1. Export or transfer the current HEAD workbook.
2. Verify the receiving workbook can be opened and its state is intact.
3. Calculate and record the new workbook identity/hash when available.
4. Update this registry so the receiving platform is marked **HEAD**.
5. Record the predecessor platform and handoff moment.
6. Continue operations from the new HEAD only.

Do not maintain competing operational heads.

### Historical traceability

A former HEAD is not automatically discarded. Its identity can be preserved in GitHub as a handoff record so the project can reconstruct which workbook state was authoritative at each baton pass.

The key distinction is:

**HEAD = where we operate now.**  
**GitHub = where we remember the baton history.**

## Related project material

- Trading operating runbook: event-sourced execution, booking, strategy-lot, and dashboard rules.
- The-Porketo `TRADING/`, `DATA/`, `OPS/`, `EVIDENCE/`, `DECISIONS/`, and `RESEARCH/` areas remain durable project knowledge surfaces.

## Current registration

**M365 / Excel = HEAD.**  
**GitHub = project memory + baton registry.**  
**Live exchange data = current market reality when execution or current pricing is required.**
