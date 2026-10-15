# Installing and running with Guix

[GNU Guix](https://guix.gnu.org/) is a functional package manager that gives
**reproducible, per-user, rollbackable** environments. It is the most
reproducible way to run this sub-project. It works on **Guix System** and as a
**package manager on a foreign distro** (Ubuntu, Debian, Fedora, WSL, etc.).

> Feasibility note: Guix is first-class on GNU/Linux. It also builds for macOS,
> but the Clojure CLI may lag upstream, so on macOS prefer Homebrew unless
> reproducibility is the priority.

---

## 1. Install Guix

### On Guix System

Nothing to do — `guix` is already your package manager. Skip to step 2.

### On a foreign GNU/Linux distro

Option A — distro package (Debian/Ubuntu):

```bash
sudo apt update
sudo apt install -y guix
# enable/start the build daemon
sudo systemctl enable --now guix-daemon
```

Option B — official installer (any distro):

```bash
# download the installer, then:
wget https://git.savannah.gnu.org/cgit/guix.git/plain/etc/guix-install.sh
chmod +x guix-install.sh
sudo ./guix-install.sh
```

Option C — on **Windows/WSL2**: install Ubuntu inside WSL, then use Option A or B.

Confirm:

```bash
guix --version
```

---

## 2. Install the toolchain

The Clojure CLI is provided by the `clojure-tools` package (older Guix releases
may call it `clojure`). Install a JDK and, optionally, `rlwrap`:

```bash
guix install openjdk
guix install clojure-tools      # if unavailable, try: guix install clojure
guix install rlwrap             # optional: nicer `clj` REPL
```

Check:

```bash
java -version
clojure --version        # or: clj --version
```

If `clojure` is not on your `PATH`, open a **new** login shell (Guix edits your
profile) or run `guix install` again — it prints the profile path.

---

## 3. Reproducible ephemeral shell (recommended)

Instead of installing globally, describe the environment once and enter it on
demand. Create a `manifest.scm` in `ft/`:

```scheme
;; ft/manifest.scm
(specifications->manifest
 '("openjdk"
   "clojure-tools"
   "rlwrap"))
```

Then:

```bash
cd ft
guix shell -m manifest.scm -- clojure -M:test
guix shell -m manifest.scm -- clojure -M:run -- --data ../samples/trading_data.csv
```

Guix will build/cache the exact toolchain and drop you into a shell where only
those packages are visible. Nothing is installed permanently.

---

## 4. Pinning an exact environment (optional, advanced)

For byte-for-byte reproducibility across machines, use `guix time-machine` to
pin a channel revision:

```bash
guix time-machine --channels=channels.scm -- shell -m manifest.scm -- clojure -M:run
```

where `channels.scm` pins the Guix revision and package channel. This is the
Guix analogue of committing a lockfile.

---

## 5. Offline use

Guix caches built packages in the store (`/gnu/store`) and, on foreign distros,
downloads substitutes from the build farm. After the first `guix shell`/`guix
install`, subsequent runs are local. Combine with the Clojure dependency cache
(`~/.m2`, `.cpcache/`) for a fully offline setup.

---

## Summary

| Task | Command |
|---|---|
| Install toolchain | `guix install openjdk clojure-tools rlwrap` |
| Ephemeral shell | `guix shell -m manifest.scm` |
| Run tests | `guix shell -m manifest.scm -- clojure -M:test` |
| Run forecast | `guix shell -m manifest.scm -- clojure -M:run -- --data ../samples/trading_data.csv` |
| Roll back | `guix package --list-generations` / `guix package --roll-back` |
