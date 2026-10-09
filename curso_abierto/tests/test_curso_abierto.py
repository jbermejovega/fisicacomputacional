# SPDX-License-Identifier: Apache-2.0
"""Finite codebook tests: formulas and source-bound course index."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

import sympy as sp

COURSE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(COURSE / "codebooks"))

from buscar_indice import adapter_plan, load_index, lookup  # noqa: E402
from modelos_exactos import (  # noqa: E402
    chromatic_triangle,
    fortuin_kasteleyn,
    hadamard_checks,
    laplacian_from_edges,
    mobius_boolean,
    spanning_tree_count,
    two_spin_ising,
)


class CourseOpenTests(unittest.TestCase):
    def test_mobius_boolean_interval(self):
        self.assertEqual(mobius_boolean([], ["a", "b"]), 1)
        self.assertEqual(mobius_boolean(["a"], ["a", "b"]), -1)
        with self.assertRaises(ValueError):
            mobius_boolean(["c"], ["a"])

    def test_matrix_tree_triangle(self):
        triangle = ((0, 1), (1, 2), (0, 2))
        expected = sp.Matrix([[2,-1,-1], [-1,2,-1], [-1,-1,2]])
        self.assertEqual(laplacian_from_edges(3, triangle), expected)
        self.assertEqual(spanning_tree_count(3, triangle), 3)

    def test_fk_triangle_exact(self):
        q, v = sp.symbols("q v")
        value = fortuin_kasteleyn(3, [(0,1),(1,2),(0,2)], q, v)
        expected = q**3 + 3*q**2*v + 3*q*v**2 + q*v**3
        self.assertEqual(sp.expand(value-expected), 0)
        q_chromatic = sp.symbols("q", integer=True, positive=True)
        self.assertEqual(chromatic_triangle(), q_chromatic*(q_chromatic-1)*(q_chromatic-2))

    def test_isings_small_partition(self):
        z, corr = two_spin_ising()
        beta, J = sp.symbols("beta J", real=True)
        self.assertEqual(sp.simplify(z-4*sp.cosh(beta*J)), 0)
        self.assertEqual(sp.simplify(corr-sp.tanh(beta*J)), 0)

    def test_hadamard_bell(self):
        checks = hadamard_checks()
        self.assertTrue(checks["h_is_unitary"])
        self.assertTrue(checks["bell_reduced_is_mixed"])
        self.assertEqual(checks["bell_reduced_purity"], sp.Rational(1,2))

    def test_source_bound_hyperjarra_search(self):
        data = load_index()
        self.assertEqual(data["retrieval"]["canonical_index"], "HyperJarraIndexTyped")
        self.assertGreaterEqual(len(data["records"]), 15)
        self.assertTrue(lookup("Ising", index=data))
        self.assertTrue(lookup("bibliotecas", index=data))
        self.assertEqual(lookup("no-such-curriculum-token-zzzz", index=data), [])

    def test_ollama_is_plan_not_model(self):
        plan = adapter_plan("OLLAMA", index=load_index())
        self.assertFalse(plan["provider_io"])
        self.assertFalse(plan["model_loaded"])
        self.assertFalse(plan["provider_imported"])
        self.assertFalse(plan["framework_is_canonical"])

    def test_private_material_must_not_enter_public_index(self):
        data = load_index()
        data["records"][0]["visibility"] = "PRIVATE"
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "PRIVATE_RECORD_IN_PUBLIC_COURSE"):
                load_index(path)

    def test_course_chapters_exist(self):
        for name in (
            "CAPITULO_00_WRAP_UP.md",
            "CAPITULO_01_COMPUTACION_CUANTICA.md",
            "CAPITULO_02_COMBINATORIA_ALGEBRAICA.md",
            "CAPITULO_03_BIBLIOTECAS_HUMANIDADES_DIGITALES.md",
            "CAPITULO_04_SISTEMAS_COMPLEJOS_MATERIA_CONDENSADA.md",
        ):
            self.assertTrue((COURSE / name).is_file(), name)
        self.assertTrue((COURSE / "LICENCIAS.md").is_file())


if __name__ == "__main__":
    unittest.main()
