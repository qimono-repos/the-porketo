"""Validate the QFT circuit against the classical DFT and check basic invariants."""

from __future__ import annotations

import numpy as np
import pytest
from qiskit import QuantumCircuit
from qiskit.circuit.library import QFTGate
from qiskit.quantum_info import Statevector

from qft import quantum


@pytest.mark.parametrize("n", [4, 8, 16, 64, 512])
def test_qft_coefficients_match_numpy_fft(n):
    rng = np.random.default_rng(42 + n)
    x = rng.standard_normal(n)
    got = quantum.qft_coefficients(x)
    want = np.fft.fft(x)
    assert np.allclose(got, want, atol=1e-9)


def test_qft_statevector_is_normalised():
    rng = np.random.default_rng(0)
    y = quantum.qft_statevector(rng.standard_normal(64))
    assert np.isclose(np.linalg.norm(y), 1.0)


def test_qft_then_inverse_recovers_signal():
    rng = np.random.default_rng(1)
    x = rng.standard_normal(16)
    x /= np.linalg.norm(x)
    qc = QuantumCircuit(4)
    qc.initialize(x, range(4))
    qc.append(QFTGate(4), range(4))
    qc.append(QFTGate(4).inverse(), range(4))
    z = np.asarray(Statevector(qc).data)
    assert np.allclose(z, x, atol=1e-9)


def test_probabilities_sum_to_one():
    rng = np.random.default_rng(2)
    p = quantum.qft_probabilities(rng.standard_normal(32))
    assert np.isclose(p.sum(), 1.0)


def test_zero_signal_is_handled():
    assert np.allclose(quantum.qft_coefficients(np.zeros(8)), 0.0)


def test_sample_qft_argmax_matches_exact():
    n = 16
    k = 3
    x = np.cos(2 * np.pi * k * np.arange(n) / n)
    exact = quantum.qft_probabilities(x)
    counts = quantum.sample_qft(x, shots=4000, seed=7)
    assert sum(counts.values()) == 4000
    sampled_bin = int(max(counts, key=counts.get), 2)
    assert sampled_bin in {k, n - k}
    assert np.argmax(exact) in {k, n - k}


def test_n_qubits_and_power_of_two():
    assert quantum.is_power_of_two(512)
    assert not quantum.is_power_of_two(500)
    assert quantum.n_qubits(512) == 9
    with pytest.raises(ValueError):
        quantum.n_qubits(500)
    with pytest.raises(ValueError):
        quantum.qft_coefficients(np.zeros(7))
