"""The quantum core: amplitude-encode a real signal and apply the QFT.

The transform is genuine quantum-mechanical: a real window is prepared as a
normalised amplitude state of ``n = log2(N)`` qubits, evolved by the QFT unitary
(``QFTGate``), and the resulting state is read out.

Conventions (verified against ``numpy.fft`` in ``tests/``)
---------------------------------------------------------
Qiskit's ``QFTGate`` implements the *unnormalised-convention / positive-exponent*
transform::

    y_j = (1/sqrt(N)) * sum_k exp(+2*pi*i*j*k/N) * v_k

For a **real** signal ``v`` the standard forward DFT (the same object Apache
Commons Math and ``numpy.fft.fft`` return for the Clojure ``ft`` sub-project) is
the conjugate sum, so it is recovered as::

    X_j = sum_k exp(-2*pi*i*j*k/N) * v_k = sqrt(N) * conj(y_j)

Because the DFT is linear, encoding ``v = d / ||d||`` and multiplying back by
``||d||`` yields the DFT of the original window ``d``.

A ``QFT then inverse-QFT`` round-trip returns the encoded state exactly, which
``tests/test_quantum.py`` asserts as an end-to-end sanity check.
"""

from __future__ import annotations

import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import QFTGate
from qiskit.quantum_info import Statevector

__all__ = [
    "n_qubits",
    "is_power_of_two",
    "qft_statevector",
    "qft_coefficients",
    "qft_probabilities",
    "sample_qft",
    "dft_reference",
]


def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0


def n_qubits(window: int) -> int:
    """Number of qubits needed to amplitude-encode a window of length ``window``."""
    if not is_power_of_two(window):
        raise ValueError(f"window length must be a power of two, got {window}")
    return window.bit_length() - 1


def qft_statevector(signal) -> np.ndarray:
    """Amplitude-encode a real signal and return the post-QFT statevector.

    The signal is normalised to unit L2 norm before encoding (``initialize``);
    the returned amplitudes are those of the QFT applied to that state.
    """
    x = np.asarray(signal, dtype=float)
    n = x.size
    if not is_power_of_two(n):
        raise ValueError(f"signal length must be a power of two, got {n}")

    norm = float(np.linalg.norm(x))
    if norm == 0.0:
        return np.zeros(n, dtype=complex)

    qc = QuantumCircuit(n_qubits(n))
    qc.initialize(x / norm, range(n_qubits(n)))
    qc.append(QFTGate(n_qubits(n)), range(n_qubits(n)))
    return np.asarray(Statevector(qc).data, dtype=complex)


def qft_coefficients(signal) -> np.ndarray:
    """Standard forward-DFT coefficients of a real signal, computed via the QFT.

    Returns ``X_j = sqrt(N) * ||x|| * conj(y_j)`` where ``y`` is the post-QFT
    statevector of the normalised signal. Equal (to floating-point precision) to
    ``numpy.fft.fft(signal)``.
    """
    x = np.asarray(signal, dtype=float)
    n = x.size
    if not is_power_of_two(n):
        raise ValueError(f"signal length must be a power of two, got {n}")
    norm = float(np.linalg.norm(x))
    if norm == 0.0:
        return np.zeros(n, dtype=complex)
    y = qft_statevector(x)
    return np.sqrt(n) * norm * np.conj(y)


def qft_probabilities(signal) -> np.ndarray:
    """Exact measurement probabilities ``|y_j|^2`` of the post-QFT state."""
    y = qft_statevector(signal)
    return np.abs(y) ** 2


def sample_qft(signal, shots: int = 4096, seed: int | None = None) -> dict[str, int]:
    """Shot-sampled measurement counts of the post-QFT state on ``AerSimulator``.

    Returns a mapping of basis-state bitstrings to counts. The bitstring integer
    ``int(key, 2)`` indexes the same frequency bin ``j`` as ``qft_statevector``.
    """
    from qiskit_aer import AerSimulator

    x = np.asarray(signal, dtype=float)
    n = x.size
    norm = float(np.linalg.norm(x))
    qubits = n_qubits(n)

    qc = QuantumCircuit(qubits)
    if norm != 0.0:
        qc.initialize(x / norm, range(qubits))
        qc.append(QFTGate(qubits), range(qubits))
    qc.measure_all()

    sim = AerSimulator()
    tqc = transpile(qc, sim)
    result = sim.run(tqc, shots=shots, seed_simulator=seed).result()
    return dict(result.get_counts())


def dft_reference(signal) -> np.ndarray:
    """Classical reference DFT (used only to validate the quantum result)."""
    return np.fft.fft(np.asarray(signal, dtype=float))
