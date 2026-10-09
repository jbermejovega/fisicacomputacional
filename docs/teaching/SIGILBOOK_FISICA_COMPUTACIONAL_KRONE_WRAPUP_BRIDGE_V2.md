# Física Computacional · Wrap-up KRONE y vínculo con SIGILBOOK V2

**Proyecto público:** Física Computacional · Universidad de Granada  
**Dirección y autoría docente declarada:** Jara Juana Bermejo Vega  
**Fecha de reconciliación:** 9 de octubre de 2026  
**Ámbito:** proyección docente pública de una faceta del libro privado SIGILBOOK; no publicación total del repositorio privado.

## 1. Qué está publicado ahora

- [Capítulo de cierre original](../../open_course/CIERRE_FISICA_COMPUTACIONAL_2026.md): recapitulación desde la pregunta física al modelo, la discretización, el código, la validación y la interpretación.
- [KRONE y competencias](../../open_course/krone/cierre_krone_v1.yaml): objetivos de aprendizaje con evidencia, error, unidades y derechos.
- [Codebook SymPy](../../open_course/codebook/cierre_fisica_sympy.py): Ising finito exacto, Hadamard, inversión de Möbius y dibujo SVG original bajo demanda.
- [Derechos y fuentes](../../open_course/DERECHOS_Y_FUENTES.md): alcance explícito CC BY 4.0 de los textos nuevos, MIT para nuevo código y límites de obras visuales anteriores.

El repositorio anterior ya impartía fundamentos de programación, Linux, números aleatorios, dinámica orbital, Ising y Schrödinger. Computación cuántica más avanzada, combinatoria algebraica, sistemas complejos, materia condensada y Humanidades Digitales son **propuestas de ampliación**, no lecciones impartidas retroactivamente.

## 2. Linaje de libro canónico → curso

El SIGILBOOK privado conserva el libro de Física Computacional con dieciséis capítulos originales y cuatro capítulos complementarios fuente (17–20), integrados en su commit
[63c01f0001074d5f76294811c28ee3288c13e574](https://github.com/jbermejovega/sigilbook/commit/63c01f0001074d5f76294811c28ee3288c13e574), PR #3674.

| SIGILBOOK interno | Proyección autónoma y pública |
| --- | --- |
| Fundamentos numéricos y simulación | capítulos originales y guías de este repositorio |
| Estadística/Ising y Schrödinger | código y prácticas residentes + ejercicio de cierre |
| Capítulo 17: computación cuántica | ejemplo exacto de Hadamard y ruta de continuación |
| Capítulo 18: combinatoria algebraica | Möbius del retículo B₂, sin copiar MIT OCW |
| Capítulo 19: bibliotecas/HD UGR | procedencia bibliográfica, derechos, recursos institucionales |
| Capítulo 20: revisión científica y polikategorías CCMS | alfabetización sobre límites de pruebas y fuentes; NO datos de revisiones reales |

La columna derecha es **suficiente por sí sola**: no requiere instalar, clonar o acceder al repositorio privado SIGILBOOK.

## 3. Trazabilidad matemática y límites de afirmaciones

\[
\mathrm{KRONE}:
(\mathrm{Modelo},\mathrm{Datos},\mathrm{Método},\mathrm{Parámetros})
\rightsquigarrow
(\mathrm{Resultado},\mathrm{Evidencia},\mathrm{Incertidumbre},\mathrm{Explicación}).
\]

Una correspondencia entre temas no establece igualdad entre teorías. La exactitud simbólica de un pequeño Hamiltoniano tampoco acredita una simulación física general. El **modelo CCMS de invitaciones para revisar manuscritos** es una herramienta de trabajo del repositorio privado, no una parte ejecutable ni un corpus abierto de manuscritos en esta asignatura.

### Repaso final del curso

Para cada práctica, exigir:
- pregunta contrastable e hipótesis;
- magnitudes, parámetros, unidades y condiciones de contorno;
- implementación reproducible con versión y comando;
- validación exacta, caso límite o convergencia;
- figura generada con código y procedencia;
- discusión de errores, validez y limitaciones.

Esta relación es una guía de repaso y no modifica fechas, notas, evaluaciones ni el programa histórico de ninguna cohorte.

## 4. Derechos, apertura y reproducción

La edición nueva tiene las licencias específicas descritas en open_course/DERECHOS_Y_FUENTES.md. **Este documento se incorpora como texto original a esa misma edición sólo en la medida permitida por los derechos de su autora** y no cambia las licencias de documentos históricos. El código anterior, el curso del MIT, notas de John Watrous, documentos restringidos de la Biblioteca UGR y trabajos científicos de terceros **no se copian ni relicencian**.

Es imprescindible distinguir: fuente abierta a lectura ≠ obra con licencia abierta de reutilización; código MIT ≠ permisos ilimitados sobre cualquier figura artística.

## 5. Verificación

**Contrato docente local**: el validador existente tools/validate_course_kqc.py conserva las entradas README, PACADOC, entorno y CI.  
**Ejecución prevista**, desde el repositorio público:

    python open_course/codebook/cierre_fisica_sympy.py
    python -m unittest discover -s open_course/tests -p 'test_*.py' -v
    python tools/validate_course_kqc.py

La prueba de redirección y los metadatos source-bound se verifican al preparar esta proyección. No debe afirmarse que los tests residentes han pasado si no se cuenta con una ejecución real.

**ONE FACT → ONE SOURCE-BOUND MODEL → MULTIPLE PEDAGOGICAL VIEWS · PLURA MANENT.**
