# SIGILBOOK · Física Computacional · Edición abierta 0.1

**Autora y dirección científica:** Jara Juana Bermejo Vega (UGR).  
**Proyecto:** faceta docente del libro SIGILBOOK, desplegada en el repositorio público de Física Computacional.  
**Estado de publicación:** primera edición de trabajo revisable. Incluye un **capítulo de cierre completo**, su codebook y el contrato docente KRONE. **No** es todavía la edición definitiva de todas las partes del libro.

## Leer

- [Capítulo 0 · Cierre transversal de Física Computacional](CIERRE_FISICA_COMPUTACIONAL_2026.md): qué conecta los modelos físicos, algoritmos, validaciones y evidencias.
- [KRONE · Índice tipado de competencias](krone/cierre_krone_v1.yaml): cinco objetivos, rutas, condiciones y evidencias de aprendizaje.
- [Codebook original SymPy](codebook/cierre_fisica_sympy.py): Ising exacto, qubits y combinatoria; produce un diagrama SVG original.
- [Derechos, bibliografía y atribución](DERECHOS_Y_FUENTES.md).
- [Vínculo canónico con SIGILBOOK V2](../docs/teaching/SIGILBOOK_FISICA_COMPUTACIONAL_KRONE_WRAPUP_BRIDGE_V2.md): correspondencia con los 20 capítulos fuente y límites de acceso; este curso funciona de forma autónoma.

## Ejecutar

Preparar el entorno docente residente (ya incluye SymPy):

    conda env create -f environment.yml
    conda activate fisica-computacional

Ejecutar, desde la raíz del repositorio:

    python open_course/codebook/cierre_fisica_sympy.py

Guardar el diagrama reproducible B₂:

    python open_course/codebook/cierre_fisica_sympy.py --svg figuras/reticulo_B2_original.svg

Comprobar las invariantes del codebook:

    python -m unittest discover -s open_course/tests -p 'test_*.py' -v
    python tools/validate_course_kqc.py

El dibujo se genera bajo demanda, no contiene material de MIT OCW, Watrous ni logos institucionales externos.

## Ruta pedagógica

El curso existente conecta Linux, C/C++ y Python, Fortran, GNUPLOT, números aleatorios, dinámica orbital, Ising y Schrödinger. La **continuación propuesta** prepara redes complejas, modelos de materia condensada, computación cuántica, combinatoria algebraica y Humanidades Digitales. Se conserva la distinción entre material ya residente y nuevos capítulos.

El criterio científico rector es que una salida numérica necesita **método, parámetros, unidades, comparación con evidencia, error e interpretación**. El contrato KRONE organiza la información sin sustituir el juicio de la docente.

## Derechos y apertura

Los textos nuevos de esta edición tienen atribución © Jara Juana Bermejo Vega y se ofrecen bajo **CC BY 4.0 exclusivamente en los archivos de la edición identificados en DERECHOS_Y_FUENTES.md**. El nuevo código generado para el curso se distribuye bajo **MIT**, cuyo texto acompaña al codebook. Las expresiones gráficas originales se reservan separadamente cuando exista un derecho de autor aplicable; no se atribuye exclusividad sobre hechos matemáticos ni se licencian de forma automática materiales anteriores o de terceros.

El acceso abierto a una URL no acredita derecho de redistribución; por eso Watrous, MIT OCW y la Biblioteca UGR se citan por enlace y no se copian.

**SIGILBOOK → libro de teorías · Física Computacional → laboratorio educativo verificable · KRONE → competencia tipada.**
