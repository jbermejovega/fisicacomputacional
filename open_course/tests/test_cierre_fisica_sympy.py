"""Focused unit tests for original computational physics SymPy wrap-up."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "codebook"))

from cierre_fisica_sympy import (  # noqa: E402
    boolean_mobius,
    exact_ising_ring,
    hadamard_lab,
    hasse_b2_svg,
    ising_energy,
    mobius_inversion_b2,
)
from sympy import Integer, Rational  # noqa: E402


class SymPyCourseWrapupTests(unittest.TestCase):
    def test_ferromagnetic_and_alternating_energy(self):
        self.assertEqual(ising_energy((1, 1, 1, 1)), -4)
        self.assertEqual(ising_energy((1, -1, 1, -1)), 4)

    def test_unphysical_spin_rejected(self):
        with self.assertRaisesRegex(ValueError, "ISING_SPINS_INVALID"):
            ising_energy((1, 0, -1, 1))

    def test_bounded_exact_enumeration(self):
        with self.assertRaisesRegex(ValueError, "ISING_EXACT_N_OUT_OF_BOUNDS"):
            exact_ising_ring(13, Integer(1))

    def test_infinite_temperature_exact_identity(self):
        out = exact_ising_ring(4, beta=Integer(0))
        self.assertEqual(out["states"], 16)
        self.assertEqual(out["Z"], 16)
        self.assertEqual(out["mean_energy"], 0)
        self.assertEqual(out["mean_total_magnetization"], 0)

    def test_qubit_unitary_and_born_rule(self):
        h = hadamard_lab()
        self.assertTrue(h["is_unitary"])
        self.assertEqual(h["norm"], 1)
        self.assertEqual(h["probabilities"], (Rational(1, 2), Rational(1, 2)))

    def test_boolean_interval_requires_order(self):
        with self.assertRaisesRegex(ValueError, "BOOLEAN_INTERVAL_NOT_ORDERED"):
            boolean_mobius(frozenset(("a",)), frozenset())

    def test_mobius_inversion_is_exact(self):
        result = mobius_inversion_b2()
        self.assertTrue(result["inversion_valid"])
        self.assertEqual(result["mu_empty_full"], 1)
        self.assertEqual(result["subset_count"], 4)

    def test_svg_is_parseable_original_and_has_four_nodes(self):
        graphic = hasse_b2_svg()
        root = ElementTree.fromstring(graphic)
        ns = "{http://www.w3.org/2000/svg}"
        self.assertEqual(len(root.findall(ns + "circle")), 4)
        self.assertEqual(len(root.findall(ns + "path")), 4)
        self.assertIn("SIGIL", graphic)
        self.assertIn("© 2026 JJBV", graphic)


if __name__ == "__main__":
    unittest.main()
