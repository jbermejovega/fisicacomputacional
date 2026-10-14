# SCI KIT — Statistical Mechanics as Gameplay (UGR)

This is an optional, reproducible computational physics learning kit. SIGIL/QUAZRIS/PYTRANADA terms describe software architecture; they are not physical theorems.

## Learning objectives
1. Define the 2D Ising Hamiltonian and its boundary conditions.
2. Implement single-spin Metropolis transitions with a seeded random generator.
3. Measure energy and magnetization; discuss equilibration, finite-size effects and autocorrelation.
4. Separate DSL (model), DSP (checks and evidence) and PACAPDG (execution dependencies).
5. Optionally map validated observables to SIGIL4GODOT scenes through QUAZRIS typed sockets.

## Physics
For periodic nearest-neighbor interactions on an LxL square lattice,
H(s) = -J sum_{<i,j>} s_i s_j - h sum_i s_i, s_i in {-1,+1}.
The Boltzmann weight is exp(-beta H)/Z. Metropolis accepts a proposal with min(1,exp(-beta DeltaH)).
A finite simulation does not prove a thermodynamic phase transition.

## Typed execution
QUAZRIS thick/thin ports connect typed input/output sockets; PYTRANADA transports data between sectors with explicit context and provenance. DSL specifies model parameters, DSP records proof/check obligations, PACAPDG orders operations. UAP gates external effects, KAPSYLA checks replay receipts.

Pipeline: Config -> Validate DSL -> Seed RNG -> Initialize -> Metropolis -> Observables -> DSP Checks -> PACAPDG Receipt -> optional QUAZRIS/PYTRANADA -> Godot render.

Run: python3 sci_kit/statmech_sigil/ising.py --size 16 --beta 0.4 --sweeps 100 --seed 42
No nonstandard Python packages required.
