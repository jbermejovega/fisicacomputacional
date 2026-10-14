"""Minimal dependency-free Ising Monte Carlo exercise for UGR SCI KIT."""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import random

def energy(spins, J=1.0, h=0.0):
    n = len(spins)
    return -J * sum(spins[i][j] * (spins[(i+1)%n][j] + spins[i][(j+1)%n])
                    for i in range(n) for j in range(n)) - h * sum(map(sum, spins))

def run(size=16, beta=0.4, sweeps=100, seed=42, J=1.0, h=0.0):
    if size < 2 or sweeps < 0 or not math.isfinite(beta) or beta < 0:
        raise ValueError("size >= 2, sweeps >= 0 and finite beta >= 0 required")
    if not all(map(math.isfinite, (J, h))):
        raise ValueError("J and h must be finite")
    rng = random.Random(seed)
    spins = [[rng.choice((-1, 1)) for _ in range(size)] for _ in range(size)]
    accepted = 0
    for _ in range(sweeps * size * size):
        i, j = rng.randrange(size), rng.randrange(size)
        s = spins[i][j]
        neighbors = (spins[(i+1)%size][j] + spins[(i-1)%size][j] +
                     spins[i][(j+1)%size] + spins[i][(j-1)%size])
        delta = 2 * s * (J * neighbors + h)
        if delta <= 0 or rng.random() < math.exp(-beta * delta):
            spins[i][j] = -s
            accepted += 1
    output = {"size": size, "beta": beta, "sweeps": sweeps, "seed": seed,
              "J": J, "h": h, "energy": energy(spins, J, h),
              "magnetization": sum(map(sum, spins)) / (size*size),
              "accepted": accepted, "spins": spins}
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return {"result": output, "sha256": hashlib.sha256(canonical.encode()).hexdigest()}

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--size", type=int, default=16)
    p.add_argument("--beta", type=float, default=0.4)
    p.add_argument("--sweeps", type=int, default=100)
    p.add_argument("--seed", type=int, default=42)
    args = p.parse_args()
    print(json.dumps(run(**vars(args)), sort_keys=True))
