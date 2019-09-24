# Calculadora de complejos

Este proyecto es acerca de las operaciones con complejos de ecuaciones, matrices y vectores.
### Introducción

Cada funcion lee tuplas "(a,b)", donde "a" representa la parte real y "b" representa la parte imaginaria.

## Ecuaciones con números complejos

La parte inicial esta compuesta por la adición, sustracción, división, producto, conjugado, modulo, conversión de cartesiano a polar y viceversa, con números complejos.

```
    C1 = (a1, b1); C2 = (a2, b2)

ADICION: C1 + C2 = (a1 + a2, b1 + b2)
SUSTRACCION: C1 - C2 = (a1 - a2, b1 - b2)
PRODUCTO: C1 + C2 = (a1a2 - b1b2, a1b2 + a2b1)
DIVISION: C1 / C2 = (a1, b1) / (a2, b2)
```

## Vectores con números complejos

La segunda parte esta compuesta por la adición, sustracción, producto, inversa, conjugado, norma, igualdad entre vectores, distancia entre vectores, producto interno, con vectores.

```
    v1 = [(c1, c2), (c1, c2),...,(c1, c2)] 
    v2 = [(c1, c2), (c1, c2),...,(c1, c2)]

ADICIÓN: (V1 + V2) [i] = V1 [i] + V2 [i]
SUSTRACCIÓN: (V1 - V2) [i] = V1 [i] - V2 [i]
PRODUCTO: (C · V)[j] = C × V[j]
INVERSA: (−V)[ j ] = −(V[ j ])
CONJUGADO: V [i] = V [-i]
NÓRMA: |V| = sqrt (x2 +y2 +z2)
VECTORES IGUALES: V1 == V2
DISTANCÍA: |V1 − V2| = sqrt⟨V1 − V2,V1 − V2⟩
PRODUCTO INTERNO: ⟨V1, V2⟩ = V† ⋆ V2
```
## Matrices con números complejos

La tercera parte esta compuesta por la adición, sustracción, escalar, traspuesta, conjugado, adjunta, inversa, identidad, igualdad de matrices, unitaria, hermitian, acción, producto interno, en matrices.

```
    m1 = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]] 
    m2 = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]

ADICIÓN: M1 + M2 = M1 [j, k] + M2 [j, k]
SUSTRACCIÓN: M1 - M2 = M1 [j, k] - M2 [j, k]
PRODUCTO: (M1 x M2)[j, k] = SUMATORY (h=0, n-1)(M1 [j, h] x B [h, k])
ESCALAR: C1 ∙ M = C ∙ M [j, k]
TRASPUESTA: M^T [j, k] = M [k, j]
CONJUGADO: M [j,k] = M [-j,-k]
ADJUNTA: M† [j, k] = M [k, j]
INVERSA: -M [i, j] = -(M [i, j])
IDENTIDAD: M [i, i] == (1, 0)
IGUALDAD DE MATRICES: M1 == M2
UNITARIA M† ∙ M
HERMITIAN:
ACCIÓN: M ∙ V
PRODUCTO INTERNO: Trace(A† ⋆ B)
```


## Casos de prueba

Hay pruebas en el archivo "pruebas" donde se encuentra la funcion que verifica casos bases. Solamente se corre el programa y automaticamente verifica todas las operaciones, dando como resultado el numero de pruebas probadas y todo este OK.

## Experimentos

#### Las canicas experimentan con coeficientes booleanos.
No solo nos interesan los estados del sistema, sino también la forma en que cambian los estados. La forma en que cambian, o la dinámica del sistema, puede representarse mediante un gráfico con bordes dirigidos. No permitimos un gráfico arbitrario. Más bien, insistimos en que cada vértice en el gráfico tiene exactamente un borde saliente. Este requisito coincidirá con nuestra demanda de que el sistema sea determinista. En otras palabras, cada canica debe moverse exactamente a un lugar. En inglés simple, esto indica que el número de canicas que alcanzarán el vértice i después de un paso de tiempo es la suma de todas las canicas que están en vértices con bordes que se conectan al vértice i.
Observe que las dos entradas superiores de Y son 0. Esto corresponde al hecho de que no hay flechas que vayan al vértice 0 o al vértice 1.

#### Experimentos de múltiples rendijas clásicas probabilísticas, con más de dos rendijas
En la mecánica cuántica, existe una indeterminación inherente en nuestro conocimiento de un estado físico. Además, los estados cambian con las leyes probabilísticas. Esto simplemente significa que las leyes que rigen la evolución de un sistema se dan al describir cómo la transición de los estados de uno a otro con cierta probabilidad.
Para capturar estos escenarios probabilísticos, modifiquemos lo que hicimos en
La última sección. En lugar de lidiar con un montón de canicas moviéndose, vamos a
trabajar con una sola canica. El estado del sistema nos dirá las probabilidades de
El mármol está en cada vértice. También debemos modificar la dinámica. En lugar de exactamente una flecha que sale de cada vértice, tendremos varias flechas disparadas de cada vértice con números reales entre 0 y 1 como pesos. Estos pesos describen la probabilidad de que nuestra canica se mueva de un vértice a otro con un solo clic. Las matrices de adyacencia para nuestros gráficos tendrán entradas reales entre 0 y 1 donde las sumas de las filas y las sumas de las columnas son todas 1. Dichas matrices se denominan doblemente estocásticas.
