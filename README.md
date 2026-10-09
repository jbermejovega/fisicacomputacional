# Física Computacional
## SIGILBOOK · libro abierto y cierre del curso

La [edición abierta del libro de Física Computacional](open_course/README.md) añade un
[capítulo de cierre transversal](open_course/CIERRE_FISICA_COMPUTACIONAL_2026.md),
ejercicios originales y un [codebook reproducible de SymPy](open_course/codebook/cierre_fisica_sympy.py).

Esta nueva capa **no reemplaza** las lecciones residentes ni afirma que las
extensiones (computación cuántica, combinatoria algebraica, sistemas complejos,
materia condensada o Humanidades Digitales) ya formaran parte del temario
impartido. Conserva copyright y licencias por archivo:
[Derechos y fuentes](open_course/DERECHOS_Y_FUENTES.md).

```bash
python open_course/codebook/cierre_fisica_sympy.py
python -m unittest discover -s open_course/tests -p 'test_*.py'
python tools/validate_course_kqc.py
```


## Curso abierto KRONE–HyperJarra (edición V1)

El curso existente se conserva y se amplía con un **wrap-up integrado** y capítulos originales sobre computación cuántica, combinatoria algebraica, materia condensada y bibliotecas de investigación/Humanidades Digitales. El índice reutiliza el linaje anterior HyperJarra de SIGILBOOK sin sustituirlo.

- [Inicio del libro abierto](curso_abierto/README.md)
- [Índice y lecturas de Física Computacional](curso_abierto/INDICE.md)
- [Wrap-up del curso](curso_abierto/CAPITULO_00_WRAP_UP.md)
- [Modelos y dibujos originales en SymPy](curso_abierto/codebooks/modelos_exactos.py)
- [Licencias específicas de esta edición](curso_abierto/LICENCIAS.md)

Los contenidos preexistentes del repositorio mantienen sus derechos y archivos. Los módulos nuevos tienen licencias expresas por alcance; la búsqueda local no arranca Ollama, llama.cpp ni LlamaIndex.


## PACADOC FIRST-USER NORMALIZATION

This repository is normalized as a replay-safe educational repository for Computational Physics students.

Start here:

- [`PACADOC.md`](PACADOC.md) — first-user / student landing guide
- [`docs/SIGIL_API_KQC_TEACHING_COMPLIANCE.md`](docs/SIGIL_API_KQC_TEACHING_COMPLIANCE.md) — SIGIL API / KQC Course Compliance policy
- [`environment.yml`](environment.yml) — stable course environment for local replay

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

## SIGIL API / KQC Course Compliance

Course improvements, global corrections, and SIGIL API adaptations are accepted through a KQC teaching gate:

```text
course_patch
-> teaching_trace
-> SIGIL_API_adaptation_check
-> KQC_replay
-> compliance_certificate
-> reviewable_course_state
```

Before publishing a teaching update, run:

```bash
python tools/validate_course_kqc.py
```

The validator keeps `README.md`, `PACADOC.md`, the compliance policy, registry, environment file, and CI workflow connected. Physics correctness still requires method, parameters, units, code path, and replayable output.

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

Recommended course environment:

```bash
conda env create -f environment.yml
conda activate fisica-computacional
python tools/validate_course_kqc.py
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
