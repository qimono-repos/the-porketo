# Installing on Windows

Only one tool is required: **`uv`**. It manages Python for you, so you do **not**
need a separate Python install.

---

## 1. Install `uv`

### Option A — winget (built into Windows 10/11)

```powershell
winget install --id=astral-sh.uv -e
```

### Option B — PowerShell installer

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Option C — Scoop / Chocolatey

```powershell
scoop install uv
# or
choco install uv
```

Open a **new** terminal and confirm:

```powershell
uv --version
```

---

## 2. Run the project (PowerShell)

The example commands are cross-platform; use `\` path separators on Windows:

```powershell
cd qft
uv sync
uv run pytest
uv run qft --data ..\samples\trading_data.csv --horizon 24
```

`uv sync` downloads a managed CPython 3.12 and the locked wheels into the
project's `.venv\`, then caches them.

---

## 3. WSL (recommended for a POSIX shell)

```powershell
wsl --install -d Ubuntu
```

Inside Ubuntu, run the PowerShell alternative (Option B) or follow
`install-linux.md` / `install-guix.md`. The rest of this project's commands
assume a POSIX shell, so WSL or Git Bash is the smoothest path.

---

## 4. Notes

- The first `uv sync` needs network access (Python + wheels). Afterwards you can
  use `uv sync --offline`.
- If a corporate proxy blocks downloads, set `HTTPS_PROXY` before running `uv`.
