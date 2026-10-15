# QFT — Agent briefs

Tailored instructions for AI coding agents working on the **qft** sub-project.
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
   fetch real market data, never place orders. Never run the circuit on real QPU
   hardware (simulator only).
2. **Tests must stay green.** `uv run pytest` → 26 passed.
3. **Spec-driven.** Work from `../specs/BACKLOG.md`; add/refresh the iteration
   spec before adding a feature.
4. **No new dependencies without a spec entry.** `pyproject.toml` currently has
   three runtime libraries (see `../docs/libraries.md`); `uv.lock` is committed.
5. **Preserve the report contract.** `uv run qft` must print one block per symbol
   and `--out` must emit valid JSON.
6. **Keep the quantum/classical parity.** For equal parameters, the metrics must
   equal the `ft` sub-project's. `tests/test_predict.py` enforces this within the
   project; `../specs/TRACEABILITY.md` records the cross-project evidence.

## Files an agent usually touches

- `src/qft/*.py` — implementation
- `tests/test_*.py` — verification
- `specs/*` — the spec you are implementing
- `docs/*` — update if the CLI or behavior changes
