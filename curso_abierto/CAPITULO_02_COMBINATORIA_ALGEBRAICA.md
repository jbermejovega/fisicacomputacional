# Capítulo 2 — Combinatoria algebraica para física computacional

**Texto y ejercicios originales · Jara Juana Bermejo Vega · edición abierta V1**

## Por qué es imprescindible

Una red de espines, un circuito cuántico, un sistema de transporte, una red neuronal y un grafo de citas son objetos distintos que comparten parte de una estructura combinatoria. Comprender esa estructura permite calcular observables, evitar enumeraciones innecesarias y distinguir simetrías reales de coincidencias visuales. Este módulo es una extensión breve de Física Computacional, no la reproducción de una asignatura de combinatoria.

## 2.1. Conjuntos parcialmente ordenados y retículos

Un conjunto parcialmente ordenado (poset) es un conjunto P con una relación reflexiva, antisimétrica y transitiva. El retículo booleano Bₙ es el conjunto de subconjuntos de {1,…,n}, ordenado por inclusión. En B₂:

```text
            {a,b}
           /     \
         {a}     {b}
           \     /
              ∅
```

El ínfimo es intersección, el supremo es unión. En un poset general puede no existir alguno de estos extremos para un par de elementos. Esto es importante para no llamar 'retículo' a cualquier grafo o DAG.

## 2.2. Álgebra de incidencia e inversión de Möbius

Para un poset localmente finito, la función de Möbius se define por μ(x,x)=1 y, si x<y, por ∑₍ₓ≤𝑧≤ᵧ₎ μ(x,z)=0. En Bₙ, la fórmula es **μ(S,T)=(-1)^(|T|-|S|)** si S⊆T.

Si g(x)=∑₍ᵧ≤ₓ₎ f(y), la inversión da f(x)=∑₍ᵧ≤ₓ₎ μ(y,x)g(y). Se puede usar para deshacer acumulaciones sobre subconjuntos (por ejemplo, contribuciones que se solapan en una enumeración de configuraciones).

**Práctica original:** enumera los cuatro elementos de B₂ y verifica que μ(∅,{a,b})=+1. Implementa la recurrencia de μ para otro poset pequeño y escribe un test para la inversión. El código de acompañamiento se encuentra en `codebooks/modelos_exactos.py`.

## 2.3. Laplaciano de grafo y teorema matriz-árbol

Para un grafo simple no dirigido G con matriz de adyacencia A y matriz diagonal de grados D, el Laplaciano es L=D−A. El teorema matriz-árbol de Kirchhoff afirma que cualquier cofactor principal de L (suprimir la misma fila y columna) cuenta el número de **árboles generadores**. Los grafos desconectados no tienen árboles generadores y el determinante correspondiente se anula.

Para el triángulo K₃: L tiene 2 en diagonal y −1 fuera de ella. Tras eliminar la tercera fila y columna queda [[2,−1],[−1,2]], con determinante **3**. Los tres árboles generadores se obtienen eliminando cualquiera de sus tres aristas.

**Conexión física:** en redes eléctricas, difusión y procesos gaussianos en grafos, el Laplaciano y sus autovalores describen conectividad y modos. La igualdad de cofactores con árboles generadores es exacta, pero no significa que el Laplaciano sea el Hamiltoniano correcto de todo sistema físico.

## 2.4. Polinomio cromático, Potts e Ising

El polinomio cromático P_G(q) cuenta coloraciones propias de los vértices con q colores. Para K₃, P_G(q)=q(q−1)(q−2). Su forma polinómica permite evaluaciones simbólicas y relaciones con la estructura del grafo.

El polinomio de Fortuin–Kasteleyn o representación de conglomerados aleatorios es

**Z_G(q,v) = ∑_{A⊆E(G)} q^{k(A)} v^{|A|}**,

donde k(A) cuenta componentes conexas del subgrafo generador con aristas A. Para el modelo Potts ferromagnético con q estados e interacción uniforme J, v=exp(βJ)−1. En el caso Ising con σ∈{−1,+1} y H=−J∑σᵢσⱼ (sin campo), el cambio de convención da

**Z_Ising = exp(−βJ|E|) · Z_G(2, exp(2βJ)−1).**

Esto no presupone que toda representación de Potts tenga dos estados; el paso q=2 y la relación entre los acoplamientos son esenciales.

**Práctica original:** calcula el polinomio cromático de un triángulo, el Laplaciano y los árboles generadores con SymPy. Después enumera los subconjuntos de aristas de un grafo de tres vértices y comprueba la expresión de Z_G(q,v), antes de intentar redes grandes.

## 2.5. Caminos sin intersección y determinantes

El lema de Lindström–Gessel–Viennot relaciona determinantes de matrices de conteo de caminos en un DAG con sumas **con signo** de familias de caminos no intersectantes. En determinadas configuraciones compatibles de fuentes y destinos la cancelación de signos permite un conteo no negativo. Es un ejemplo de por qué una identidad algebraica puede sustituir una enumeración exponencial, siempre que sus hipótesis se cumplan.

**Ejercicio:** construye un DAG pequeño de fuentes y sumideros, computa el número de caminos entre cada par, calcula el determinante y enumera las familias no intersectantes. Explica cuándo la interpretación del determinante requiere signos.

## 2.6. Referencias y alcance de la reutilización

Este capítulo se inspira en la cobertura temática de [MIT OCW 18.212 Algebraic Combinatorics (primavera de 2019)](https://ocw.mit.edu/courses/18-212-algebraic-combinatorics-spring-2019/), impartido por Alexander Postnikov, especialmente los bloques de **posets y retículos**, **teorema matriz-árbol** y **lema de Lindström–Gessel–Viennot**. Los materiales MIT OCW se distribuyen bajo condiciones propias (en el paquete consultado figura CC BY-NC-SA 4.0); **no se han copiado notas, soluciones, figuras ni diapositivas** a este curso. Los ejemplos y desarrollos presentes son nuevos y pueden seguir la licencia declarada para esta edición.

## Criterios de evaluación

Se califican simultáneamente corrección combinatoria, modelización física, código reproducible, declaración de hipótesis y justificación de cuándo una interpretación no es válida. Esta unidad enlaza directamente con [Ising](../06_Monte_Carlo_Ising/) y [sistemas complejos](CAPITULO_04_SISTEMAS_COMPLEJOS_MATERIA_CONDENSADA.md).
