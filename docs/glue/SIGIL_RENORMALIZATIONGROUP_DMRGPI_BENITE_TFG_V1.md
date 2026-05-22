# SIGIL_RENORMALIZATIONGROUP_DMRGPI_BENITE_TFG_V1

## Scope

This artifact defines a replay-safe method layer for applying a SIGIL-style renormalization group to the Benite TFG computational-physics context and constructing three tensor-train geometries:

- `VORTEX_TENSOR_TRAIN`
- `VOID_TENSOR_TRAIN`
- `ALHAMBRA_TENSOR_TRAIN`

through a DMRGΠ workflow.

---

## Authorship / context

```yaml
authorship:
  TFG_author: Marina Benitez Sanchez
  framework_author: Jara Juana Bermejo Vega
  affiliation: University of Granada
  line: computational_physics_quantum_computation
```

---

## Core equation

```text
SIGILRENORMALIZATIONGROUP
=
SIGIL gate
+ coarse-graining Φ
+ invariant projection Π
+ replay trace
```

with:

```text
Π = PACA_PDG
PDG = Fix(Π)
KAPSYLA(X) ⇔ Π(quo(X)) = quo(X)
```

---

## Method pipeline

```mermaid
flowchart LR
    A[Benite TFG model] --> B[SIGIL admissibility]
    B --> C[Tensorization]
    C --> D[DMRG sweep Φ]
    D --> E[Π projection]
    E --> F[Renormalized tensor train]
    F --> G[KAPSYLA replay closure]
```

---

## DMRGΠ definition

```text
DMRGΠ(X)
=
Π(DMRG_sweep(X))
```

where `DMRG_sweep` performs local tensor optimization and `Π` extracts the invariant replay-safe representative.

Operationally:

```text
local tensor update
→ truncation / compression
→ invariant check
→ replay certificate
```

---

## Tensor train families

### 1. VORTEX_TENSOR_TRAIN

```yaml
VORTEX_TENSOR_TRAIN:
  role: circulation_preserving_tensor_train
  geometry: cyclic_boundary_or_spiral_ordering
  invariant:
    - winding_like_order
    - phase_flow_consistency
    - local_update_preserves_global_circulation
  dmrgpi_rule:
    - optimize local bonds
    - preserve vortex invariant under Π
```

Interpretation:

```text
VORTEX = tensor train where local updates preserve a global circulation class.
```

---

### 2. VOID_TENSOR_TRAIN

```yaml
VOID_TENSOR_TRAIN:
  role: obstruction_gap_tensor_train
  geometry: missing_center_or_forbidden_subspace
  invariant:
    - null_sector
    - forbidden_lift
    - contextual_gap
  dmrgpi_rule:
    - compress around void sector
    - preserve obstruction under Π
```

Interpretation:

```text
VOID = tensor train organized around an explicit non-admissible or null sector.
```

---

### 3. ALHAMBRA_TENSOR_TRAIN

```yaml
ALHAMBRA_TENSOR_TRAIN:
  role: patterned_symmetry_tensor_train
  geometry: tiled_quasiperiodic_or_motif_repeated_ordering
  invariant:
    - local_motif_consistency
    - global_pattern_reconstruction
    - symmetry_aware_compression
  dmrgpi_rule:
    - optimize motif blocks
    - preserve reconstruction under Π
```

Interpretation:

```text
ALHAMBRA = tensor train where repeated local motifs reconstruct a global invariant pattern.
```

---

## SIGILRG algorithm

```python
class SIGILRenormalizationGroup:
    def __init__(self, projector, sigil_gate, trace):
        self.projector = projector
        self.sigil_gate = sigil_gate
        self.trace = trace

    def step(self, tensor_train):
        assert self.sigil_gate(tensor_train)
        updated = dmrg_local_sweep(tensor_train)
        projected = self.projector(updated)
        self.trace.record(projected)
        return projected

    def run(self, tensor_train, n_steps):
        state = tensor_train
        for _ in range(n_steps):
            state = self.step(state)
        return state
```

---

## Minimal DMRGΠ pseudo-code

```python
def dmrgpi_step(train, local_solver, projector, trace):
    for bond in train.bonds():
        train = local_solver.optimize_bond(train, bond)
        train = train.truncate_admissibly(bond)
        train = projector(train)
        trace.append({"bond": bond, "pi_fixed": projector.is_fixed(train)})
    return train
```

---

## Repository routing

```yaml
routing:
  k:
    target: sigilbook
    role: theorem_kernel_and_canonical_method
  q:
    target: sigil4cython
    role: cython_quantum_projection_runtime
  c:
    target: fisicacomputacional
    role: compiled_strict_typed_computational_physics_runtime
```

---

## Open repository gate

```text
open_repo(C)
⇔
compiled
∧ strict_typed
∧ reproducible
∧ kapsyla_stable
```

---

## Final compression

```text
SIGILRG = renormalization with admissibility gates
DMRGΠ   = tensor-train optimization followed by invariant projection
VORTEX  = circulation invariant
VOID    = obstruction invariant
ALHAMBRA= motif reconstruction invariant
```

**KANONIKAL. SIGILRG × DMRGΠ × BENITE_TFG SEALED.**
