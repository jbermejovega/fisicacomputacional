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
  status: pass_or_error
```

## 6. PACA/PACAPDG interpretation

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

## 7. Course conduct

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

## 8. Minimal command discipline

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

## 9. Teaching assistant checklist

```text
student can open terminal
student can identify environment
student can launch Jupyter
student can run first example
student can copy exact error
student can reset/recreate environment if needed
student can identify parameters and units
```

## 10. Computational physics law

```text
numerical result valid
⇔
method stated
∧ parameters stated
∧ units stated
∧ code/path replayable
∧ output traceable
```

## 11. Final statement

This repository is PACADOC-normalized for UGR first users: it prioritizes clear entry, accessible learning, safe debugging, reproducible computation, and traceable numerical physics.
