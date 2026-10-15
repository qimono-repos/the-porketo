# FT — Agent briefs

Tailored instructions for AI coding agents working on the **ft** sub-project.
Each file points at the same source of truth but is written for that agent's
conventions.

| File | Agent | Convention it matches |
|---|---|---|
| [claude-code.md](claude-code.md) | Claude Code | `CLAUDE.md`-style project brief |
| [openai-codex.md](openai-codex.md) | OpenAI Codex | `AGENTS.md`-style project brief |
| [gemini.md](gemini.md) | Gemini CLI | `GEMINI.md`-style project brief |
| [grok.md](grok.md) | Grok | general agent brief |

## Shared invariants (all agents)

1. **Synthetic data only.** `../../samples/trading_data.csv` is dummy data. Never
   fetch real market data, never place orders.
2. **Tests must stay green.** `clojure -M:test` → 0 failures / 0 errors.
3. **Spec-driven.** Work from `../specs/BACKLOG.md`; add/refresh the iteration
   spec before adding a feature.
4. **No new dependencies without a spec entry.** `deps.edn` currently has three
   libraries (see `../docs/libraries.md`).
5. **Preserve the report contract.** `clojure -M:run` must print one block per
   symbol and `--out` must emit valid JSON.

## Files an agent usually touches

- `src/ft/*.clj` — implementation
- `test/ft/*_test.clj` — verification
- `specs/*` — the spec you are implementing
- `docs/*` — update if the CLI or behavior changes
