# Capítulo de cierre · Física Computacional
## Del modelo físico a la simulación reproducible · Edición abierta 0.1

**Autora y dirección académica:** Jara Juana Bermejo Vega · Universidad de Granada  
**Identidad:** FISICACOMPUTACIONAL_CIERRE_KRONE_SIGILBOOK_V1  
**Estado:** capítulo original para revisión docente. No modifica retroactivamente el programa impartido ni acredita una evaluación oficial.  
**Derechos:** © 2026 Jara Juana Bermejo Vega. Para el alcance de esta edición original véase [Derechos y procedencia](DERECHOS_Y_FUENTES.md).

> Física computacional no consiste en producir una figura plausible. Consiste en transformar un problema físico bien definido en un experimento numérico cuya corrección, precisión, límites y procedencia pueden someterse a examen.

### 1. Qué conecta las lecciones del repositorio

| Material residente | Competencia | Pregunta del cierre |
|---|---|---|
| [Introducción a los ordenadores](../01_Introduccion_Que_son_los_ordenadores/) | Representación y límites | ¿Qué información representa una variable? |
| [C/C++ y Python](../00_herramientas/) | Algoritmos, pruebas y tipos | ¿Cómo separar modelo físico de implementación? |
| [Linux, SSH y Git](../02_Linux/) | Entornos reproducibles | ¿Puede otra persona repetir el cálculo? |
| [Fortran](../03_Lenguaje_Fortran/) | Cómputo científico | ¿Se puede optimizar sin modificar observables? |
| [Números aleatorios](../03_ejercicio_numeros_aleatorios/) | Monte Carlo | ¿Cómo se mide el error de muestreo? |
| [GNUplot](../04_GNUplot/) | Comunicación visual | ¿Qué unidades, escalas y condiciones aparecen? |
| [Sistema solar](../05_Sistema_Solar/) y [cohete](../08_Leccion_Cohete/) | Integración temporal | ¿Se preservan los invariantes del modelo? |
| [Monte Carlo e Ising](../06_Monte_Carlo_Ising/) | Estadística y colectividad | ¿Equilibrio físico o convergencia aparente? |
| [Schrödinger](../07_Leccion_Schrodinger/) | Estados y evolución | ¿Es hermítico el Hamiltoniano? |
| [Voluntarios](../09_Voluntarios/) | Autonomía científica | ¿Se puede defender y refutar la simulación? |

Estas rutas corresponden a **materiales existentes**. Computación cuántica, materia condensada avanzada, combinatoria algebraica y Humanidades Digitales se presentan como **ampliaciones transversales**, no como lecciones impartidas que se hayan verificado retrospectivamente.

### 2. Ciclo de un experimento computacional

Para estado físico \(x\), parámetros \(\theta\) y observable \(O(x)\):

\[
\boxed{\text{pregunta}\to\text{modelo}\to\text{discretización}\to
\text{código}\to\text{validación}\to\text{incertidumbre}\to
\text{interpretación}\to\text{reproducción}}
\]

1. **Modelo:** grados de libertad, ecuaciones, hipótesis, dimensiones, condiciones iniciales y de contorno.
2. **Algoritmo:** método, tamaño de paso, malla, temperatura, número de muestras y tolerancia.
3. **Ejecución:** versión del software, semilla, sistema, parámetros, datos y comando.
4. **Validación:** solución exacta, identidad, invariante, convergencia o caso límite.
5. **Inferencia:** separar errores de discretización, truncamiento, muestreo, redondeo y modelo.
6. **Comunicación:** figura original, código regenerador, incertidumbre y procedencia.

Una ejecución reproducible de un cálculo incorrecto sigue siendo incorrecta: la reproducibilidad no sustituye la validación física.

### 3. Dinámica clásica: conservar no es dibujar

En \( \dot q=p/m \), \( \dot p=F(q) \), Verlet ofrece error global \(O(\Delta t^2)\) bajo las hipótesis habituales. El diagnóstico de una órbita debe incluir energía mecánica, convergencia con el paso temporal y estabilidad, no solo una animación.

**Práctica A.** Comparar dos pasos temporales para una órbita, representar \(E(t)-E(0)\) y explicar por qué una figura atractiva no acredita precisión. No presuponer que un integrador general conserve exactamente la energía.

### 4. Física estadística: Ising y Monte Carlo

Para \(N\) espines \(s_i\in\{-1,+1\}\) con contorno periódico:

\[
H(s)=-J\sum_{i=1}^{N}s_i s_{i+1}-h\sum_{i=1}^{N}s_i,\quad s_{N+1}=s_1.
\]

Con \(k_B=1\), \(\beta=1/T\), la función de partición y un observable se calculan mediante

\[
Z=\sum_s e^{-\beta H(s)},\qquad
\langle O\rangle=\frac{1}{Z}\sum_s O(s)e^{-\beta H(s)}.
\]

Metropolis acepta un cambio con \(p=\min(1,\exp(-\beta\,\Delta H))\). Los pasos correlacionados no deben tratarse automáticamente como muestras independientes.

**Práctica B.** Enumerar los \(2^4=16\) estados del anillo de cuatro espines y comparar \(Z\), energía media y magnetización con muestreo Monte Carlo. El [codebook SymPy](codebook/cierre_fisica_sympy.py) proporciona la referencia exacta; no justifica por sí mismo el límite termodinámico.

### 5. Mecánica cuántica: preservar la norma

Para \(H=H^\dagger\), la evolución exacta es

\[
|\psi(t)\rangle=e^{-iHt/\hbar}|\psi(0)\rangle,\quad
\langle\psi(t)|\psi(t)\rangle=\langle\psi(0)|\psi(0)\rangle.
\]

En un esquema numérico hay que controlar las condiciones de frontera, la hermiticidad discreta y la convergencia espacial y temporal.

**Práctica C.** Calcular un estado o paquete de ondas, refinar la malla y comprobar la norma. Una pérdida de norma puede indicar un fallo numérico, no un fenómeno físico.

### 6. Puente hacia computación cuántica y materia condensada

La puerta Hadamard produce

\[
H|0\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2},
\qquad P(0)=P(1)=\frac12.
\]

El código verifica exactamente \(H^\dagger H=I\). Este es el inicio de una ampliación sobre qubits y circuitos, no una afirmación de que el repositorio anterior impartiera ya toda la computación cuántica.

En materia condensada, el puente va de Ising a Hamiltonianos sobre redes, bandas, transporte y localización. En sistemas complejos va de leyes locales a propiedades colectivas, correlaciones y escalas. Son rutas de continuación del libro.

### 7. Puente a combinatoria algebraica

En el retículo booleano \(B_n\), la función de Möbius es

\[
\mu(S,T)=(-1)^{|T\setminus S|}\quad(S\subseteq T).
\]

La inversión de Möbius permite recuperar funciones a partir de sumas acumuladas y conecta con inclusión-exclusión y polinomios de grafos, útiles en mecánica estadística. El codebook implementa la inversión en \(B_2\) y puede generar un dibujo vectorial original del diagrama de Hasse.

**Referencia externa:** [MIT OpenCourseWare 18.212 Algebraic Combinatorics, Spring 2019](https://ocw.mit.edu/courses/18-212-algebraic-combinatorics-spring-2019/download/). Se referencia su materia; no se redistribuyen las notas ni sus figuras.

### 8. Bibliotecas científicas y Humanidades Digitales

Los resultados computacionales también son documentos de investigación: requieren metadatos, identificadores, métodos, versiones, derechos, autoría y preservación. La accesibilidad técnica de un PDF o una colección **no equivale** a un permiso de reutilización.

**Práctica D.** Crear una ficha de procedencia de una figura: modelo, código generador, dataset, versiones, hipótesis, fuente, licencia y limitaciones.

Lecturas para esta ampliación:
- Morales-del-Castillo, Tamayo Ramírez y Peis Redondo (2020), *Bibliotecas de investigación y Humanidades Digitales en España*, [DOI 10.5944/RHD.VOL.5.2020.27653](https://doi.org/10.5944/RHD.VOL.5.2020.27653).
- [Biblioteca UGR · Digital Research in the Arts and Humanities](https://bibliotecaugr.libguides.com/digital_research) (algunos recursos requieren identificación institucional).
- [Digibug · Repositorio UGR](https://digibug.ugr.es/).

### 9. KRONE: unidad de aprendizaje tipada

Cada ejercicio ocupa una ocurrencia propia:

\[
K_e=(id, modelo, método, parámetros, unidades, evidencia, error,
licencia, replay)_e.
\]

El tipo controla la **estructura y procedencia**; no demuestra la física. La docente, la comparación con evidencia y la evaluación académica son autoridades distintas. Véase el [manifiesto KRONE](krone/cierre_krone_v1.yaml).

### 10. Proyecto integrador y autoevaluación

Elegir una ruta: (A) dinámica orbital, (B) Ising exacto/Monte Carlo, (C) Schrödinger, (D) enumeración combinatoria. Entregar **una pregunta falsable, ecuaciones y unidades, código ejecutable, una validación, una figura propia con su fuente generadora y una discusión de errores**. Añadir el comando de reproducción, parámetros, bibliografía y licencia de cada recurso.

Rúbrica **orientativa** para autoevaluación (no sustituye el sistema oficial):

| Criterio | Peso |
|---|---:|
| Formulación y supuestos | 25 % |
| Método e implementación | 25 % |
| Validación y cuantificación del error | 25 % |
| Interpretación | 15 % |
| Reproducibilidad y procedencia | 10 % |

**No se evalúa solo rendimiento numérico:** explicar *por qué* funciona y *cuándo* falla forma parte del resultado científico.

### 11. Checklist de cierre

- [ ] Distingo modelo, algoritmo, código, datos y figura.
- [ ] Explico condiciones, parámetros y unidades.
- [ ] Verifico un caso límite o un invariante físico.
- [ ] Cuantifico errores y dependencia de escala.
- [ ] Puedo repetir el cálculo en un entorno documentado.
- [ ] Identifico lo que la simulación **no** ha demostrado.
- [ ] Atribuyo correctamente software, bibliografía y arte.
- [ ] Diferencio materiales ya impartidos de ampliaciones futuras.

\[
\boxed{\mathrm{Física\ computacional}
=\mathrm{modelo}+\mathrm{algoritmo}+\mathrm{error}
+\mathrm{evidencia}+\mathrm{interpretación}}
\]

**SIGILBOOK es el atlas conceptual; este repositorio ofrece una de sus facetas docentes y reproducibles.** No es necesario instalar SIGIL para resolver las actividades de cierre.
