"""
SIGIL4BLOOD_TOY_SIMULATION

Toy mechanistic contextual Ising / Metropolis–Kawasaki simulation.

This is NOT a medical model.
It tests the qualitative hypothesis:

  reduced anticoagulant damping
+ boundary/stasis fields
+ trigger perturbations
→ higher probability of clot-domain nucleation.

Author: JJBV / Jara Juana Bermejo Vega
"""

from __future__ import annotations

import numpy as np

rng = np.random.default_rng(42)


def make_boundary_field(n, strength=0.0):
    y, x = np.mgrid[0:n, 0:n]
    edge_dist = np.minimum.reduce([x, y, n - 1 - x, n - 1 - y]).astype(float)
    edge_field = np.exp(-edge_dist / 3.0)
    valve = np.exp(-((x - n * 0.52) ** 2) / (2 * (n * 0.04) ** 2))
    return strength * (0.65 * edge_field + 0.35 * valve)


def make_stasis_field(n, strength=0.0):
    y, x = np.mgrid[0:n, 0:n]
    basin = np.exp(-(((x - n * 0.55) ** 2 + (y - n * 0.65) ** 2) / (2 * (n * 0.18) ** 2)))
    return strength * basin


def initial_state(n, p_active=0.05):
    return np.where(rng.random((n, n)) < p_active, 1, -1).astype(np.int8)


def neighbors_sum(s):
    return (
        np.roll(s, 1, axis=0)
        + np.roll(s, -1, axis=0)
        + np.roll(s, 1, axis=1)
        + np.roll(s, -1, axis=1)
    )


def energy(s, J, h):
    pair = s * (np.roll(s, 1, axis=0) + np.roll(s, 1, axis=1))
    return -J * pair.sum() - (h * s).sum()


def metropolis_step(s, J, h, beta, kawasaki_prob=0.65):
    n = s.shape[0]

    if rng.random() < kawasaki_prob:
        i, j = rng.integers(0, n, size=2)
        if rng.random() < 0.5:
            ni, nj = (i + rng.choice([-1, 1])) % n, j
        else:
            ni, nj = i, (j + rng.choice([-1, 1])) % n

        if s[i, j] == s[ni, nj]:
            return

        e0 = energy(s, J, h)
        s[i, j], s[ni, nj] = s[ni, nj], s[i, j]
        e1 = energy(s, J, h)
        dE = e1 - e0

        if not (dE <= 0 or rng.random() < np.exp(-beta * dE)):
            s[i, j], s[ni, nj] = s[ni, nj], s[i, j]

    else:
        i, j = rng.integers(0, n, size=2)
        dE = 2 * s[i, j] * (J * neighbors_sum(s)[i, j] + h[i, j])

        if dE <= 0 or rng.random() < np.exp(-beta * dE):
            s[i, j] *= -1


def run_demo():
    n = 48
    J = 0.45
    beta = 0.80

    anticoag_damping = 0.45
    boundary_strength = 0.13
    stasis_strength = 0.18
    trigger_strength = 0.22

    boundary = make_boundary_field(n, boundary_strength)
    stasis = make_stasis_field(n, stasis_strength)
    trigger = make_stasis_field(n, trigger_strength)

    h = boundary + stasis + trigger - anticoag_damping

    s = initial_state(n)

    for _ in range(10000):
        metropolis_step(s, J, h, beta)

    activated_fraction = (s == 1).mean()

    print("SIGIL4BLOOD demo")
    print("activated fraction:", activated_fraction)


if __name__ == "__main__":
    run_demo()
