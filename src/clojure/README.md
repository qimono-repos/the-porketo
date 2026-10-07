# Clojure harvest calculator

```text
src/clojure/
├── deps.edn
└── src/
    └── qimono/
        └── harvest.clj
```

Start a REPL:

```bash
cd src/clojure
clj
```

Then:

```clojure
(require '[qimono.harvest :as harvest])
(harvest/calculate
  (harvest/bd "12345")
  (harvest/bd "0.250")
  (harvest/bd "3055.3875")
  (harvest/bd "0.01")
  (harvest/bd "0.000001"))
```
