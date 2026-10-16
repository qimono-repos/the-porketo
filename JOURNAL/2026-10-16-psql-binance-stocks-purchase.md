# 2026-10-16 — PSQL (Pioneer Acquisition Corp. II) Binance Stocks purchase

**When:** Fri 16 Oct 2026, 12:12:14 ART (GMT−3; Binance Order History display)  
**Who:** Operator + ChatGPT (allocation math and journal); Claude will handle the Google Sheet  
**Status:** Executed; the broker receipt is the execution source of truth.

## Decision and rationale

Add a small PSQL position through Binance Stocks because the interface supports fractional-share orders, unlike the whole-share-only XNDU order. The purpose of the sizing exercise was to keep the allocation as close as practical to Qimono's standard USDC 0.75 increments, while respecting the platform's minimum order and fee.

**Important instrument distinction:** PSQL is displayed by Binance as “Pioneer Acquisition Corp. II Class A Ordinary Shares.” The screenshot alone does not establish that this is a pure quantum-computing operating company. Do not classify it as a pure-play quantum holding without separately verifying the underlying company, transaction/business purpose, and project eligibility criteria. This journal records the executed trade and sizing rationale, not a verified quantum thesis.

## Execution — Binance order-history screenshot

- Instrument: PSQL — Pioneer Acquisition Corp. II Class A Ordinary Shares
- Binance instrument page shown during order: https://www.binance.com/en/stocks/EQ_BBCQ
- Side / type: Buy / Limit
- Order timestamp: 2026-10-16 12:12:14 (Binance display; interpreted as ART, GMT−3)
- Limit price: 5.85 USDC
- Filled quantity: **0.868 PSQL**
- Displayed execution price: **5.84 USDC per share**
- Displayed fee: **0.17 USDC**
- Displayed total debit: **−5.24 USDC**
- Status: **Filled**
- Order ID displayed: **12738c8-96db-4a1d-a022-ec67919338e9** (transcribed from screenshot; verify exact string if using as a unique key)

The screenshot is the source for the quantity, execution price, fee, total debit, timestamp and filled status. Preserve the displayed total debit rather than substituting a recomputed number.

## Sizing math and rationale

### 1. Qimono's standard increment

The project's normal micro-investment units are:
- 1 unit = USDC 0.75
- 2 units = USDC 1.50
- 3 units = USDC 2.25

The nearest practical target around Binance's approximately USDC 5 minimum is **7 units**:

7 × USDC 0.75 = **USDC 5.25 target allocation**

This is a target budget for the sizing exercise, not the execution amount.

### 2. Include the estimated fee before converting budget to shares

At the time of the preview:
- Limit price = USDC 5.85 per share
- Estimated fee = USDC 0.17
- Target total budget = USDC 5.25

Budget available for the share notional after reserving the estimated fee:

USDC 5.25 − USDC 0.17 = **USDC 5.08**

Estimated share quantity at the limit price:

USDC 5.08 ÷ USDC 5.85 per share = **0.868376... shares**

The entered quantity was **0.868 shares** (rounded down to three decimal places), giving estimated notional:

0.868 × USDC 5.85 = **USDC 5.0778**, approximately USDC 5.08.

Adding the preview's estimated fee:
USDC 5.0778 + USDC 0.17 = **USDC 5.2478**, approximately **USDC 5.25**.

### 3. Actual fill versus target

The order-history receipt reports:
- 0.868 shares filled at USDC 5.84 = 0.868 × 5.84 = **USDC 5.06912** share notional
- Displayed fee = **USDC 0.17**
- Displayed total debit = **USDC 5.24**

The displayed fee plus share notional equals USDC 5.23912, which rounds to USDC 5.24. The displayed total is therefore arithmetically consistent to the cent with the receipt's price and quantity.

Compared with the seven-unit target:
- Target: USDC 5.25
- Actual displayed debit: USDC 5.24
- Difference: **−USDC 0.01**
- Equivalent standard units: USDC 5.24 ÷ USDC 0.75 ≈ **6.987 units**

The fill landed approximately one cent below the seven-unit target. This is a good fit to the allocation convention while recording the actual execution rather than forcing the bookkeeping amount to USDC 5.25.

## Interpretation and controls

- The seven-unit number was used as a **budget target**. It was not the number to enter into Binance's shares field.
- The shares field required a fractional share quantity. We reserved the preview's estimated fee, divided the remaining budget by the limit price, and rounded the share quantity down to 0.868.
- The actual trade was filled; this is not merely a preview.
- Record actual shares, actual execution price, actual fee, displayed debit, timestamp and order ID in the canonical book.
- Do not overwrite the real debit with the USDC 5.25 target. The target is analytical metadata only.
- Before classifying this as a quantum holding, verify what PSQL represents and whether it qualifies under the project's “pure quantum” inclusion rule. The instrument name and screenshot alone do not establish that.

## Bookkeeping handoff (Claude)

- Append the executed PSQL buy to the canonical Google Sheet as a source event, using the Binance receipt.
- Record 0.868 PSQL, execution price 5.84 USDC/share, fee 0.17 USDC, displayed total debit 5.24 USDC, timestamp 2026-10-16 12:12:14, order ID as shown, status Filled.
- Record target sizing metadata separately: 7 × 0.75 = USDC 5.25; actual displayed debit is USDC 5.24.
- Do not book a fictional USDC 5.25 execution.
- Apply the normal data chain: **REAL EXECUTION → SOURCE EVENT LOG → DERIVED POSITION → STRATEGY LOT → DASHBOARD**. Verify upstream formulas/ranges after structural changes and inspect the Dashboard last.
- Keep quantum eligibility unresolved until independently verified.

## Evidence classification

**Execution evidence:** user-provided Binance Stock Order History screenshot.  
**Sizing calculation:** derived from the project's USDC 0.75 increment, the order preview's USDC 5.85 limit price and estimated USDC 0.17 fee, then checked against the final receipt.  
**Quantum classification:** unverified; do not infer from the ticker or this order screenshot.

