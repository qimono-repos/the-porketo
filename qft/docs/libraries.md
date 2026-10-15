# QFT — Libraries, in detail

The project deliberately uses a **small** set of libraries, all declared in
`pyproject.toml`:

```toml
[project]
dependencies = [
    "qiskit>=1.0",
    "qiskit-aer>=0.14",
    "numpy>=1.24",
]

[dependency-groups]
dev = ["pytest>=8.0"]
```

`uv.lock` pins the resolved versions (currently `qiskit 2.5.2`,
`qiskit-aer 0.17.2`, `numpy 2.5.4`, `scipy 1.18.1`, `pytest 9.1.1`).

---

## 1. `uv` — Python, packaging & dependency management

**What:** a single-binary project manager for Python (from Astral). It installs
and selects Python interpreters, creates the virtual environment, resolves and
installs dependencies, and runs commands inside that environment.

**Why we use it:** it makes the whole toolchain one command (`uv sync`) with no
system Python prerequisite, and it records exact versions in `uv.lock`.

**Commands we use**

| Command | Meaning |
|---|---|
| `uv sync` | Create/refresh `.venv` from `pyproject.toml` + `uv.lock`. |
| `uv run pytest` | Run pytest inside `.venv` (syncing first if needed). |
| `uv run qft ...` | Run the `qft` console script (the `[project.scripts]` entry point). |
| `uv python install 3.12` | Explicitly fetch a managed CPython 3.12. |
| `uv sync --offline` | Resolve/install with no network (cache only). |
| `uv lock` | Re-resolve and update `uv.lock` (only when deps change). |

**Layout choices**

- We use a **`src/` layout** (`src/qft/`) so the package cannot be imported by
  accident without installation — tests import the *installed* package.
- The project is installed in **editable** mode by `uv sync`, so code changes are
  picked up without re-installing.
- `requires-python = ">=3.10"` and `.python-version = 3.12` pin the interpreter.

**Gotcha:** `uv run qft` only works because `[project.scripts]` maps the name to
`qft.main:main`. Without that entry point, use `uv run python -m qft.main`. (The
module also has an `if __name__ == "__main__"` guard, so `python -m qft.main`
works too.)

---

## 2. `numpy` — arrays and the reference DFT

**What:** the fundamental array/numerics library.

**Where we use it**

- `qft.data` / `qft.predict` treat series as `numpy.ndarray` of `float64`.
- `qft.metrics` computes MAE/RMSE/MAPE with vectorised expressions:
  ```python
  np.mean(np.abs(a - p))            # MAE
  np.sqrt(np.mean((a - p) ** 2))    # RMSE
  ```
- `qft.predict.top_bins` sorts by `np.abs(spectrum)`.
- `qft.quantum.dft_reference` returns `np.fft.fft(signal)` — used **only** in
  tests as the classical ground truth the QFT must match.

**Gotcha:** NumPy's default complex type is `complex128` (double precision),
which is what we want; avoid `np.float32` here or the 1e-9 test tolerances fail.

---

## 3. `qiskit` — circuits, the QFT gate, and statevector simulation

Qiskit is the quantum SDK. We use a deliberate subset.

### The API we call

```python
from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import QFTGate
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(n)
qc.initialize(signal / np.linalg.norm(signal), range(n))  # amplitude encoding
qc.append(QFTGate(n), range(n))                           # the transform
y = np.asarray(Statevector(qc).data)                      # exact statevector
```

- **`QuantumCircuit.initialize`** — prepares an arbitrary (normalised) state
  vector. This is the amplitude encoding: `N = 2^n` amplitudes → `n` qubits.
  *Verified:* it preserves the state exactly (no residual global phase), so our
  coefficient recovery is exact.
- **`QFTGate(n)`** — the QFT as a reusable gate. **Use this, not the deprecated
  `qiskit.circuit.library.QFT` class** (deprecated in Qiskit 2.1, scheduled for
  removal in 3.0).
- **`Statevector(circuit)`** — exact, noiseless statevector simulation. Cheap for
  our sizes (≤ 10 qubits) and avoids shot noise, which is what we want for a
  deterministic forecast.
- **`transpile(circuit, backend)`** — required before Aer can run a circuit that
  contains the composite `qft` instruction (Aer does not natively understand it;
  it raises `unknown instruction: qft` otherwise).

### The convention that matters

Qiskit's QFT uses a **positive** exponent and `1/√N` scaling:

```
y_j = (1/√N) · Σ_k e^{+2πijk/N} · v_k
```

The standard **forward** DFT (what `np.fft.fft` and Commons Math's `STANDARD`
normalization return) is the *negative*-exponent, unnormalised sum, so for a real
signal:

```
X_j = Σ_k e^{-2πijk/N} · v_k = √N · conj(y_j)
```

We therefore set `spectrum = √N · ‖x‖ · conj(y)`. Getting this sign/conjugation
relationship right is the single most important detail in the project; it is
locked down by `tests/test_quantum.py::test_qft_coefficients_match_numpy_fft`
(sizes 4…512) and by round-trip and forecast-agreement tests.

### Frequency-bin indexing

The statevector index `j` is exactly the frequency bin: `j = 0` is DC,
`j = N/2` is Nyquist, and `period = N/j` hours. Because we only ever feed **real**
windows, bins `j` and `N−j` are conjugates and we read the positive halves
(`1 … N/2−1`) plus DC and Nyquist.

---

## 4. `qiskit-aer` — shot-based simulation

**What:** a high-performance simulator package. We only use `AerSimulator` for
the optional `--shots` demonstration.

```python
from qiskit_aer import AerSimulator
sim = AerSimulator()
tqc = transpile(qc, sim)                 # decompose qft into basis gates
counts = sim.run(tqc, shots=4096, seed_simulator=1234).result().get_counts()
```

- Use `seed_simulator` for reproducibility.
- The counts key is a bitstring; `int(key, 2)` indexes the same bin `j` as the
  statevector (`tests/test_quantum.py::test_sample_qft_argmax_matches_exact`
  checks the measured arg-max matches the exact distribution's arg-max).
- **Gotcha:** you must `measure_all()` and `transpile` before `run`, and the
  composite `qft` instruction must be decomposed (Aer otherwise errors).
- The forecast never depends on shots; it always uses the exact statevector.

---

## 5. `pytest` — testing

**What:** the de-facto Python test framework. Dev-only dependency.

- Tests live in `tests/` (`testpaths = ["tests"]` in `pyproject.toml`).
- We use `@pytest.mark.parametrize` to run the DFT-equality check over several
  window sizes, and `pytest.raises` for the power-of-two guards.
- Run with `uv run pytest`; add `-q` (already in `addopts`), `-k NAME` to filter,
  or `-v` for detail.

---

## Transitive dependencies (pinned in `uv.lock`)

You will see more packages installed than the four above — for example `scipy`
(a Qiskit dependency), `rustworkx` (Qiskit's graph library), `symengine`,
`stevedore`, `dill`, `python-dateutil`. These are pulled in by Qiskit; you should
not need to import them directly.

## Version matrix

| Library | Version (locked) | Role | License |
|---|---|---|---|
| uv | 0.13.x | Python/env/dep management | MIT/Apache-2.0 |
| Python | 3.12 | Interpreter (uv-managed) | PSF |
| numpy | 2.5.4 | Arrays + reference DFT | BSD-3 |
| qiskit | 2.5.2 | Circuits, QFTGate, Statevector | Apache-2.0 |
| qiskit-aer | 0.17.2 | Shot-based simulation | Apache-2.0 |
| pytest | 9.1.1 | Tests (dev) | MIT |
