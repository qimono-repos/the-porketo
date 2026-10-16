# 2026-10-16 — Binance quantum-stock chase closed: HQ not added

**When:** Fri 16 Oct 2026, approx. 12:15 ART (GMT−3)  
**Status:** Research/order-sizing review only; **no HQ order was submitted**.

## Decision

Skip Horizon Quantum Holdings Ltd. (HQ) on Binance Stocks for this sprint. The order panel identifies the instrument as “Horizon Quantum Holdings Ltd. Class A Ordinary Shares,” with a displayed price around USDC 13.353 and “Whole shares only” / minimum 1 share. Fractional-share trading is unavailable for this instrument.

The issue is not simply that HQ's nominal share price is high. The minimum whole-share position is too large for Qimono's USDC 0.75 micro-allocation convention. One share at the displayed limit price of USDC 13.37 would consume roughly 18 standard units before fees:

- 17 units = 17 × USDC 0.75 = USDC 12.75, insufficient for one share.
- 18 units = 18 × USDC 0.75 = USDC 13.50, only USDC 0.13 above the USDC 13.37 limit price before fees.
- Because fees could push the total above the USDC 13.50 target, this does not provide a clean fit to the model.
- A fractional position would be preferable for the small-ticket strategy, but Binance's order panel says whole shares only.

**Conclusion: let HQ go for now.** Do not submit an order. This is an operational sizing decision, not a negative judgment about the company's technology or future.

## Why this closes the Binance quantum-stock search episode

The operator's aim was to expand exposure to pure quantum-computing companies available through Binance, while keeping position sizing compatible with Qimono's small-ticket model. During this episode:

- **XNDU (Xanadu)** was purchased: 2 whole shares, because Binance required a minimum of 2 whole shares. Binance order history shows a 3.12 USDC fill per share, a 0.17 USDC fee and a displayed total debit of 6.43 USDC. Its whole-share minimum makes it a deliberate sizing exception; the 0.02 USDC difference between displayed arithmetic and total remains flagged for reconciliation in the XNDU journal.
- **PSQL** was purchased as a fractional-share order: 0.868 shares filled at 5.84 USDC per share, fee 0.17 USDC, displayed total debit 5.24 USDC. The sizing calculation targeted seven USDC 0.75 units (USDC 5.25) and reserved the estimated fee before calculating share quantity. The PSQL journal separately flags that its quantum eligibility is unverified; do not classify it as a pure-quantum holding without further evidence.
- **HQ** was evaluated but not purchased because whole-share-only trading makes the smallest position too large and awkward for the USDC 0.75 unit model.

This closes the **current Binance-side search episode**, not a permanent ban on future research. Reopen only if Binance adds fractional trading, the instrument price/order constraints change enough to fit the policy, or the project's allocation rules are deliberately revised.

## Research/eligibility caveat

The screenshot supports the displayed name and trading constraints, not the full business thesis. This note does not independently establish HQ's eligibility as a pure-play quantum company. The decision does not depend on resolving that classification because the operational sizing constraint alone is sufficient to skip the trade.

## Bookkeeping / project handling

- **No HQ trade row, position, strategy lot or execution event should be created.** There is no execution receipt because no order was placed.
- This is a research/decision journal only.
- Keep actual execution data separate from sizing targets and analysis.
- The two completed purchases (XNDU and PSQL) have separate journal entries and should be reconciled/booked by Claude in the canonical Google Sheet.
- Preserve the operating chain for executed trades: **REAL EXECUTION → SOURCE EVENT LOG → DERIVED POSITION → STRATEGY LOT → DASHBOARD**. Read the Dashboard last.

## Evidence

- Operator-provided Binance Stocks screenshot for HQ at https://www.binance.com/en/stocks/EQ_HQ (displayed price approximately USDC 13.353; limit price field USDC 13.37; minimum 1; whole shares only).
- XNDU completed-order evidence is recorded in [the XNDU purchase journal](2026-10-16-xndu-xanadu-binance-stocks-purchase.md).
- PSQL completed-order evidence is recorded in [the PSQL purchase journal](2026-10-16-psql-binance-stocks-purchase.md).

**Evidence classification:** HQ trading constraints are transcribed from the user-provided screenshot; unit comparisons are calculations; the skip decision is the operator's policy choice. No HQ execution occurred.
