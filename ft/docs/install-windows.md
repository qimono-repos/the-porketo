# Installing on Windows

Two things are needed: a **JDK** and the **Clojure CLI**. Pick one of the
options below. If you prefer a Unix-like environment, use the **WSL** option and
then follow the Linux (or Guix) guide — the commands in this project assume a
POSIX shell, so WSL or Git Bash is the smoothest path.

---

## 1. A JDK

### Option A — winget (built into Windows 10/11)

```powershell
winget install EclipseAdoptium.Temurin.21.JDK
```

### Option B — Microsoft Build of OpenJDK

```powershell
winget install Microsoft.OpenJDK.21
```

### Option C — Chocolatey / Scoop

```powershell
choco install temurin21        # or: scoop install temurin21-jdk
```

### Set `JAVA_HOME`

Find the install directory (e.g. `C:\Program Files\Eclipse Adoptium\jdk-21...`),
then:

```powershell
setx JAVA_HOME "C:\Program Files\Eclipse Adoptium\jdk-21.0.x-hotspot"
setx PATH "%JAVA_HOME%\bin;%PATH%"
```

Open a **new** terminal and confirm:

```powershell
java -version
```

---

## 2. The Clojure CLI

### Option A — Scoop (recommended on Windows)

```powershell
scoop install clojure
```

### Option B — Chocolatey

```powershell
choco install clojure
```

### Option C — official installer (PowerShell)

Follow the official guide: <https://clojure.org/guides/install_clojure>
(the Windows installer is a PowerShell script). The `clojure` command lands on
your `PATH`.

Verify:

```powershell
clojure --version
```

---

## 3. Run the project (Git Bash or WSL)

The example commands use a POSIX shell. In **Git Bash** (ships with Git for
Windows):

```bash
cd ft
clojure -P
clojure -M:test
clojure -M:run -- --data ../samples/trading_data.csv --horizon 24
```

In **PowerShell** the same commands work, but path separators and `--` parsing
are identical; just use `..\samples\trading_data.csv`.

---

## 4. WSL (recommended if you want Guix)

```powershell
wsl --install -d Ubuntu
```

Then, inside Ubuntu, follow `install-linux.md` or `install-guix.md`. Guix works
well inside WSL2.
