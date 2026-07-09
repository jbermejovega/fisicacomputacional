# Examen final - Fisica Computacional QQUAPP 2026

```yaml
examen:
  id: EXAMEN_FINAL_FISICA_COMPUTACIONAL_QQUAPP_2026
  repositorio: jbermejovega/fisicacomputacional
  tipo: final
  modalidad: individual
  entorno_recomendado: fisica-computacional
  regla_kqc: metodo + codigo + parametros + unidades + salida_reproducible
  total_obligatorio: 10.0
  voluntario_extra: 2.0
```

## Instrucciones generales

Entrega un archivo comprimido o repositorio con:

- un notebook o script por pregunta;
- un `README.md` breve con instrucciones de ejecucion;
- figuras generadas, si las hay;
- tablas o ficheros de datos generados, si los hay;
- una seccion de reproducibilidad con entorno, version de Python, paquetes usados, parametros y unidades.

Toda respuesta debe incluir:

```text
resultado fisico = metodo + codigo + parametros + unidades + salida reproducible
```

No se evalua solo que el codigo ejecute. Se evalua que el metodo sea correcto, que las unidades sean visibles, que los parametros esten justificados y que la salida pueda reproducirse.

## Condiciones tecnicas

Usa preferentemente el entorno del curso:

```bash
conda env create -f environment.yml
conda activate fisica-computacional
python tools/validate_course_kqc.py
```

Paquetes permitidos por defecto: `numpy`, `scipy`, `matplotlib`, `pandas`, `sympy`, `jupyterlab`, `pytest` y librerias de la biblioteca estandar de Python.

Si usas otro paquete, debes justificarlo y dejar una ruta alternativa razonable con los paquetes del entorno del curso.

## Rubrica global

```yaml
rubrica:
  metodo_fisico_y_numerico: 30
  implementacion_y_reproducibilidad: 25
  analisis_de_error_y_estabilidad: 20
  interpretacion_fisica: 15
  claridad_de_entrega: 10
```

Penalizaciones fuertes:

- resultado sin unidades;
- parametros ocultos;
- grafica sin ejes o leyenda cuando sea necesaria;
- codigo no ejecutable;
- no indicar el metodo numerico;
- cambiar varios parametros sin explicar el efecto;
- presentar una salida que no pueda regenerarse.

---

# Parte A - Preguntas obligatorias avanzadas

## Pregunta 1. Optimizacion HPC de un problema de N cuerpos simplificado

**Puntuacion:** 2.0 puntos.

Implementa y optimiza una simulacion bidimensional de `N` particulas con interaccion gravitatoria suavizada:

```text
F_ij = G m_i m_j (r_j - r_i) / (|r_j - r_i|^2 + eps^2)^(3/2)
```

Usa condiciones iniciales reproducibles con una semilla fija. Integra la dinamica durante un tiempo total `T` usando un integrador explicito que indiques y justifiques.

### Tareas

1. Implementa una version base clara, aunque no sea la mas rapida.
2. Implementa una version optimizada usando vectorizacion con `numpy` o una estrategia equivalente permitida por el entorno.
3. Mide el tiempo de ejecucion para al menos tres tamanos: por ejemplo `N = 100, 300, 600`.
4. Representa el escalado temporal observado y comparalo con la complejidad teorica esperada.
5. Analiza estabilidad numerica, conservacion aproximada de energia y efecto del parametro `eps`.

### Entrega minima

- codigo reproducible;
- tabla de tiempos;
- grafica de escalado;
- grafica de energia o error relativo;
- explicacion breve de cuellos de botella y decisiones de optimizacion.

### Criterios especificos

```yaml
criterios:
  formulacion_del_modelo: 0.35
  implementacion_base_correcta: 0.30
  optimizacion_reproducible: 0.45
  medida_de_rendimiento: 0.35
  estabilidad_y_error: 0.35
  interpretacion_hpc: 0.20
```

---

## Pregunta 2. Integracion de resultados numericos: validacion cruzada de metodos

**Puntuacion:** 2.0 puntos.

Estudia un oscilador no lineal amortiguado y forzado:

```text
x'' + gamma x' + omega_0^2 x + alpha x^3 = A cos(Omega t)
```

Convierte la ecuacion en un sistema de primer orden e integra el sistema con al menos dos metodos numericos distintos, por ejemplo:

- `scipy.integrate.solve_ivp` con dos tolerancias diferentes;
- un metodo propio de Runge-Kutta de orden 4;
- un metodo de Euler mejorado usado solo como referencia de baja precision.

### Tareas

1. Define un conjunto base de parametros con unidades o escalado adimensional claro.
2. Compara trayectorias, energia efectiva o amplitud estacionaria segun corresponda.
3. Construye una tabla que integre resultados de varios metodos y tolerancias.
4. Define un criterio de aceptacion de resultados: convergencia, estabilidad y consistencia fisica.
5. Discute que resultado final aceptarias como certificado y cual descartarias.

### Entrega minima

- notebook/script con los metodos usados;
- tabla comparativa de resultados;
- al menos una grafica de trayectoria o espacio de fases;
- seccion final titulada `Resultado certificado`.

### Criterios especificos

```yaml
criterios:
  reduccion_a_primer_orden: 0.25
  implementacion_de_metodos: 0.35
  integracion_de_tablas_y_graficas: 0.35
  validacion_cruzada: 0.45
  criterio_de_certificacion: 0.40
  claridad_y_reproducibilidad: 0.20
```

---

# Parte B - Temas obligatorios del curso

## Pregunta 3. Interpolacion, ajuste y estimacion de incertidumbre

**Puntuacion:** 1.5 puntos.

Se proporciona o se genera un conjunto de datos sintetico de una magnitud fisica `y(t)` con ruido gaussiano controlado.

### Tareas

1. Genera datos reproducibles con semilla fija o usa un fichero de datos incluido en la entrega.
2. Ajusta un modelo fisico razonable, por ejemplo decaimiento exponencial, movimiento amortiguado o ley de potencias.
3. Estima parametros e incertidumbres usando `scipy.optimize` o un metodo explicado.
4. Representa datos, ajuste y residuos.
5. Decide si el modelo es aceptable a partir de los residuos y de la escala del ruido.

### Salida esperada

```text
parametros ajustados + incertidumbre + unidades + grafica + comentario fisico
```

---

## Pregunta 4. Ecuaciones diferenciales ordinarias y control del error

**Puntuacion:** 1.5 puntos.

Resuelve numericamente un problema de mecanica o fisica matematica descrito por EDOs. Opciones validas:

- pendulo simple no lineal;
- tiro con rozamiento;
- circuito RLC;
- oscilaciones acopladas;
- crecimiento/relajacion con escala temporal fisica.

### Tareas

1. Especifica la ecuacion, variables, parametros y unidades.
2. Integra el sistema con al menos dos pasos temporales o tolerancias.
3. Compara contra una solucion analitica aproximada cuando exista, o contra una solucion de referencia numerica.
4. Estima el error y explica como cambia con el paso temporal o tolerancia.
5. Muestra una grafica fisicamente interpretable.

---

## Pregunta 5. Monte Carlo, estadistica numerica y reproducibilidad

**Puntuacion:** 1.5 puntos.

Usa un metodo Monte Carlo para estimar una cantidad fisica o matematica relevante. Ejemplos:

- estimacion de `pi` por muestreo;
- integral de una funcion con significado fisico;
- camino aleatorio y difusion;
- distribucion de velocidades o energia con muestreo aleatorio.

### Tareas

1. Fija y documenta la semilla aleatoria.
2. Estudia la convergencia con el numero de muestras.
3. Representa error estimado frente a numero de muestras.
4. Compara con un valor exacto o de referencia cuando exista.
5. Interpreta el resultado en terminos de incertidumbre estadistica.

---

## Pregunta 6. Transformadas, espectro y analisis de senales fisicas

**Puntuacion:** 1.5 puntos.

Analiza una senal fisica sintetica o realista compuesta por varias frecuencias, ruido y una escala temporal conocida.

### Tareas

1. Construye o carga una senal reproducible `s(t)`.
2. Calcula su transformada discreta de Fourier con `numpy.fft` o metodo equivalente.
3. Identifica frecuencias dominantes y amplitudes relativas.
4. Estudia el efecto de la duracion total, frecuencia de muestreo y ruido.
5. Presenta una grafica temporal y una grafica espectral con unidades correctas.

---

# Parte C - Preguntas voluntarias integradas

Estas preguntas permiten sumar hasta 2.0 puntos extra, sin superar la nota maxima oficial que establezca la asignatura. Estan pensadas para integrar ejercicios voluntarios en el examen final mediante una extension reproducible.

## Voluntaria 1. Paralelizacion conceptual y diseno de benchmark

**Puntuacion extra:** hasta 1.0 punto.

A partir de la Pregunta 1, disena una estrategia de paralelizacion para CPU multinucleo o GPU, aunque no la ejecutes si el entorno no lo permite.

### Tareas

1. Identifica que bucles o bloques son paralelizables.
2. Propone una estrategia con `multiprocessing`, `numba`, `mpi4py`, CUDA o vectorizacion por bloques.
3. Define que magnitudes medirias: tiempo total, speedup, eficiencia, memoria y error numerico.
4. Explica que resultado esperarias y que limitaciones tendria.
5. Incluye pseudocodigo o diagrama de flujo.

La respuesta debe dejar claro que no se confunde una propuesta HPC con una mejora no medida.

## Voluntaria 2. Integracion de resultados en informe cientifico reproducible

**Puntuacion extra:** hasta 1.0 punto.

A partir de cualquiera de las preguntas obligatorias, construye un mini-informe reproducible que integre datos, codigo, resultados y conclusion fisica.

### Tareas

1. Incluye una tabla resumen de parametros y unidades.
2. Incluye una tabla de resultados principales.
3. Incluye al menos dos figuras generadas por el codigo.
4. Incluye una seccion `Limitaciones`.
5. Incluye una seccion `Como reproducir` con comandos concretos.

Se valorara especialmente que el informe pueda ser entendido y reejecutado por otra persona sin pedir aclaraciones.

---

# Plantilla minima de entrega

```text
entrega/
  README.md
  pregunta_1_hpc_n_cuerpos.ipynb
  pregunta_2_integracion_resultados.ipynb
  pregunta_3_ajuste.ipynb
  pregunta_4_edo_error.ipynb
  pregunta_5_monte_carlo.ipynb
  pregunta_6_fourier.ipynb
  voluntaria_1_benchmark.md
  voluntaria_2_informe.md
  outputs/
    figuras/
    tablas/
```

## Plantilla de reproducibilidad por pregunta

```yaml
reproducibilidad:
  pregunta: numero
  archivo: ruta
  metodo: metodo numerico usado
  parametros: lista con valores y unidades
  entorno: fisica-computacional
  python: version usada
  paquetes: lista minima
  comando_reproduccion: comando o notebook
  salida: figura/tabla/valor generado
  estado: pass_or_error
```

## Cierre KQC

```text
Un resultado del examen es valido si y solo si:
metodo declarado
and codigo/path reproducible
and parametros visibles
and unidades visibles
and salida trazable
and interpretacion fisica coherente
```
