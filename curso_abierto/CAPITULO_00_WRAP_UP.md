# Capítulo 0 — Wrap-up de Física Computacional

**Física Computacional (UGR) · Jara Juana Bermejo Vega · edición abierta V1**

## 0.1. Qué hemos aprendido realmente

La física computacional no consiste en utilizar un ordenador para obtener una cifra. Consiste en pasar de una hipótesis física a un **modelo matemático**, elegir una **representación computacional**, controlar el **error** y volver a una **interpretación física falsable**. El algoritmo es una parte de la argumentación, nunca su sustituto. Este capítulo articula las actividades ya existentes del repositorio: terminal y lenguajes científicos, métodos numéricos, dinámica orbital, aleatoriedad, Monte Carlo–Ising, ecuación de Schrödinger y problemas diferenciales.

Una entrega científica reproducible debe separar seis capas: (i) objeto físico y simplificaciones, (ii) ecuaciones y observables, (iii) discretización, (iv) algoritmo y estructura de datos, (v) validación y estadística, (vi) relato de las limitaciones. KRONE es aquí una ficha docente tipada para mantener esas capas separadas.

## 0.2. Revisión de programación científica

En la práctica, una matriz NumPy y un array Fortran pueden representar el mismo observable, pero no son la misma ocurrencia de cálculo: importan precisión, orden de memoria, tipos, índices, dependencias, versión de compilador y semilla. Una ejecución de C/C++ también debe indicar optimizaciones e información de compilación si se comparan rendimientos.

**Actividad de cierre:** toma una de las prácticas de `03_Lenguaje_Fortran`, documenta su entrada, salida, coste temporal aproximado y prueba de regresión; escribe después una versión de referencia en Python. No afirmes equivalencia sólo porque una gráfica parezca similar: compara invariantes, tolerancias y coste.

**Medida de error:** para una aproximación (x_h) al valor de referencia (x_star), el error absoluto es (E_a=|x_h-x_star|). El relativo (E_r=E_a/|x_star|) requiere (x_star
eq0). Distinguimos error de redondeo, truncamiento, estimación estadística y error del propio modelo. No todos disminuyen cuando se reduce el paso o se aumenta el número de muestras.

## 0.3. Integradores, conservación y dinámica

Las prácticas del [Sistema Solar](../05_Sistema_Solar/) y del [Cohete](../08_Leccion_Cohete/) son dos laboratorios de ecuaciones diferenciales. Dado (dot y=f(t,y)), Euler explícito tiene orden global 1; Runge–Kutta clásico orden global 4 bajo hipótesis adecuadas de suavidad y estabilidad. En sistemas hamiltonianos es crucial distinguir orden local de preservación cualitativa a tiempos largos.

Para (dot x=v), (dot v=a(x)), el esquema de *velocity Verlet* es:

[x_{n+1}=x_n+v_nDelta t+	frac12 a(x_n)Delta t^2,]
[v_{n+1}=v_n+	frac12[a(x_n)+a(x_{n+1})]Delta t.]

En un problema conservativo compara energía (H), momento angular cuando exista esa simetría, error de trayectoria frente a una referencia y deriva al aumentar el tiempo. Un método simpléctico puede conservar mejor la estructura geométrica a largo plazo sin conservar exactamente el valor de la energía en cada paso.

**Actividad de cierre:** traza (E(Delta t)) en escala log-log para al menos tres pasos; estima la pendiente sin confundirla con una prueba de convergencia universal. Identifica una escala donde redondeo, estabilidad o condición inicial domina.

## 0.4. Aleatoriedad, Monte Carlo y física estadística

Un generador pseudoaleatorio produce secuencias deterministas a partir de una semilla. La semilla es condición de **repetibilidad**, no garantía de buena calidad estadística. La práctica [Monte Carlo–Ising](../06_Monte_Carlo_Ising/) utiliza una distribución de Boltzmann (p_eta(s)propto e^{-eta H(s)}), con (eta=1/(k_B T)).

Para el Ising clásico (H=-Jsum_{langle i,jangle}s_i s_j-hsum_i s_i), (s_iin{-1,+1}), una actualización simétrica de Metropolis admite un cambio con

[P_{mathrm{aceptar}}=min(1,e^{-etaDelta E}).]

El código debe explicar la política de contorno, el orden de barrido, el calentamiento, la medida de magnetización y la estimación del error. Las muestras de una cadena de Markov suelen estar autocorrelacionadas; no pueden tratarse indiscriminadamente como observaciones independientes.

Como prueba analítica mínima, para **dos espines** y (h=0):

[Z_2=2e^{eta J}+2e^{-eta J}=4cosh(eta J),qquad langle s_1s_2angle=	anh(eta J).]

Este resultado permite verificar un simulador pequeño con todos los microestados enumerados antes de intentar redes grandes. Para una estimación con (N) muestras y tiempo de autocorrelación integrado (	au_{mathrm{int}}=	frac12+sum_{tgeq1}ho(t)), se utiliza como orientación (N_{mathrm{eff}}simeq N/(2	au_{mathrm{int}})) cuando la estimación de (	au_{mathrm{int}}) es estable.

**Actividad de cierre:** compara la estimación Monte Carlo de (langle s_1s_2angle) con (	anh(eta J)) en dos temperaturas; informa semilla, número de barridos, calentamiento, incertidumbre y diferencias.

## 0.5. Schrödinger, operadores y matrices

La práctica [Schrödinger](../07_Leccion_Schrodinger/) es un laboratorio de algebra lineal, condiciones de contorno y evolución temporal. Para un Hamiltoniano hermítico (H=H^dagger) independiente del tiempo:

[ihbarpartial_t|psi(t)angle=H|psi(t)angle,qquad U(t)=e^{-iHt/hbar}.]

Como (U^dagger U=I), se conserva (|psi(t)|_2), además del producto interno entre estados evolucionados por el mismo operador. Una aproximación numérica puede violar esta propiedad por truncamiento o por un integrador inapropiado.

Para (H=-(hbar^2/2m)partial_x^2+V(x)), la diferencia centrada (partial_x^2psi(x_j)approx(psi_{j-1}-2psi_j+psi_{j+1})/Delta x^2) induce una matriz tridiagonal. Especifica el dominio, contornos y pesos de cuadratura antes de normalizar el vector discreto.

**Actividad de cierre:** calcula los dos primeros niveles de una caja 1D para varias resoluciones; verifica convergencia y conservación de norma durante una propagación. Escribe claramente qué cambia si los contornos son periódicos.

## 0.6. Cómo relacionar las prácticas

| Problema | Objeto común | Método | Testigo físico |
|---|---|---|---|
| Órbitas | Estado continuo (y(t)) | Integración EDO | Energía, momento angular, orden de error |
| Ising | Configuración discreta (s) | MCMC | Distribución de Boltzmann, correlaciones |
| Schrödinger | Vector complejo (psi) | Matrices y propagación | Norma, autovalores, dispersión |
| Grafos y redes | Vértices + aristas | Combinatoria/espectro | Componentes, simetrías, conectividad |
| Archivo digital | Fuentes + metadatos | Extracción y consulta | Derechos, procedencia, integridad |

Estas conexiones justifican las extensiones a [computación cuántica](CAPITULO_01_COMPUTACION_CUANTICA.md), [combinatoria algebraica](CAPITULO_02_COMBINATORIA_ALGEBRAICA.md), [materia condensada](CAPITULO_04_SISTEMAS_COMPLEJOS_MATERIA_CONDENSADA.md) y [Humanidades Digitales](CAPITULO_03_BIBLIOTECAS_HUMANIDADES_DIGITALES.md).

## 0.7. Ficha KRONE de una práctica

```yaml
KRONE_LEARNING_EXPERIMENT_V1:
  model: Hamiltoniano_o_EDO_con_unidades
  assumptions: [hipotesis_de_modelo, condiciones_de_contorno]
  observable: magnitud_y_estimador
  numeric_method: algoritmo_y_orden_o_sesgo
  code: ruta_repositorio_y_commit
  environment: Python_3_12_o_compilador_declarado
  parameters: valores_con_unidades
  random_seed: null_si_no_aplica
  numerical_errors: [discretizacion, precision, muestreo]
  replay: comando_y_salidas_minimas
  original_figure: codigo_y_parametros_de_generacion
  interpretation: afirmacion_delimitada
  provenance: fuente_y_regimen_de_reutilizacion
  assessment: resultado_e_interpretacion
```

El `assessment` evalúa tanto el resultado como la interpretación; una cifra correcta con explicación físicamente equivocada no acredita comprensión. La certificación docente sigue correspondiendo al profesorado, no a SIGIL ni a una herramienta generativa.

## 0.8. Evaluación final sugerida (no sustituye la guía docente oficial)

Entrega un experimento único que reúna al menos **dos** familias metodológicas del curso. Ejemplos: (i) integración determinista de un sistema y estimación Monte Carlo de la incertidumbre en un parámetro, (ii) comparar un espectro discreto con un límite continuo, o (iii) clasificar grafos de interacción e investigar la dependencia de sus correlaciones térmicas. Adjunta informe corto, código, entorno, tres pruebas y una figura cuya fuente pueda regenerarse.

**Cierre:** la informática aporta experimentos; las matemáticas estructuran sus límites; la física decide qué preguntas tienen sentido. **Método + parámetros + unidades + código + incertidumbre + interpretación + procedencia** es la forma verificable de un resultado.
