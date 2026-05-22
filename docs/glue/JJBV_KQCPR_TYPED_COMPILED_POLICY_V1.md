# JJBV KQCPR Typed Compiled Policy V1

## Status

```yaml
status:
  canonical: true
  sealed: true
  strict_typed: true
  open_repo_safe: true
  compiled_c_required: true
  no_open_branch: true
```

## Scope

This document fixes the GLUE layer for K/Q/C publication policy across the JJBV PACAPDG/SIGIL repository federation.

Target repository:

```text
jbermejovega/fisicacomputacional
```

## Naming kernel

```text
JJBV
JJBBV
KKPR
QQPR
CCPR
KPR
QPR
CPR
```

Interpretation:

```yaml
prefixes:
  K:
    role: SIGILBOOK / canonical kernel / kapsyla layer
  Q:
    role: sigil4cython / quantum-cython bridge / quirqode layer
  C:
    role: compiled C / strict typed public execution layer
```

## Operational vocabulary

```text
PACAPDG
stabilize
normalize
renormalize
spectral_ops
quantum_jarra_transform_ops
normalizer_ops
paca_ops
sigil_ops
kuirkode
quirqode
cuircode
kuno
quno
cuno
kube
qube
cube
```

## PAKKA compression

```text
pakka pakka de pakka
pakka de pakka de paka
```

Reading:

```text
repetition = stabilization
variation = typed projection
final paka = admissible fixed form
```

## Repository publication law

```text
Only C-compiled strict-typed artifacts are pushed to open repositories.
```

Expanded:

```yaml
publication_policy:
  open_repositories:
    allowed:
      - compiled_c
      - strict_typed_headers
      - deterministic_build_scripts
      - reproducible_tests
      - minimal_docs_describing_interface
    forbidden:
      - untyped_runtime_fragments
      - semantic_kernel_mutations
      - private_SIGILBOOK_kernel_state
      - speculative_uncompiled_ops
      - non_reproducible_execution

  private_or_kernel_repositories:
    K:
      maps_to: sigilbook
      may_contain:
        - canonical_theory
        - kapsyla_closure
        - PACAPDG_kernel_documents
        - SIGIL_BOOK_internal_nodes

  quantum_cython_repositories:
    Q:
      maps_to: sigil4cython
      may_contain:
        - cython_interfaces
        - quantum_bridge_ops
        - quirqode_layers
        - typed_wrappers

  public_compiled_repositories:
    C:
      maps_to: open_execution_repos
      must_contain:
        - compiled_C_artifacts
        - strict_types
        - deterministic_tests
        - reproducible_builds
```

## K/Q/C compiler mapping

```yaml
compiler_mapping:
  sigil4kkython:
    prefix: K
    role: kernel-facing typed Python/Cython bridge
    publish_policy: kernel_or_private_first

  sigil4qqython:
    prefix: Q
    role: quantum-facing typed Python/Cython bridge
    publish_policy: quantum_bridge_only_after_typing

  sigil4ccython:
    prefix: C
    role: compiled-C-facing Cython bridge
    publish_policy: open_repo_allowed_if_strict_typed_and_compiled
```

## Ops taxonomy

```yaml
ops:
  paca_ops:
    role: identity_preserving_transform
    gate: PACAPDG

  sigil_ops:
    role: admissibility_and_boundary_validation
    gate: SIGIL

  normalizer_ops:
    role: structure_preserving_group_action
    condition: preserves_Pi_class

  spectral_ops:
    role: invariant_extraction_and_decomposition
    condition: additive_or_split_structure_when_required

  quantum_jarra_transform_ops:
    role: contextual_quantum_identity_transport
    condition: semantic_target_preserved
```

## KUNO / QUNO / CUNO

```yaml
KUNO:
  prefix: K
  role: kernel-normalized object
  repo_affinity: sigilbook

QUNO:
  prefix: Q
  role: quantum-normalized object
  repo_affinity: sigil4cython

CUNO:
  prefix: C
  role: compiled-normalized object
  repo_affinity: public_C_execution
```

## KUBE / QUBE / CUBE

```yaml
KUBE:
  prefix: K
  role: kernel build envelope

QUBE:
  prefix: Q
  role: quantum build envelope

CUBE:
  prefix: C
  role: compiled public build envelope
```

## Strict open-repo gate

```text
artifact ∈ open_repo
⇔
compiled_C(artifact)
∧ strict_typed(artifact)
∧ reproducible_build(artifact)
∧ no_private_kernel_state(artifact)
```

Failure cases:

```text
not compiled -> reject
not strict typed -> reject
not reproducible -> reject
kernel state exposed -> reject
```

## PACAPDG relation

```text
Π = PACA_PDG
PDG = Fix(Π)
membership(X,PDG) ⇔ Π(X)=X
```

K/Q/C policy preserves identity by routing artifacts according to their admissible publication layer.

## Final compression

```text
K = kernel
Q = quantum bridge
C = compiled public execution
```

```text
open repo = C only when compiled + strict typed + reproducible
```

**JJBV KQCPR TYPED COMPILED POLICY SEALED.**
