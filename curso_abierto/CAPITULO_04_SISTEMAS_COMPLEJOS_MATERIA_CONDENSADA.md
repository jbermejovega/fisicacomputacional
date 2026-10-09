# Capítulo 4 — Sistemas complejos, física estadística y materia condensada

**Curso abierto de Física Computacional · UGR · Jara Juana Bermejo Vega**

## 4.1. De la partícula a la red

Muchos fenómenos colectivos se describen mediante un conjunto V de sitios y un conjunto E de interacciones. El grafo puede representar una red cristalina, un circuito, una topología de comunicación o un conjunto de relaciones. Compartir la estructura de grafo no iguala las leyes físicas que actúan sobre ella.

Compara tres operadores distintos sobre una misma red: (i) Laplaciano L=D−A para difusión sobre un grafo, (ii) Hamiltoniano de Ising H=−J∑σᵢσⱼ para espines y (iii) Hamiltoniano de enlaces H=−tA+diag(εᵢ) para transporte de una partícula. Sus dominios, dimensiones y observables son diferentes.

## 4.2. Ising como sistema complejo

En el Ising ferromagnético, los grados de libertad individuales son simples pero sus correlaciones pueden organizar fases macroscópicas. A temperatura finita en una red bidimensional adecuada se observan comportamiento crítico y efectos de tamaño finito. En una cadena Ising 1D de alcance finito y sin campo no aparece una transición de fase ferromagnética a temperatura finita en el límite termodinámico.

**Práctica:** estudia un número creciente de sitios del problema `06_Monte_Carlo_Ising`; compara magnetización, energía, susceptibilidad estimada, histogramas y tiempo de autocorrelación. No infieras exponente crítico a partir de una sola dimensión de red o un único tamaño.

## 4.3. Propagación, bandas y localización

Para una partícula en una cadena con acoplamiento uniforme t y contorno periódico, el modelo tight-binding sin desorden tiene dispersión E(k)=−2t cos(k a), donde a es la distancia de red y k el número de onda. Con un potencial aleatorio εᵢ, pueden aparecer estados espacialmente localizados y transporte reducido; la naturaleza de la localización depende de dimensionalidad, simetría, correlaciones y distribución de desorden.

La razón de participación inversa de un vector normalizado es IPR(ψ)=∑ᵢ|ψᵢ|⁴. Vale 1 para un estado situado en un solo sitio y 1/N para amplitud uniforme en N sitios. Es una medida de extensión espacial, **no** una prueba suficiente de transición de fase ni de una movilidad crítica en cualquier sistema.

**Práctica:** genera el Hamiltoniano de una cadena de N sitios y calcula eigenvalores/eigenvectores con SciPy; contrasta N=8 y N=16; dibuja IPR frente al valor de desorden para varias realizaciones y estima una dispersión estadística. Declara condiciones de contorno y energía de referencia.

## 4.4. Redes, simetrías y combinatoria

Los grafos permiten contar componentes, ciclos y árboles generadores. La **teoría de representaciones de simetrías** puede reducir la dimensión de bloques de un operador y simplificar su diagonalización. Pero un simple automorfismo de grafo no implica automáticamente una simetría de cualquier Hamiltoniano definido sobre él: deben preservarse los pesos, campos y términos de interacción pertinentes.

Para comenzar, usa el [teorema matriz-árbol y funciones de Möbius](CAPITULO_02_COMBINATORIA_ALGEBRAICA.md). Una descomposición por simetría y un truncamiento numérico son operaciones distintas; ambas requieren testigos de precisión y dominio.

## 4.5. Puente con computación cuántica

Los qubits pueden usarse para representar espines, y las correlaciones multi-sitio forman parte de modelos de muchos cuerpos. Para dos qubits un operador unitario conserva norma y puede crear entrelazamiento; para muchos qubits la descripción completa crece como 2^N. Redes tensoriales, formalismos estabilizadores y métodos variacionales aprovechan estructuras, pero deben justificarse dentro de una familia concreta de estados y errores permitidos.

El trabajo de investigación sobre ventaja cuántica y métodos de simulación clásica relacionado con SIGILBOOK es **contexto científico**, no sustituto de la derivación pedagógica ni promesa de escalabilidad universal.

## 4.6. Proyecto final integrado

**Problema:** elegir un grafo G de al menos 6 vértices. Construir L, un Hamiltoniano Ising sobre sus aristas y un Hamiltoniano tight-binding usando la misma matriz A. Identificar claramente qué observables corresponden a cada teoría. Calcular un espectro, una estadística Monte Carlo y un diagrama original del grafo. Comparar sensibilidad a una perturbación de una arista.

Entrega un cuaderno o script con fuente, controles de error, semilla y unidades; explica por qué un resultado de una de las tres representaciones no se transfiere automáticamente a las otras. La interpretación es tan importante como los resultados computacionales.

**KRONE de cierre:** misma geometría de incidencia ≠ misma dinámica, operador o interpretación. La continuidad entre materias surge de interfaces matemáticas documentadas, no de colapsar teorías.
