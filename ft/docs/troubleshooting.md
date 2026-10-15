# FT — Troubleshooting

## "Unable to locate a Java Runtime" / `java` not found

The Clojure CLI needs a JDK on `PATH` (and/or `JAVA_HOME`).

- **macOS (Homebrew, keg-only JDK):**
  ```bash
  export JAVA_HOME=/opt/homebrew/opt/openjdk   # Intel: /usr/local/opt/openjdk
  export PATH="$JAVA_HOME/bin:$PATH"
  ```
- **Linux:** install `openjdk-21-jdk` (or your distro's JDK) and ensure
  `java -version` works.
- **Windows:** set `JAVA_HOME` and add `%JAVA_HOME%\bin` to `PATH` (see
  `install-windows.md`).
- **Guix:** `guix install openjdk`, then open a new login shell.

Check with `echo $JAVA_HOME` and `java -version`.

---

## `clojure: command not found`

The Clojure CLI is not installed or not on `PATH`. See the per-OS install docs.
Guix users: `guix install clojure-tools` (or `clojure`), then a new shell.

---

## Dependency download failures (first run, offline)

First run needs network to fetch Commons Math and data.csv. If you are offline:

- Pre-download on a connected machine: `clojure -P`, then copy `~/.m2/repository`
  and the project's `.cpcache/` to the target machine.
- Or use Guix substitutes (see `install-guix.md`).

---

## `FFT length must be a power of two`

You passed a `--window` value that is not a power of two. Use 128, 256, 512,
1024, … The radix-2 FFT cannot use e.g. 1000.
(The default, 512, is fine.)

---

## Forecast looks "flat" or trivially tracks the trend

Too few components. Increase `--k` (e.g. `--k 16`). Conversely, if the forecast
is wild, reduce `--k` — large `k` fits noise and destabilises extrapolation.

---

## `--horizon` implies a window longer than the data

`analyse` needs `total − horizon ≥ window`. With 1024 samples per symbol,
`window + horizon` must be ≤ 1024. If you raise `--window` to 1024 you must lower
`--horizon`.

---

## CSV path errors

Run from the `ft/` directory, or pass an absolute path:

```bash
clojure -M:run -- --data /full/path/to/trading_data.csv
```

---

## Stale classpath / weird resolution

Clear the cache and re-resolve:

```bash
rm -rf .cpcache
clojure -P
```

If you suspect a dependency conflict: `clojure -Stree`.

---

## Tests pass locally but you want verbose output

`clojure -M:test` prints per-namespace results. For a single namespace during
development, use a REPL:

```bash
clj
user=> (require '[clojure.test :as t] 'ft.predict-test)
user=> (t/run-tests 'ft.predict-test)
```
