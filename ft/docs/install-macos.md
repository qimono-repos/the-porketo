# Installing on macOS

## 1. Homebrew (recommended)

```bash
# JDK (keg-only) and the Clojure CLI
brew install openjdk
brew install clojure/tools/clojure
```

Homebrew's `openjdk` is **keg-only**, so the `java` launcher does not use it by
default. Point `JAVA_HOME` at it (Apple-silicon path shown; Intel is
`/usr/local/opt/openjdk`):

```bash
echo 'export JAVA_HOME=/opt/homebrew/opt/openjdk' >> ~/.zshrc
echo 'export PATH="$JAVA_HOME/bin:$PATH"'        >> ~/.zshrc
source ~/.zshrc
```

Verify:

```bash
java -version
clojure --version
```

> If a system `/usr/libexec/java_home` exists, you may instead use
> `export JAVA_HOME=$(/usr/libexec/java_home)`.

## 2. Official installer (no Homebrew)

Install a JDK (Temurin, Zulu, or Oracle) from the vendor, then install the
Clojure CLI:

```bash
curl -L -O https://github.com/clojure/brew-install/releases/latest/download/posix-install.sh
chmod +x posix-install.sh
sudo ./posix-install.sh
```

## 3. Guix on macOS

Guix runs on macOS but is less common and may not provide the newest Clojure
CLI. Native Homebrew is preferred here; see `install-guix.md` if you want it.

## 4. Run

```bash
cd ft
clojure -P
clojure -M:test
clojure -M:run -- --data ../samples/trading_data.csv --horizon 24
```
