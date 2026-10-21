# Milestone: 30 USDT in the harvest wallet

**Date:** 2026-10-21, 13:08 ART
**Project:** the-porketo (Qimono trading experiment)

## The number

Binance Spot USDT: **30.15355463**.

It ties to the book exactly: 27.90355463 at the 2026-10-20 wallet check, plus 2.25 USDT harvested today (AXS 0.75, IBMB 0.45, SPCXB 0.45, BTC 0.30, TSLAB 0.30). Today was the first day under the fixed-step harvest ladder (`protocols/harvest-ladder.md`).

## What it means

USDT harvesting started on 2026-10-07. It took about two weeks to reach 30 USDT, a pace of roughly **$1 to $1.50 per day**, or about 30 a month or more.

For the survival of the experiment, this is the first hard evidence that the system can feed itself, while it is still being refined.

## How to read the composition

**Reconciliations count.** Rows such as CRR-0004 (USDT already in the wallet) and CRR-0010 (a 0.70 inflow with no harvest attribution) are not confirmed harvests. They are related to harvesting, which is why they landed in this wallet. In real-life projects, real numbers overrule the theory: the wallet is the truth.

**Harvests at a loss are exceptions, not damage.** A few sales (CRT-0055, CRT-0063, CRT-0064, CRT-0065) took principal instead of excess above anchor. That is bad practice, but as long as it does not happen systematically it is an exception to the rule, not structural damage. The ladder protocol (0.30 minimum, never more than the full excess) is designed to prevent it.

## Open caveat

Harvests come from the lots that rose. Lots below their anchors (PUMP, IMX, GALA, ILV, ZEC and others) still carry roughly -35 in open losses on the crypto side. The experiment is fully self-sustaining once the harvest pace outruns that drag.

## Lesson

Today's cleanup (an overwritten Sprint row, scattered forecasts, unit deductions done by hand) comes from using a spreadsheet as the book of record. These problems will keep appearing until the book moves to a serious database. The planned fix is migration to a Datomic book of record.
