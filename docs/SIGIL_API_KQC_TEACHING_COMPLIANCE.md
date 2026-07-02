# SIGIL_API_KQC_TEACHING_COMPLIANCE_V1

Copyright (c) JJBV / Jara Juana Bermejo Vega. All rights reserved.

## Purpose

This document defines the course-maintenance glue for `jbermejovega/fisicacomputacional`.

The repository is a teaching surface for computational physics. It may be corrected, updated, and adapted to new SIGIL API surfaces over time, but every change must preserve student readability, replayability, units, parameters, and KQC compliance.

```text
course_patch
-> teaching_trace
-> SIGIL_API_adaptation_check
-> KQC_replay
-> compliance_certificate
-> publishable_course_state
```

## KQC teaching policy

```text
K = course kernel: notebook, script, exercise, environment, or explanation
Q = quotient over student machines and classroom contexts
C = certificate: replay evidence with method, parameters, units, and output trace
```

A teaching artifact is accepted only when:

```text
method stated
and parameters stated
and units stated
and code/path replayable
and output traceable
and student impact visible
```

The short law remains:

```text
no replay -> no certified result
```

## SIGIL API adaptation rule

When the course adapts to a new SIGIL API, the change must record:

```yaml
sigil_api_adaptation:
  old_surface: previous command, notebook pattern, API, or workflow
  new_surface: replacement command, notebook pattern, API, or workflow
  student_impact: what changes for learners
  migration_note: one-step explanation for teaching assistants
  replay_status: pass_or_error
  kqc_certificate: required_before_publication
```

A SIGIL API update is not a release authority by itself. It is a trace input that becomes course authority only after KQC replay and instructor review.

## Global correction rule

Global corrections are allowed when they improve the course and remain replay-safe.

Allowed global corrections:

- clarify student instructions;
- refresh supported Python/Jupyter environment guidance;
- add or repair reproducibility metadata;
- update notebooks or scripts for current scientific Python APIs;
- adapt examples to new SIGIL API surfaces;
- improve accessibility, wording, and classroom sequencing;
- add CI checks that validate course policy without heavy dependencies.

Rejected global corrections:

- hiding a failing output;
- changing many scientific parameters without a trace note;
- removing units or method statements;
- publishing a notebook or script without a replay path;
- treating branch topology as proof;
- transporting identity or copyright authority from another repository.

## Maintenance cadence

The course can be improved every now and then under this invariant:

```text
small_patch
-> explicit teaching reason
-> replay check
-> compliance check
-> reviewable PR
```

The recommended cadence is:

```text
before term: environment and first-run check
mid term: examples, typos, API drift, classroom pain points
after term: structural corrections and next-release notes
whenever SIGIL API changes: adaptation note plus KQC replay
```

## Required files

```yaml
required_files:
  readme: README.md
  first_user_doc: PACADOC.md
  policy: docs/SIGIL_API_KQC_TEACHING_COMPLIANCE.md
  registry: registry/sigil_api_kqc_teaching_compliance_v1.yaml
  validator: tools/validate_course_kqc.py
  environment: environment.yml
  ci: .github/workflows/course-kqc-compliance.yml
```

## CI certificate

The minimum compliance certificate is:

```bash
python tools/validate_course_kqc.py
```

This check validates that the teaching policy, registry, environment file, README, and PACADOC remain connected.

It does not prove the physics. It proves that the course update did not remove the KQC teaching contract.

## Publication gate

A course state is publishable when:

```text
README points to PACADOC and compliance policy
PACADOC keeps first-user readability
registry records the KQC compliance invariant
environment file gives a stable course setup
validator passes
SIGIL API adaptations include migration notes
JJBV attribution and rights notice are preserved
```
