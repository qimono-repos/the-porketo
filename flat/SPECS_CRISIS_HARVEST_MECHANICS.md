# Crisis Harvest Mechanics

## Purpose

Define the mechanics used when the project reaches a **CRITICAL: FINAL HARVEST DAY** condition and no normal harvest has occurred by market close.

## Core Selection Rule

The crisis candidate is selected from the **strategy lots**, not from the aggregate wallet balance.

At the crisis decision point:

1. Evaluate every open stock and crypto strategy lot that has **not reached its harvest threshold**.
2. For each lot, calculate the remaining gap to its harvest threshold in the common USD/USDC-equivalent management currency.
3. Select the lot with the **smallest positive absolute dollar gap** to its harvest threshold.
4. Do not select by ticker aggregate, percentage distance, or total wallet position.
5. Preserve the strategy-lot identity and its immutable material anchor.

The Harvest Threshold is the lot's Material Anchor plus its target profit. Crossing the threshold creates a harvest signal; the crisis mechanism is the exception that can act on a lot that remains below threshold.

## Crisis Movement

The crisis movement is a **liberation of the selected lot's material anchor**, not a disposal of the entire asset.

The standard crisis movement is:

- Sell/convert **90% of the selected lot's material anchor**.
- Leave **10% of that material anchor** invested in the same strategy lot.
- Keep the lot identity and its material anchor unchanged in the strategy record.
- Calculate the native asset quantity to enter in Binance's **FROM** field from the 90% anchor amount using the executable quote available for the notification snapshot.
- The notification quantity is calculated at the crisis notification snapshot and is the actionable quantity for execution.

This means the protocol does **not** sell 90% of the wallet's total asset balance and does not merge separate strategy lots.

## Execution Robustness

If the position available at execution is smaller than the native quantity specified in the crisis notification, execute the entire remaining position rather than canceling the crisis movement.

The final Binance Preview/receipt is execution truth. A planned movement is not booked as a trade until the broker/exchange confirms it.

## Required Notification

Every actionable crisis notification must use the Binance-ready move grid:

| # | Binance move | TYPE IN “FROM” | Approx. USDC harvested / spent | Anchor left invested |
|---|---|---|---:|---:|
| 1 | ASSET → USDC | exact native quantity | ≈ 90% of anchor | 10% of anchor |

The notification must also identify the selected strategy lot and show:

**ASSET @ entry price (position X of N) | Current value | Anchor | Gap to harvest threshold**

The notification title is:

**🚨 CRITICAL: FINAL HARVEST DAY 🚨**

The notification must make the crisis movement explicit and include the exact native quantity to type into Binance's FROM field.

## Example From the Current Crypto Sprint Snapshot

TAO @ $240.80 is a concrete example of the selection logic. Its material anchor is $4.98456 USDC, current market value is $4.993769716 USDC, and harvest threshold is $4.99456 USDC. Its absolute gap to threshold is approximately $0.000790284 USDC, making it the closest below-threshold lot in that snapshot.

For the crisis movement:

- 90% of anchor = $4.486104 USDC.
- 10% of anchor left invested = $0.498456 USDC.
- Using the snapshot price of $264.529938 USDC/TAO, the native FROM quantity is approximately 0.016958776 TAO.

The example notification therefore identifies:

**TAO @ $240.80 (position 3 of 3)**

and instructs:

**TYPE IN “FROM”: 0.016958776 TAO**

This example is a mechanics example, not a permanent instruction to select TAO. Candidate selection must be recomputed from the current snapshot every time the crisis rule activates.

## Relationship to Normal Harvesting

Normal harvesting remains threshold-driven and opportunistic. Crisis harvesting is an anti-stagnation exception activated only after the project's final-harvest-day condition has been reached and the normal harvesting window has ended.

Separate strategy lots remain separate throughout the process.
