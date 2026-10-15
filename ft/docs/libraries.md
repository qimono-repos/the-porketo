# FT — Libraries, in detail

The project deliberately uses **four** libraries. Each is explained below:
what it is, why we use it, the exact API we call, and the gotchas.

Dependencies are declared in `deps.edn`:

```clojure
{:paths ["src"]
 :deps {org.clojure/clojure        {:mvn/version "1.12.0"}
        org.apache.commons/commons-math3 {:mvn/version "3.6.1"}
        org.clojure/data.csv       {:mvn/version "1.1.0"}}
 :aliases {...}}
```

---

## 1. tools.deps (`clojure` CLI) — build & dependency management

**What:** the official Clojure CLI. It reads `deps.edn`, resolves Maven/Git
dependencies, builds a classpath, and runs code. It replaces Leiningen for this
project.

**Key concepts**

- The classpath is derived *on demand* from `deps.edn` (no `project.clj`).
- Resolved deps are cached in `~/.m2/repository` (Maven jars) and `~/.gitlibs`
  (git deps). The computed classpath is cached in `.cpcache/`.
- **Aliases** add extra paths/deps or change the entry point.

**Commands we use**

| Command | Meaning |
|---|---|
| `clojure -P` | Download/resolve all deps, then stop (prime the cache). |
| `clojure -M:run -- ARGS` | Run with the `:run` alias; `-M` uses `:main-opts`. |
| `clojure -M:test` | Run with the `:test` alias (`:extra-paths ["test"]`). |
| `clojure -Spath` | Print the resolved classpath (debugging). |
| `clojure -Stree` | Print the dependency tree (debugging conflicts). |

**Our aliases**

```clojure
:aliases
{:run  {:main-opts ["-m" "ft.main"]}
 :test {:extra-paths ["test"]
        :main-opts ["-m" "ft.runner"]}}
```

**Gotcha:** `clojure -M:run -- --horizon 24` needs the literal `--` so the
program receives `--horizon` rather than the launcher.

---

## 2. `org.clojure/clojure` 1.12.0 — the language/runtime

Clojure is a JVM Lisp. Notable features used here:

- **Immutable data structures** — vectors and maps; the model is a plain map.
- **Destructuring** — `(let [{:keys [a b n spectrum bins]} model] ...)`.
- **Java interop** — `(some-package.Class. args)`, `(method .obj args)`; used
  heavily to call Commons Math.
- **`reduce`, `map`, `Math/*`** — numerics are JVM doubles, so `Math/sin`,
  `Math/hypot`, `Math/PI` behave exactly as Java.

Version note: 1.12.x adds qualified methods and better error messages; nothing
here depends on bleeding-edge features, so 1.11 would also work.

---

## 3. Apache Commons Math 3.6.1 — the FFT

`org.apache.commons/commons-math3` is a mature numerical library. We use exactly
one class: `FastFourierTransformer`.

### The API we call

```clojure
(:import [org.apache.commons.math3.transform FastFourierTransformer
          DftNormalization TransformType]
         [org.apache.commons.math3.complex Complex])

(def transformer
  (FastFourierTransformer. DftNormalization/STANDARD))

(.transform transformer (double-array xs) TransformType/FORWARD) ; -> Complex[]
```

- **`DftNormalization/STANDARD`** — the forward transform is exactly
  `X[k] = Σₙ x[n]·e^(−2πikn/N)`. We rely on this so that **bin `k` means `k`
  cycles across the window**, which makes `period = N/k` meaningful.
  (The alternative, `UNITARY`, scales by `1/√N`; we do not use it.)
- **`TransformType/FORWARD`** / **`INVERSE`**. We only use `FORWARD`; we
  reconstruct manually so we can keep a subset of bins.
- **Length must be a power of two.** Commons Math throws for other lengths.
  Our `ft.fft/power-of-two?` guards this with a friendlier error.
- **Result** is `Complex[]`; we read `.getReal` / `.getImaginary`, and compute
  magnitude with `Math/hypot`.

### Why the frequency convention matters

With `STANDARD` normalization and `k` meaning cycles-per-window:

- `k = 0` → DC (the mean).
- `k = N/2` → Nyquist (the fastest representable oscillation, period 2).
- `k` and `N−k` are conjugate-symmetric for real input; we only read `k` in
  `1..N/2−1` and reconstruct their real effect with the `2/N` factor.

### Reconstruction formula we implement

For a real signal, the inverse transform is:

```
x[t] = (1/N)·X[0]
     + (2/N)·Σ_{k=1}^{N/2−1} Re( X[k]·e^{i2πkt/N} )
     + (1/N)·X[N/2]·(−1)^t              // Nyquist term
```

Leaving out the Nyquist term is a classic subtle bug — full-bin reconstruction
is *not* exact without it (we hit this in Iteration 03).

### Alternatives

- **JTransforms** — faster, multi-threaded, but a heavier dependency and a
  different API.
- **Neanderthal** — high-performance native BLAS/FFT; overkill here.
- **clojure.core** — none; the language has no built-in FFT.

### Performance

A 512-point radix-2 FFT is microseconds. 1024 points × 4 symbols × (1 holdout +
1 refit) is trivially fast (well under a second).

---

## 4. `org.clojure/data.csv` 1.1.0 — CSV I/O

**What:** a minimal, fast CSV reader/writer.

**API we call** (in `ft.data`):

```clojure
(require '[clojure.data.csv :as csv]
         '[clojure.java.io :as io])

(with-open [r (io/reader path)]
  (let [[header & rows] (csv/read-csv r)] ...))
```

- `read-csv` returns a **lazy sequence of vectors of strings**, including the
  header row. We `mapv` over it to realise it inside `with-open`.
- We build a map per row by zipping the header keywords with the values, so
  column order is never hard-coded.
- Numbers are converted explicitly (`Double/parseDouble`, `Long/parseLong`) —
  `data.csv` gives strings, never parsed values.
- `write-csv` exists (not used here) if you add CSV export (backlog item F3).

**Gotchas**

- **Laziness + `with-open`:** realise the seq *inside* the `with-open`, otherwise
  the reader is closed before the lazy values are read.
- **BOMs/whitespace:** the synthetic file is clean UTF-8 without a BOM; if you
  swap in a real export, trim fields and strip a leading BOM.

---

## 5. `clojure.test` — testing (built into Clojure)

No extra dependency. `clojure.test` provides `deftest`, `is`, `testing`, and
`run-tests`. Because we did not want a third-party test runner, `ft.runner`
just calls `clojure.test/run-tests` on our namespaces and exits non-zero on
failure — so `clojure -M:test` works with zero extra deps.

```clojure
(deftest mae-basic
  (is (< (Math/abs (- (ft.metrics/mae [1 2 3] [2 4 6]) 2.0)) 1e-9)))
```

---

## Version matrix

| Library | Version | Role | License |
|---|---|---|---|
| Clojure | 1.12.0 | Language | EPL-1.0 |
| tools.deps (CLI) | 1.12.6.x | Build/deps | EPL-1.0 |
| commons-math3 | 3.6.1 | FFT | Apache-2.0 |
| data.csv | 1.1.0 | CSV I/O | EPL-1.0 |
