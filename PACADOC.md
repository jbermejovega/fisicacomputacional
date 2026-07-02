# PACADOC — Física Computacional

```yaml
capsule:
  id: PACADOC_FISICA_COMPUTACIONAL_V1_0_0
  type: first_user_student_landing_document

  status:
    canonical: true
    normalized: true
    stable_release: true
    release_number: "1.0.0"
    student_facing: true
    UGR_ready: true
    safety_first: true
    accessibility_first: true
    reproducibility_first: true
    sigil_api_adaptable: true
    kqc_policy_bound: true
    course_maintenance_ready: true
    compliance_reviewable: true
    no_open_branch: true

  repository:
    owner: jbermejovega
    name: fisicacomputacional
    default_branch: main

  audience:
    - UGR students
    - first-time computational physics learners
    - teaching assistants
    - course reviewers

  kernel:
    - PACA_CORE
    - PACA_PDG
    - SIGIL
    - SIGIL_API
    - KQC
    - UAP
    - TRACE
    - PYTHON
    - JUPYTER
    - NUMERICAL_PHYSICS
```

## 1. What this repository is

This repository is a first-user educational repository for Computational Physics.

It is intended for students learning how to use code, numerical methods, notebooks, and reproducible workflows to solve physics problems.

The normalized rule is:

```text
physics result
=
method
+
code
+
parameters
+
units
+
replayable output
```

A numerical result is not complete if the path to reproduce it is missing.

## 2. First-user path

Start here:

```text
1. Read README.md.
2. Install Python or Miniconda.
3. Create a clean course environment.
4. Install Jupyter and scientific packages.
5. Open the first notebook or script.
6. Run examples in order.
7. Change one parameter at a time.
8. Record outputs and errors.
```

Recommended environment path:

```bash
conda env create -f environment.yml
conda activate fisica-computacional
python tools/validate_course_kqc.py
```

## 3. Student safety rule

Do not debug by changing many things at once.

Use:

```text
one error
one change
one rerun
one note
```

If something fails, record:

```text
operating system
Python version
environment name
file or notebook name
cell or line number
error message
last command executed
```

## 4. Accessibility rule

Learning material should remain readable under student conditions:

- small screens;
- fatigue;
- multilingual reading;
- unstable internet;
- first-time terminal use;
- first-time programming errors;
- mathematical anxiety;
- classroom time pressure.

Operational writing rule:

```text
one step per line
one command per block
one concept per exercise
no hidden assumptions
```

## 5. Reproducibility rule

A computational physics output is course-stable only if the execution path can be replayed.

```text
no replay → no certified result
```

Minimum reproducibility record:

```yaml
replay_record:
  repository: fisicacomputacional
  file: path/to/file.py_or_notebook.ipynb
  environment: course_environment_name
  python_version: "..."
  package_manager: conda_or_pip
  input_parameters: "..."
  units: "..."
  status: pass_or_error
```

## 6. SIGIL API / KQC teaching compliance

SIGIL API / KQC teaching compliance is the maintenance rule for adapting this course over time.

```text
course_patch
-> teaching_trace
-> SIGIL_API_adaptation_check
-> KQC_replay
-> compliance_certificate
-> reviewable_course_state
```

A SIGIL API adaptation must state:

```yaml
sigil_api_adaptation:
  old_surface: previous command, notebook pattern, API, or workflow
  new_surface: replacement command, notebook pattern, API, or workflow
  student_impact: what changes for learners
  migration_note: one-step explanation for teaching assistants
  replay_status: pass_or_error
```

A course correction is ready for review only when method, parameters, units, code path, and replay evidence remain visible.

The policy lives in `docs/SIGIL_API_KQC_TEACHING_COMPLIANCE.md` and the machine-readable invariant lives in `registry/sigil_api_kqc_teaching_compliance_v1.yaml`.

## 7. PACA/PACAPDG interpretation

Different systems may render the same computational object differently:

- Linux terminal;
- macOS terminal;
- Windows PowerShell;
- VS Code;
- JupyterLab;
- browser notebook.

The invariant is:

```text
Π(quo(r_i(X))) = Π(quo(r_j(X)))
```

Meaning:

```text
different student environments
same computational learning identity
```

## 8. Course conduct

Allowed:

- ask for help early;
- share error messages;
- compare outputs;
- document fixes;
- rerun notebooks or scripts;
- use accessible settings;
- explain approximations.

Forbidden:

- hiding errors;
- copying outputs without running or understanding the path;
- changing many dependencies without recording changes;
- presenting non-reproducible output as final;
- reporting numerical results without units, parameters, or method.

## 9. Minimal command discipline

Use commands in small blocks.

```bash
python --version
```

```bash
conda --version
```

```bash
jupyter --version
```

Do not paste long unknown command chains without reading them.

## 10. Teaching assistant checklist

```text
student can open terminal
student can identify environment
student can launch Jupyter
student can run first example
student can copy exact error
student can reset/recreate environment if needed
student can identify parameters and units
student can run the KQC course validator
```

## 11. Computational physics law

```text
numerical result valid
⇔
method stated
∧ parameters stated
∧ units stated
∧ code/path replayable
∧ output traceable
```

## 12. Final statement

This repository is PACADOC-normalized for UGR first users: it prioritizes clear entry, accessible learning, safe debugging, reproducible computation, traceable numerical physics, and KQC-compliant adaptation to SIGIL API changes.
