# SPDX-License-Identifier: Apache-2.0
"""Original KRONE codebook: finite exact checks for computational physics.

A small, local SymPy-backed library. It does not execute network requests,
LlamaIndex, Ollama, SIGILBOOK/UAP gates, or open any confidential sources.
Mathematical examples are explicitly bounded; notebook results need independent
physical interpretation.
"""
from __future__ import annotations

from itertools import combinations
from typing import Iterable

import sympy as sp


def mobius_boolean(lower: Iterable[str], upper: Iterable[str]) -> int:
    """Möbius function μ(S,T) of the subset lattice, provided S ⊆ T."""
    lo = frozenset(lower)
    hi = frozenset(upper)
    if not lo.issubset(hi):
        raise ValueError("NOT_AN_INTERVAL_IN_BOOLEAN_LATTICE")
    return (-1) ** len(hi - lo)


def laplacian_from_edges(n: int, edges: Iterable[tuple[int, int]]) -> sp.Matrix:
    """Unweighted simple undirected graph Laplacian with n labeled vertices."""
    if not isinstance(n, int) or not 1 <= n <= 20:
        raise ValueError("GRAPH_SIZE_OUT_OF_BOUNDS")
    pairs = _checked_edges(n, edges)
    result = sp.zeros(n)
    for u, v in pairs:
        result[u, u] += 1
        result[v, v] += 1
        result[u, v] -= 1
        result[v, u] -= 1
    return result


def _checked_edges(n: int, edges: Iterable[tuple[int, int]]) -> tuple[tuple[int, int], ...]:
    seen: set[tuple[int, int]] = set()
    out: list[tuple[int, int]] = []
    for pair in edges:
        if not isinstance(pair, tuple) or len(pair) != 2:
            raise ValueError("INVALID_EDGE")
        u, v = pair
        if type(u) is not int or type(v) is not int:
            raise ValueError("INVALID_VERTEX_ID")
        if not (0 <= u < n and 0 <= v < n) or u == v:
            raise ValueError("OUT_OF_RANGE_OR_LOOP")
        edge = (min(u, v), max(u, v))
        if edge in seen:
            raise ValueError("DUPLICATE_EDGE")
        seen.add(edge)
        out.append(edge)
    return tuple(sorted(out))


def spanning_tree_count(n: int, edges: Iterable[tuple[int, int]]) -> sp.Integer:
    """Matrix-tree cofactor (exact number of spanning trees)."""
    matrix = laplacian_from_edges(n, edges)
    if n == 1:
        return sp.Integer(1)
    return sp.Integer(matrix[0:n - 1, 0:n - 1].det())


def _component_count(n: int, edges: Iterable[tuple[int, int]]) -> int:
    parent = list(range(n))

    def root(i: int) -> int:
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for u, v in edges:
        a, b = root(u), root(v)
        if a != b:
            parent[b] = a
    return len({root(v) for v in range(n)})


def fortuin_kasteleyn(n: int, edges: Iterable[tuple[int, int]],
                       q: sp.Symbol | sp.Expr, v: sp.Symbol | sp.Expr) -> sp.Expr:
    """Return Z_G(q,v)=sum_{A subset E} q^k(A) v^|A| for <=16 edges."""
    if not isinstance(n, int) or not 1 <= n <= 12:
        raise ValueError("GRAPH_SIZE_OUT_OF_BOUNDS")
    pairs = _checked_edges(n, edges)
    if len(pairs) > 16:
        raise ValueError("EXPONENTIAL_EDGE_BUDGET_EXCEEDED")
    q = sp.sympify(q)
    v = sp.sympify(v)
    total: sp.Expr = sp.Integer(0)
    for k in range(len(pairs) + 1):
        for selected in combinations(pairs, k):
            total += q ** _component_count(n, selected) * v ** k
    return sp.expand(total)


def chromatic_triangle() -> sp.Expr:
    """Exactly count proper colorings of the triangle K3."""
    q = sp.symbols("q", integer=True, positive=True)
    return sp.factor(q * (q - 1) * (q - 2))


def two_spin_ising() -> tuple[sp.Expr, sp.Expr]:
    """Partition function and correlation for two spins H=-J s1 s2, h=0."""
    beta = sp.symbols("beta", real=True)
    J = sp.symbols("J", real=True)
    z = sp.Integer(4) * sp.cosh(beta * J)
    corr = sp.tanh(beta * J)
    return z, corr


def hadamard_checks() -> dict[str, sp.Expr | bool]:
    """Verify H^dagger H=I and Bell state's reduced density = I/2."""
    sqrt2 = sp.sqrt(2)
    h = sp.Matrix([[1, 1], [1, -1]]) / sqrt2
    unitary = sp.simplify(h.H * h) == sp.eye(2)
    zero = sp.Matrix([1, 0])
    plus = h * zero
    bell = sp.kronecker_product(plus, zero)
    cnot = sp.Matrix([[1,0,0,0], [0,1,0,0], [0,0,0,1], [0,0,1,0]])
    bell = cnot * bell
    rho = bell * bell.H
    reduced = sp.Matrix([
        [sum(rho[2*i+b, 2*j+b] for b in range(2)) for j in range(2)]
        for i in range(2)
    ])
    reduced = sp.simplify(reduced)
    return {
        "h_is_unitary": unitary,
        "bell_reduced": reduced,
        "bell_reduced_is_mixed": reduced == sp.eye(2) / 2,
        "bell_reduced_purity": sp.simplify(sp.trace(reduced * reduced)),
    }


def self_check() -> dict[str, str | bool | int]:
    """Bounded didactic checks; a local receipt, NOT proof-host certification."""
    q, v = sp.symbols("q v")
    triangle = ((0, 1), (1, 2), (2, 0))
    fk = fortuin_kasteleyn(3, triangle, q, v)
    expected = q**3 + 3*q**2*v + 3*q*v**2 + q*v**3
    had = hadamard_checks()
    ising_z, corr = two_spin_ising()
    beta, J = sp.symbols("beta J", real=True)
    return {
        "mobius_B2": mobius_boolean([], ["a", "b"]),
        "triangle_trees": int(spanning_tree_count(3, triangle)),
        "fortuin_kasteleyn_triangle": sp.expand(fk - expected) == 0,
        "hadamard_unitary": bool(had["h_is_unitary"]),
        "bell_reduced_is_mixed": bool(had["bell_reduced_is_mixed"]),
        "bell_purity": str(had["bell_reduced_purity"]),
        "two_spin_partition": sp.simplify(ising_z - 4*sp.cosh(beta*J)) == 0,
        "two_spin_correlation": sp.simplify(corr - sp.tanh(beta*J)) == 0,
        "scientific_certification": False,
    }


if __name__ == "__main__":
    from json import dumps
    print(dumps(self_check(), ensure_ascii=False, sort_keys=True))
