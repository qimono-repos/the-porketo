# File Naming Convention

_Set by Albert, 2026-10-15._

## Rule

**No whitespace in file or folder names.** Use hyphens to separate words.

- Good: `Claude-Code-Team-Meeting-Insights.md`
- Bad: `Claude Code Insights.md`

## Why

Names without spaces are easy to work with in the terminal and scale cleanly to scripts and automation. No quoting or escaping is needed.

## Agent naming pattern

When several agents write parallel files for the same task, prefix each file with the agent name so they don't collide on the shared branch:

- `ChatGpt-Team-Meeting-Insights.md`
- `Claude-Code-Team-Meeting-Insights.md`

## Applies to

Every agent (Claude, ChatGPT, and anyone added later) and every new file in this repo.
