# 2026-10-16 — XNDU (Xanadu) Binance Stocks purchase

**When:** Fri 16 Oct 2026, 11:56:22 ART (GMT−3; Binance order-history timestamp)  
**Who:** Operator + ChatGPT (research, decision support, journal); Claude will update the Google Sheet  
**Status:** Executed; book update delegated to Claude. This journal records the broker receipt and decision rationale, not a substitute for the canonical trade log.

## Decision and rationale

Add Xanadu Quantum Technologies (XNDU) as another pure-play quantum-computing company, specifically to gain exposure to photonic quantum hardware and the PennyLane software ecosystem.

The project's aim is broader exposure to genuine quantum-computing modalities for the ongoing quantum-learning/portfolio experiment, not exposure to quantum-resistant crypto or general technology companies. Existing quantum-related holdings noted during the discussion were IONQ, QBTS/QBTSB, IBMB, QNTB, RGTI, QUBT, INFQ and ALGO.

Reasons to include XNDU:
- **Pure-play fit:** Xanadu describes itself as a photonic quantum-computing company developing quantum computers using light and software including PennyLane.
- **Software relevance:** PennyLane is an open-source quantum programming platform, a particularly relevant connection to the operator's quantum-computing studies and Python ecosystem.
- **Modality coverage:** photonics adds a distinct hardware approach to the portfolio's quantum narrative. This is not fully new modality diversification because QUBT is also photonics; the incremental distinction is Xanadu's specific company, technology roadmap and PennyLane ecosystem.
- **Venue access:** the operator's CEDEAR broker did not permit fractional Xanadu shares, while Binance Stocks exposed XNDU (EQ_XNDU) for whole-share orders.
- **Micro-investment fit:** the operator's usual allocation increments are USDC 0.75, 1.50 and 2.25. The Binance constraint (whole shares only, minimum 2 shares) forces a larger-than-standard position. The decision was to accept this as an explicit sizing exception rather than pretend it is a normal $0.75 increment.

## Execution — broker order history is authoritative

Source: operator-provided Binance Stocks Order History screenshot, dated 2026-10-16.

- Instrument: XNDU — Xanadu Quantum Technologies Limited Class B Subordinate Voting Shares
- Binance instrument path: https://www.binance.com/en/stocks/EQ_XNDU
- Side / type: Buy / Limit
- Order created / updated: 2026-10-16 11:56:22 (Binance display; interpreted as ART, GMT−3)
- Order limit price: 3.14 USDC
- Filled quantity: **2 XNDU**
- Displayed fill price: **3.12 USDC per share**
- Displayed fee: **0.17 USDC**
- Displayed total debit: **−6.43 USDC**
- Status: **Filled**
- Order ID displayed: e20c8ae1-eddb-48e4-9567-7b8d1762d478

### Reconciliation flag

The displayed fields do not arithmetically reconcile at face value: 2 × 3.12 + 0.17 = 6.41 USDC, while Binance displays a total debit of 6.43 USDC. The receipt's displayed total (−6.43 USDC) is the current execution record and must not be silently overwritten by a reconstructed value. **Claude/bookkeeper: inspect the detailed transaction or wallet history to reconcile the USDC 0.02 difference before treating the book as reconciled.** Do not invent an extra fee or adjustment.

## Allocation math and policy exception

The pre-trade quote shown in the Binance page was around 3.137 USDC per share; the later order-history receipt shows the actual fill at 3.12 USDC. Use the receipt for execution, not the earlier quote.

- Share notional from displayed fill: 2 × 3.12 = 6.24 USDC
- Displayed fee: 0.17 USDC
- Binance displayed total debit: 6.43 USDC (subject to the reconciliation flag above)
- Standard project increment: 0.75 USDC
- 6.43 ÷ 0.75 ≈ 8.57 standard increments
- Nine increments would equal 6.75 USDC, but that is only a sizing comparison, **not** the actual trade cost and not a reason to book the trade as 6.75 USDC.

Record the actual execution as two whole shares and the receipt's total debit. Keep the whole-share minimum as a venue constraint / policy exception. Do not round the real fill to the nearest project increment. The order panel showed minimum 2 and maximum buy 60 shares, with “Whole shares only”; the user reported the same 2-share minimum on the sell side. This does not establish that future buys or sells can be placed in one-share quantities; verify order validation at the time of any later trade.

## Research and thesis

### What Xanadu is
Xanadu's official investor-relations materials describe it as a pure-play photonic quantum-computing company. It develops quantum-computing hardware using light and the PennyLane open-source quantum software platform.

### Technical roadmap (company targets, not verified future outcomes)
On 2026-08-31, Xanadu published a milestone-driven roadmap targeting up to 200 logical qubits by 2029, up to 500 by 2030 and 1,000+ by 2031, alongside a path toward a quantum data center in 2029–2030. These are management targets and remain uncertain.

### Financial condition and risk
Xanadu's Q2 2026 results reported US$312.8 million in cash at 2026-06-30. Its SEC-filed quarterly report reported US$4.343 million revenue for the six months ended 2026-06-30 and US$62.7 million net loss over that six-month period; customer concentration was also disclosed. The company expects further operating losses while it funds R&D and commercialization. Cash provides runway, but it does not eliminate execution risk, future funding needs, dilution risk or the possibility that the technology takes longer than expected to commercialize.

### Valuation interpretation
The decision was **not** based on a claim that XNDU was fundamentally undervalued. The low nominal share price was attractive only in the operational sense that whole-share Binance access made a small position possible. A low per-share price alone does not establish that a company is cheap relative to its value.

### Key risks / thesis invalidation signals to watch
- Photonic hardware and fault-tolerance milestones slip materially versus the published roadmap.
- PennyLane adoption, partnerships or other software activity fail to translate into durable commercial revenue.
- Continued cash burn, new capital raises or share issuance materially dilute holders.
- Customer concentration remains high or revenue growth fails to justify the market valuation.
- The position becomes operationally awkward because the whole-share minimum prevents the intended small staged buys/sells.

## Bookkeeping handoff (Claude)

- Record the actual filled XNDU buy as a new source trade/event in the canonical Google Sheet, using the receipt as the source of truth.
- Preserve: 2 XNDU shares, fill 3.12 USDC/share, fee 0.17 USDC, displayed debit 6.43 USDC, timestamp 2026-10-16 11:56:22, order ID above, status Filled.
- Add an explicit reconciliation note for the USDC 0.02 arithmetic difference; verify against transaction/wallet history rather than inventing a correction.
- Carry the position through the normal chain: **REAL EXECUTION → SOURCE EVENT LOG → DERIVED POSITION → STRATEGY LOT → DASHBOARD**.
- Do not read or edit the Dashboard as the source; it is downstream and should be checked last.
- Mark this lot as a whole-share / minimum-order sizing exception to the regular USDC 0.75 increments. Do not represent the position as a 6.75 USDC fill.
- No sell/harvest has occurred as part of this journal. Future order-size constraints must be verified in Binance at the time of the order.

## Sources

1. Binance XNDU Stocks page and user-provided Order History screenshot (primary execution evidence): https://www.binance.com/en/stocks/EQ_XNDU
2. Xanadu, “Xanadu Announces Technological Roadmap Presentation,” 2026-08-24 (company description and PennyLane): https://investors.xanadu.ai/news-releases/news-release-details/xanadu-announces-technological-roadmap-presentation
3. Xanadu, “Xanadu Charts Path to Over 1,000 Logical Qubits by 2031,” 2026-08-31 (company roadmap and targets): https://investors.xanadu.ai/news-releases/news-release-details/xanadu-charts-path-over-1000-logical-qubits-2031
4. Xanadu, “Xanadu Announces Second Quarter 2026 Results,” 2026-08-05 (cash, operations and business update): https://investors.xanadu.ai/news-releases/news-release-details/xanadu-announces-second-quarter-2026-results
5. SEC, Xanadu Quantum Technologies Limited, quarterly report for period ended 2026-06-30 (financial statements, losses, revenue and customer concentration): https://www.sec.gov/Archives/edgar/data/2097163/000209716326000020/xndu-20260630_d2.htm

---
**Evidence classification:** Fill quantity, fill price, fee, total debit, timestamp, order ID and Filled status are transcribed from the user-provided Binance order-history screenshot. Company/financial/roadmap statements are linked research. The thesis and allocation comparison are analysis. The USDC 0.02 discrepancy remains unresolved.
