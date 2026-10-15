# QFT — Documentation

Offline documentation for the **qft** (Quantum Fourier Transform
price-prediction) Python sub-project. Everything here is meant to be read on a
machine with **no internet access** once the toolchain is installed.

## Contents

| Doc | What it covers |
|---|---|
| [install-windows.md](install-windows.md) | Windows 10/11 (native PowerShell, winget, WSL) |
| [install-macos.md](install-macos.md) | macOS (Homebrew, the standalone `uv` installer) |
| [install-linux.md](install-linux.md) | Debian/Ubuntu, Fedora, Arch |
| [install-guix.md](install-guix.md) | Guix (Guix System *and* Guix on a foreign distro) |
| [run.md](run.md) | How to run, every CLI flag, and the algorithm step by step |
| [libraries.md](libraries.md) | Every library used, in detail, with API notes |
| [troubleshooting.md](troubleshooting.md) | Common errors and fixes |

## The toolchain in one sentence

**QFT needs only [`uv`](https://docs.astral.sh/uv/).** `uv` installs and manages
the right **Python 3.12** for you, creates the virtual environment, and installs
the pinned dependencies (Qiskit, Qiskit Aer, NumPy) — you do **not** need a
system Python.

## Zero-network reproducibility

Reproducibility comes from the committed lockfile, `uv.lock`. After the first
successful sync, the project runs offline.

```bash
# first time (needs network once):
uv sync                     # creates .venv, downloads Python 3.12 + deps

# thereafter (no network needed):
uv run pytest
uv run qft --data ../samples/trading_data.csv --horizon 24
```

`uv sync` respects `uv.lock`, so every machine resolves the **exact same**
package versions. If you must move the project to an air-gapped machine, copy the
`uv` cache (`~/.cache/uv` on Linux, `~/Library/Caches/uv` on macOS,
`%LOCALAPPDATA%\uv\cache` on Windows) plus the project (including `uv.lock`),
then run with `uv sync --offline`.

> Why a lockfile? `pyproject.toml` states *ranges* (`qiskit>=1.0`); `uv.lock`
> pins the *resolved* versions (currently `qiskit 2.5.2`, `qiskit-aer 0.17.2`,
> `numpy 2.5.4`) so results are bit-for-bit reproducible.
