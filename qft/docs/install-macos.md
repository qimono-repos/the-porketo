# Installing on macOS

## 1. `uv` (recommended)

`uv` is a single Rust binary that manages Python versions, virtual environments,
and dependencies. It replaces `pyenv` + `venv` + `pip` + `pip-tools`.

```bash
# Homebrew
brew install uv

# or the standalone installer (no Homebrew)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify:

```bash
uv --version
```

You do **not** need to install Python yourself — `uv` will fetch a managed
CPython 3.12 the first time you sync (`uv python install 3.12` does it
explicitly if you prefer).

> Apple-silicon vs Intel: `uv` ships native binaries for both; no path tweaks
> needed.

## 2. Run

```bash
cd qft
uv sync
uv run pytest
uv run qft --data ../samples/trading_data.csv --horizon 24
```

`uv sync` creates `.venv/` and installs the locked dependencies. The first run
downloads Python 3.12 and the wheels; afterwards everything is local.

## 3. Guix on macOS

Guix runs on macOS but its Python/`uv` packaging may lag upstream, so Homebrew
(or the standalone installer) is preferred here. See `install-guix.md`.

## 4. Optional: make I/O offline-safe

```bash
uv sync --offline        # after the first sync, no network needed
```
