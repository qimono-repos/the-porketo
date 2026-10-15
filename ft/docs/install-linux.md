# Installing on Linux

You need a **JDK 17+** and the **Clojure CLI**. `rlwrap` is optional but makes
the `clj` REPL nicer.

---

## Debian / Ubuntu

```bash
sudo apt update
sudo apt install -y openjdk-21-jdk rlwrap

# Clojure CLI (distro packages are often too old; use the official script)
curl -L -O https://github.com/clojure/brew-install/releases/latest/download/linux-install.sh
chmod +x linux-install.sh
sudo ./linux-install.sh
```

A newer JDK: `sudo apt install openjdk-21-jdk` (Debian 12/Ubuntu 24.04) is
enough. If `java -version` shows an old JDK, set `JAVA_HOME` to the 21 install
(e.g. `/usr/lib/jvm/java-21-openjdk-amd64`).

## Fedora / RHEL

```bash
sudo dnf install -y java-21-openjdk-devel rlwrap
sudo dnf install -y clojure     # may be old; official script also works
```

## Arch

```bash
sudo pacman -S jdk-openjdk clojure rlwrap
```

## Guix

If you use Guix (Guix System or Guix as a package manager on another distro),
see **`install-guix.md`** — it is the most reproducible option:

```bash
guix install clojure openjdk rlwrap
```

---

## Verify

```bash
java -version
clojure --version
```

## Run

```bash
cd ft
clojure -P
clojure -M:test
clojure -M:run -- --data ../samples/trading_data.csv --horizon 24
```
