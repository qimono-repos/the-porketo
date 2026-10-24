# Harvest threshold raised to anchor + 0.60; column renamed

**Date:** 2026-10-24, ~13:45 Paramaribo/Halifax (GMT−3)
**Decided by:** Albert (operator). Applied in the book by Claude.
**Book:** TRADE-October-26-Sprint (`1X5JbgerRy5gv6uttPw3dOlw3Dj-qXfmOBDKlx1vX9V0`)

## What changed in the book

| Page | Column (title) | Cells | Before | After |
|---|---|---|---|---|
| Sprint | P "Target profit ($)" → **"Min excess to harvest ($)"** | P3:P61 (header P2) | 0.10 (September lots) / 0.01 (newer lots) | **0.60** on every lot row |
| Crypto Sprint | J "Target profit (USDC)" → **"Min excess to harvest (USDC)"** | J6:J48 (header J5) | 0.01 | **0.60** on every lot row |
| Crypto Sprint | K "Harvest threshold (USDC)" | K35 (SOL @ 111.369), K36 (ALGO @ 0.118955) | typed constant 0.76 | formula `=D35+J35`, `=D36+J36`, like the rest of the column |

Column Q "Harvest threshold ($)" on page Sprint and column K on page Crypto Sprint were not touched: they stay `= anchor + min excess` and recalculated on their own. Example: page Sprint, cell Q15 (OKLO row #9, Lemon) moved from 10.05 to **10.55**, which is a price of about 42.68.

## Why

The threshold column was a leftover from before the harvest ladder.

- The September convention was "harvest at anchor + 0.10"; later lots used + 0.01 (the "global crypto harvest trigger is now +0.01 USDC" note on the ETH lot).
- Since the ladder amendment of 2026-10-24 (`protocols/harvest-ladder.md`, "never round up past 50%"), no harvest is possible below **0.60 excess**: the smallest step is 0.30 and it may not exceed 50% of the excess.
- So the book flagged lots as ready at +0.01 to +0.10 when nothing could actually be sold. That noise hid the real candidates and made "Harvest ready" useless.

After the change, the threshold column matches the operating rule: a lot over its threshold has at least one ladder step that fits. On 24 Oct the only stock lots over it were CVX (row #8, excess ≈ 0.90) and the two DUKB lots (#17 ≈ 0.91, #40 ≈ 0.85, sell pending for the DUKB migration).

## Why the rename

"Target profit" read as a profit goal. The number is a floor: the minimum excess a lot needs before the ladder allows any harvest. "Min excess to harvest" says that.

## Not changed

- Material anchors, units, harvest history: untouched.
- The 50% rule and the ladder itself: unchanged. This only aligns the book with them.
- Known open issue, not fixed here: Dashboard "Harvest ready" and "Open P/L" still show `#REF!`, and Crypto Sprint B2 "Budget" and J2 "Harvest ready" too.

## Precedent

If the ladder's minimum step changes, this column must change with it: min excess = 2 × smallest ladder step.
