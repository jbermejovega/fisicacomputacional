"""Original SymPy codebook for the computational physics wrap-up.

Models: exact finite Ising ring, single-qubit Hadamard, Boolean Möbius
inversion and a reproducible vector Hasse diagram. Scientific validation
requires comparison with the physical assumptions stated in the chapter.

SPDX-License-Identifier: MIT
Copyright (c) 2026 Jara Juana Bermejo Vega
"""
from __future__ import annotations

import argparse
from itertools import combinations, product
import json
from pathlib import Path
from xml.sax.saxutils import escape

from sympy import I, Integer, Matrix, S, exp, log, simplify, sqrt, symbols


def ising_energy(spins: tuple[int, ...], coupling=1, field=0):
    """Periodic 1D nearest-neighbour Ising energy; k_B is not used here.

    E = -J sum_i s_i s_(i+1) - h sum_i s_i, N >= 2.
    """
    if len(spins) < 2 or any(spin not in (-1, 1) for spin in spins):
        raise ValueError("ISING_SPINS_INVALID")
    return simplify(
        -coupling * sum(spins[i] * spins[(i + 1) % len(spins)]
                        for i in range(len(spins)))
        - field * sum(spins)
    )


def exact_ising_ring(n: int, beta, coupling=1, field=0) -> dict:
    """Enumerate a small finite ring, returning exact SymPy quantities."""
    if type(n) is not int or not 2 <= n <= 12:
        raise ValueError("ISING_EXACT_N_OUT_OF_BOUNDS")
    states = tuple(product((-1, 1), repeat=n))
    weights = tuple(exp(-beta * ising_energy(s, coupling, field)) for s in states)
    partition = simplify(sum(weights))
    mean_energy = simplify(
        sum(ising_energy(s, coupling, field) * w for s, w in zip(states, weights))
        / partition
    )
    mean_magnetization = simplify(
        sum(sum(s) * w for s, w in zip(states, weights)) / partition
    )
    mean_abs_magnetization = simplify(
        sum(abs(sum(s)) * w for s, w in zip(states, weights)) / partition
    )
    return {
        "n": n,
        "states": len(states),
        "Z": partition,
        "mean_energy": mean_energy,
        "mean_total_magnetization": mean_magnetization,
        "mean_abs_total_magnetization": mean_abs_magnetization,
    }


def hadamard_lab() -> dict:
    """A single qubit: H†H=1, P(0)=P(1)=1/2."""
    h = Matrix([[1, 1], [1, -1]]) / sqrt(2)
    zero = Matrix([1, 0])
    psi = h * zero
    projector_norm = simplify((psi.conjugate().T * psi)[0])
    return {
        "matrix": h,
        "state": psi,
        "is_unitary": simplify(h.conjugate().T * h - Matrix.eye(2)) == Matrix.zeros(2),
        "norm": projector_norm,
        "probabilities": tuple(simplify(psi[i] * psi[i].conjugate()) for i in range(2)),
    }


def _powerset(items: tuple[str, ...]) -> tuple[frozenset[str], ...]:
    return tuple(
        frozenset(part)
        for k in range(len(items) + 1)
        for part in combinations(items, k)
    )


def boolean_mobius(lower: frozenset[str], upper: frozenset[str]) -> int:
    """Möbius function of the finite Boolean lattice on a given interval."""
    if not lower <= upper:
        raise ValueError("BOOLEAN_INTERVAL_NOT_ORDERED")
    return (-1) ** len(upper - lower)


def mobius_inversion_b2() -> dict:
    """Check a finite inclusion-exclusion identity via exact enumeration."""
    subsets = _powerset(("a", "b"))
    original = {s: Integer(1 + len(s)) for s in subsets}
    cumulative = {
        s: sum(original[t] for t in subsets if t <= s)
        for s in subsets
    }
    recovered = {
        s: simplify(
            sum(boolean_mobius(t, s) * cumulative[t]
                for t in subsets if t <= s)
        )
        for s in subsets
    }
    return {
        "inversion_valid": recovered == original,
        "mu_empty_full": boolean_mobius(frozenset(), frozenset(("a", "b"))),
        "subset_count": len(subsets),
        "original": {",".join(sorted(s)) or "empty": str(v) for s, v in original.items()},
        "recovered": {",".join(sorted(s)) or "empty": str(v) for s, v in recovered.items()},
    }


def hasse_b2_svg() -> str:
    """Create an original vector illustration using a typed Boolean poset.

    No copied external artwork, screenshots or logos are embedded.
    SVG graphics copyright (c) 2026 Jara Juana Bermejo Vega.
    All rights reserved as a prospective original course-art notice;
    prior third-party rights are not changed.
    """
    locations = {
        frozenset(): (300, 260),
        frozenset(("a",)): (160, 150),
        frozenset(("b",)): (440, 150),
        frozenset(("a", "b")): (300, 40),
    }
    labels = {
        frozenset(): "∅",
        frozenset(("a",)): "{a}",
        frozenset(("b",)): "{b}",
        frozenset(("a", "b")): "{a,b}",
    }
    ordered = tuple(locations)
    lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="600" height="315" viewBox="0 0 600 315">',
        '<title>Retículo booleano B2 e inversión de Möbius</title>',
        '<desc>Dibujo original reproducible de cuatro elementos y sus cubrimientos.</desc>',
        '<rect width="600" height="315" fill="#121b29"/>',
    ]
    for lower in ordered:
        for upper in ordered:
            if lower < upper and len(upper - lower) == 1:
                x1, y1 = locations[lower]
                x2, y2 = locations[upper]
                lines.append(
                    f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#63d5dc" '
                    'stroke-width="3" fill="none"/>'
                )
    for element, (x, y) in locations.items():
        mu = boolean_mobius(frozenset(), element)
        lines.append(f'<circle cx="{x}" cy="{y}" r="30" fill="#304e77" stroke="#f5c677" stroke-width="2"/>')
        lines.append(f'<text x="{x}" y="{y+6}" font-size="18" text-anchor="middle" fill="#ffffff">{escape(labels[element])}</text>')
        lines.append(f'<text x="{x+38}" y="{y+6}" font-size="13" fill="#f5c677">μ={mu:+d}</text>')
    lines.append('<text x="12" y="303" font-size="12" fill="#e5e8f0">SIGIL · Física Computacional · B2 · © 2026 JJBV</text>')
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Repaso SymPy de Física Computacional")
    parser.add_argument("--svg", type=Path, help="guardar diagrama vectorial original B2")
    args = parser.parse_args()
    beta = log(2)
    ising = exact_ising_ring(4, beta)
    qubit = hadamard_lab()
    inversion = mobius_inversion_b2()
    payload = {
        "schema_id": "FISICACOMPUTACIONAL_WRAPUP_CODEBOOK_V1",
        "scientific_scope": "small_exact_examples_only",
        "ising": {k: str(v) for k, v in ising.items()},
        "hadamard": {
            "is_unitary": qubit["is_unitary"],
            "probabilities": [str(v) for v in qubit["probabilities"]],
            "norm": str(qubit["norm"]),
        },
        "mobius": inversion,
        "units": "dimensionless; k_B=1; H uses exact symbolic amplitudes",
        "replay": "deterministic_no_random_sampling",
    }
    if args.svg is not None:
        args.svg.parent.mkdir(parents=True, exist_ok=True)
        args.svg.write_text(hasse_b2_svg(), encoding="utf-8")
        payload["svg_output"] = str(args.svg)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
