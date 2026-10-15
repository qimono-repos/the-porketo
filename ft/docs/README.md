# FT — Documentation

Offline documentation for the **ft** (Fourier-transform price-prediction)
Clojure sub-project. Everything here is designed to be read on a machine with
**no internet access** once the toolchain is installed.

## Contents

| Doc | What it covers |
|---|---|
| [install-windows.md](install-windows.md) | Windows 10/11 (native, Scoop, Chocolatey, WSL) |
| [install-macos.md](install-macos.md) | macOS (Homebrew, official installer) |
| [install-linux.md](install-linux.md) | Debian/Ubuntu, Fedora, Arch |
| [install-guix.md](install-guix.md) | Guix (Guix System *and* Guix on a foreign distro) |
| [run.md](run.md) | How to run, every CLI flag, and the algorithm step by step |
| [libraries.md](libraries.md) | Every library used, in detail, with API notes |
| [troubleshooting.md](troubleshooting.md) | Common errors and fixes |

## The toolchain in one sentence

**FT needs a JDK (Java 17+) and the Clojure CLI (`clojure`).** That is all. The
Clojure libraries (Commons Math, data.csv) are fetched automatically by the CLI
on first run and cached under `~/.m2` and `.cpcache/`.

## Zero-network reproducibility

After the first successful dependency resolution, the project runs offline.

```bash
# first time (needs network once):
clojure -P                     # download and cache all deps

# thereafter (no network needed):
clojure -M:test
clojure -M:run -- --data ../samples/trading_data.csv
```

If you must move the project to an air-gapped machine, copy the Maven cache
(`~/.m2/repository`) and the project's `.cpcache/` directory along with the
source, then run `clojure -M:run` directly.
