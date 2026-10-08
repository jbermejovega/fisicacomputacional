"""Reproducibility and scientific assertions for the Ising teaching example."""
from __future__ import annotations

import importlib.util
from fractions import Fraction
from math import cosh, tanh
from pathlib import Path
import sys

import pytest

FILE = Path(__file__).resolve().parents[1] / "examples" / "ising_exact.py"
spec = importlib.util.spec_from_file_location("physics_art_ising", FILE)
assert spec is not None and spec.loader is not None
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)


def test_exact_energy_and_spin_convention():
    assert m.energy((1, 1, 1, 1), m.ring_edges(4), Fraction(1), Fraction(0)) == -4
    assert m.energy((1, -1, 1, -1), m.ring_edges(4), Fraction(1), Fraction(0)) == 4


def test_four_spin_ring_ferromagnet_ground_and_degeneracy():
    r = m.exact_spectrum()
    assert r["configuration_count"] == 16
    assert r["ground_energy"] == "-4"
    assert r["ground_states"] == ["0000", "1111"]
    assert r["quantum_bridge"]["qpu_executed"] is False


def test_four_spin_ring_antiferromagnet():
    r = m.exact_spectrum(J=Fraction(-1), beta=Fraction(0))
    assert r["ground_states"] == ["0101", "1010"]
    assert r["ground_energy"] == "-4"


def test_beta_zero_partition_and_symmetry():
    r = m.exact_spectrum(beta=Fraction(0))
    assert r["partition_function"] == pytest.approx(16)
    assert r["mean_magnetization"] == pytest.approx(0.0)


def test_exact_replay():
    assert m.exact_spectrum(J=Fraction(1,2)) == m.exact_spectrum(J=Fraction(1,2))


def test_physically_consistent_field_symmetry_breaking():
    r = m.exact_spectrum(h=Fraction(1,4), beta=Fraction(1))
    assert r["ground_energy"] == "-5"
    assert r["ground_states"] == ["0000"]
    assert r["mean_magnetization"] > 0


def test_invalid_grid_rejected():
    with pytest.raises(ValueError):
        m.ring_edges(2)
    with pytest.raises(ValueError):
        m.exact_spectrum(n=11)
    with pytest.raises(ValueError):
        m.exact_spectrum(beta=Fraction(-1))
