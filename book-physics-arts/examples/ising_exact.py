"""Finite Ising field exercise: exact classical enumeration and a QML bridge.

Teaching source: standard library only. No data download, QPU, auto-grading,
network requests, or dependency on an unmerged SIGIL API branch.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import product
from math import exp
import json


def energy(spins: tuple[int, ...], edges: tuple[tuple[int, int], ...],
           J: Fraction, h: Fraction) -> Fraction:
    if not spins or any(s not in (-1, 1) for s in spins):
        raise ValueError("spins must be ±1")
    n = len(spins)
    if any(a == b or not (0 <= a < n and 0 <= b < n) for a, b in edges):
        raise ValueError("invalid edge")
    if len(set(tuple(sorted(e)) for e in edges)) != len(edges):
        raise ValueError("duplicate edge")
    return -J * sum(spins[a] * spins[b] for a, b in edges) - h * sum(spins)


def ring_edges(n: int) -> tuple[tuple[int, int], ...]:
    if type(n) is not int or not 3 <= n <= 10:
        raise ValueError("ring requires 3..10 sites")
    return tuple((i, (i + 1) % n) for i in range(n))


def exact_spectrum(n: int = 4, J: Fraction = Fraction(1),
                   h: Fraction = Fraction(0),
                   beta: Fraction = Fraction(1, 2)) -> dict:
    """Return energies exactly; finite-T observables approximately."""
    if type(n) is not int or not 3 <= n <= 10:
        raise ValueError("site count out of bounds")
    J, h, beta = Fraction(J), Fraction(h), Fraction(beta)
    if beta < 0 or beta * (n * (abs(J) + abs(h))) > 400:
        raise ValueError("beta or energy scale outside safe bounds")
    edges = ring_edges(n)
    records = []
    for bits in product((0, 1), repeat=n):
        spins = tuple(1 - 2 * bit for bit in bits)
        E = energy(spins, edges, J, h)
        records.append({"bits": "".join(str(b) for b in bits),
                        "energy": str(E),
                        "magnetization": sum(spins)})
    weights = [exp(-float(beta * Fraction(r["energy"]))) for r in records]
    Z = sum(weights)
    minimum = min(Fraction(row["energy"]) for row in records)
    ground = [row["bits"] for row in records if Fraction(row["energy"]) == minimum]
    mean_energy = sum(w * float(Fraction(r["energy"]))
                      for w, r in zip(weights, records)) / Z
    mean_mag = sum(w * r["magnetization"]
                   for w, r in zip(weights, records)) / Z
    return {
        "method": "exact_enumeration_classical_ising",
        "site_count": n, "edges": [list(e) for e in edges],
        "J": str(J), "h": str(h), "beta": str(beta),
        "units": {"J": "energy_unit", "h": "energy_unit",
                  "beta": "inverse_energy_unit", "spin": "dimensionless"},
        "states": records, "configuration_count": 1 << n,
        "ground_energy": str(minimum), "ground_states": ground,
        "partition_function": Z, "mean_energy": mean_energy,
        "mean_magnetization": mean_mag,
        "quantum_bridge": {
            "operator": "H_Z=-J sum_(i,j) Z_i Z_j-h sum_i Z_i",
            "spin_to_basis": "+1 => 0; -1 => 1",
            "qpu_executed": False, "quantum_advantage_claimed": False,
            "z_basis_spectrum_equal_to_classical": True
        },
        "style_preparation": "optional artistic sonification; not performed",
        "replay": "deterministic with Python stdlib and fixed parameters"
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Finite Ising/QML field exercise")
    parser.add_argument("--sites", type=int, default=4)
    parser.add_argument("--J", default="1", help="exact rational energy (e.g. 1/2)")
    parser.add_argument("--h", default="0", help="exact rational energy")
    parser.add_argument("--beta", default="1/2", help="inverse energy")
    args = parser.parse_args()
    print(json.dumps(exact_spectrum(args.sites, Fraction(args.J),
                                   Fraction(args.h), Fraction(args.beta)),
                     indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
