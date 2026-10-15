# Installing and running with Guix

[GNU Guix](https://guix.gnu.org/) is a functional package manager that gives
**reproducible, per-user, rollbackable** environments. It is first-class on
GNU/Linux and also builds for macOS.

> **Feasibility note:** this sub-project's toolchain is **`uv` + Python**, which
> is *not* the strongest fit for Guix — Guix prefers to build Python packages
> from source with its own `python-build-system`, whereas `uv` downloads pinned
> binary wheels. Two workable approaches are given below; the **ephemeral
> `uv`** approach is what we recommend, because it keeps the exact dependency
> set that `uv.lock` records.

---

## 1. Install Guix

### On Guix System

`guix` is already the package manager. Skip to step 2.

### On a foreign GNU/Linux distro

Option A — distro package (Debian/Ubuntu):

```bash
sudo apt update
sudo apt install -y guix
sudo systemctl enable --now guix-daemon
```

Option B — official installer (any distro):

```bash
wget https://git.savannah.gnu.org/cgit/guix.git/plain/etc/guix-install.sh
chmod +x guix-install.sh
sudo ./guix-install.sh
```

Option C — on **Windows/WSL2**: install Ubuntu inside WSL, then use A or B.

Confirm:

```bash
guix --version
```

---

## 2. Recommended: Guix for isolation, `uv` for Python

Provide `uv` inside an ephemeral Guix shell, then let `uv` manage Python and the
wheels. This keeps Guix responsible for the outer environment while `uv.lock`
pins the Python side. Create a `manifest.scm` in `qft/`:

```scheme
;; qft/manifest.scm
(specifications->manifest
 '("uv"           ; if this package exists in your Guix revision
   "curl"
   "gcc-toolchain"))
```

Then:

```bash
cd qft
guix shell -m manifest.scm -- uv sync
guix shell -m manifest.scm -- uv run pytest
guix shell -m manifest.scm -- uv run qft --data ../samples/trading_data.csv
```

If `uv` is **not** available in your Guix revision, install it *inside* the
ephemeral shell with the official installer:

```bash
guix shell -m manifest.scm -- bash -c 'curl -LsSf https://astral.sh/uv/install.sh | sh && ~/.local/bin/uv sync'
```

---

## 3. Alternative: pure Guix Python environment

If you must avoid `uv` entirely, build the environment from Guix packages. The
versions will be whatever Guix ships, so they may differ from `uv.lock`:

```bash
guix install python python-pytest python-numpy
```

Qiskit and Qiskit-Aer are not in Guix as of this writing, so a pure-Guix run
would need `guix shell` + `pip` inside a throwaway venv:

```bash
guix shell -m manifest.scm -- bash -c '
  python -m venv .venv && . .venv/bin/activate &&
  pip install -r requirements.txt &&   # if you export one from uv
  python -m pytest'
```

For reproducible results, prefer the `uv` approach in step 2.

---

## 4. Pinning an exact environment (optional, advanced)

Pin the Guix revision with `guix time-machine`, exactly analogous to committing a
lockfile:

```bash
guix time-machine --channels=channels.scm -- shell -m manifest.scm -- \
  uv run qft --data ../samples/trading_data.csv
```

Combine this with the committed `uv.lock` for a fully pinned stack:
Guix pins the outer tools, `uv.lock` pins the Python packages.

---

## 5. Offline use

Guix caches builds in `/gnu/store`; `uv` caches wheels in `~/.cache/uv`. After
the first run, combine `guix shell -m manifest.scm -- uv sync --offline` for a
network-free setup.

---

## Summary

| Task | Command |
|---|---|
| Outer shell | `guix shell -m manifest.scm` |
| Install Python deps | `uv sync` (inside the shell) |
| Run tests | `guix shell -m manifest.scm -- uv run pytest` |
| Run forecast | `guix shell -m manifest.scm -- uv run qft --data ../samples/trading_data.csv` |
| Roll back Guix | `guix package --list-generations` / `guix package --roll-back` |
