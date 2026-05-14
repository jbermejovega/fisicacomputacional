# Física Computacional

## PACADOC FIRST-USER NORMALIZATION

This repository is normalized as a replay-safe educational repository for Computational Physics students.

Start here:

- [`PACADOC.md`](PACADOC.md) — first-user / student landing guide

## What this repository is

This repository supports learning computational physics through code, notebooks, numerical experiments, and reproducible workflows.

Core rule:

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

## First student path

```text
1. Install Python or Miniconda.
2. Create a clean course environment.
3. Install Jupyter and scientific packages.
4. Open the first notebook or script.
5. Run examples in order.
6. Change one parameter at a time.
7. Save outputs and errors.
8. Ask for help with the exact error message.
```

## Debugging rule

```text
one error
one change
one rerun
one note
```

Do not debug by changing many things at once.

## Reproducibility rule

```text
no replay → no certified result
```

A result is complete only when the path can be replayed and the method, parameters, and units are visible.

## PACA/PACAPDG invariant

```text
Π(quo(r_i(X))) = Π(quo(r_j(X)))
```

Meaning:

```text
different machines / notebooks / environments
same computational learning identity
```

## Minimal student record

When something works or fails, record:

```text
operating system
Python version
environment name
file or notebook name
cell or line number
input parameters
units
output or error message
```

## Final law

```text
numerical result valid
⇔
method stated
∧ parameters stated
∧ units stated
∧ code/path replayable
∧ output traceable
```
