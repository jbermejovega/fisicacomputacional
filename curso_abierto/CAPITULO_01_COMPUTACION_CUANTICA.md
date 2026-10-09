# Capítulo 1 — Introducción a la computación cuántica desde la física

**Edición abierta JJBV · curso de Física Computacional / UGR**

## 1.1. Una nueva representación de un sistema físico

En física clásica una variable discreta con dos estados toma valores en \(\{0,1\}\). Un qubit puro es un vector unitario de \(\mathbb C^2\), salvo fase global: \(|\psi\rangle=\alpha|0\rangle+\beta|1\rangle\) con \(|\alpha|^2+|\beta|^2=1\). Un registro de \(n\) qubits vive en \((\mathbb C^2)^{\otimes n}\), de dimensión \(2^n\). El vector de amplitudes no es una distribución clásica: contiene fases e interferencias.

Convenciones: \(|0\rangle=(1,0)^T\), \(|1\rangle=(0,1)^T\). Las compuertas de un qubit son matrices unitarias. Por ejemplo:

\[H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad X=\begin{pmatrix}0&1\\1&0\end{pmatrix}.\]

Verifica simbólicamente \(H^\dagger H=I\) y \(H^2=I\). Tras \(H|0\rangle\), ambos resultados computacionales ocurren con probabilidad \(1/2\); una medición elimina las coherencias de esa base si no se conserva el resultado y el estado postmedición.

## 1.2. Mediciones y estadística

Para un proyector \(P\), la regla de Born da \(p=\langle\psi|P|\psi\rangle\). En un experimento con \(N\) medidas independientes de una probabilidad \(p\), el error estándar de la frecuencia es aproximadamente \(\sqrt{p(1-p)/N}\). Las muestras de un simulador que devuelve \(p\) exactamente no son equivalentes a \(N\) disparos (*shots*) de un dispositivo físico.

**Ejercicio:** prepara en código la salida ideal de \(|+\rangle=H|0\rangle\), simula 100, 1.000 y 10.000 medidas con una semilla fija y compara con el error estándar binomial. Explica qué magnitud converge y qué hipótesis se necesitan.

## 1.3. Productos tensoriales, compuertas controladas y entrelazamiento

El estado \(|00\rangle\) es separable. Aplicando \(H\otimes I\) y luego CNOT (primer qubit de control) se obtiene \(|\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2\), que no puede factorizarse como \(|a\rangle\otimes|b\rangle\). Su matriz de densidad reducida es \(\rho_A=I/2\).

**Ejercicio simbólico:** construye el proyector \(|\Phi^+\rangle\langle\Phi^+|\), calcula por suma explícita la traza parcial de B y verifica su pureza \(\mathrm{tr}(\rho_A^2)=1/2\). Contrasta con un estado producto, cuya reducción pura tiene \(\mathrm{tr}(\rho_A^2)=1\).

## 1.4. Por qué cuesta simular circuitos

Un simulador de vector de estado utiliza (2^n) amplitudes complejas; por eso una descripción ingenua escala exponencialmente. Pero **no implica que todo circuito cuántico sea difícil de simular**: las simetrías, el formalismo estabilizador/Clifford, redes tensoriales y descomposiciones estructuradas cambian el problema efectivo. Una cota formal de recursos debe declarar familia de circuitos, precisión, representación y criterio de coste.

En el marco del proyecto SIGILBOOK/FoQaQML, una línea de investigación estudia la optimización de simulación clásica de circuitos dominados por Clifford mediante reducción de simetrías. Esa investigación es un resultado especializado y no reemplaza los fundamentos de este capítulo.

## 1.5. Qué debe demostrar una práctica

Una práctica reproducible entregará: puerta o Hamiltoniano expresados en matrices, estado inicial, orden de composición, convención de índices, base de medida, probabilidades esperadas, error de muestreo cuando aplique y comando de replay. Añade un contraejemplo mostrando por qué dos amplitudes con la misma probabilidad individual pueden producir interferencias distintas.

## Lecturas complementarias

John Watrous, *The Theory of Quantum Information* y sus materiales públicos de teoría de información cuántica: inspiración de estructura y rigor, **no texto reproducido aquí**. Para profundizar, comparar mediciones proyectivas, trazas parciales, canales cuánticos y nociones de complejidad. Este es un capítulo original introductorio; no pretende cubrir por sí solo todos los resultados de Watrous.

**Puente siguiente:** [combinatoria algebraica](CAPITULO_02_COMBINATORIA_ALGEBRAICA.md) para estudiar grafos/hipergrafos de interacción y [materia condensada](CAPITULO_04_SISTEMAS_COMPLEJOS_MATERIA_CONDENSADA.md) para interpretar redes y correlaciones.
