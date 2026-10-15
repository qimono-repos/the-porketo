# Installing on Linux

You need **`uv`** only. It manages the Python interpreter, the virtual
environment, and dependencies.

---

## Debian / Ubuntu

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
# or, if your distro packages uv:
sudo apt update && sudo apt install -y uv
```

## Fedora / RHEL

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
# or:
sudo dnf install -y uv
```

## Arch

```bash
sudo pacman -S uv
```

## Guix

See **`install-guix.md`** — Guix works but `uv` may need to be installed via its
installer inside a `guix shell`; Homebrew/installer is preferred.

---

## Verify

```bash
uv --version
```

`uv` installs its own CPython 3.12; no system Python package (e.g.
`python3-dev`) is required.

## Run

```bash
cd qft
uv sync
uv run pytest
uv run qft --data ../samples/trading_data.csv --horizon 24
```

## Offline

```bash
uv sync --offline        # after the first successful sync
```
