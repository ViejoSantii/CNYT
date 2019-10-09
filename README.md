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

#### Experimento de múltiples rendijas cuánticas
Esta matriz no es unitaria. La razón por la que esta matriz no es unitaria es que no hemos colocado todas las flechas en nuestro gráfico. Hay muchas más formas posibles en que la persona puede viajar en una situación física de la vida real. En particular, el fotón podría viajar de derecha a izquierda. El diagrama y la matriz se volverían demasiado complicados si pusiéramos todas las transiciones. Simplemente estamos tratando de demostrar el fenómeno de la interferencia y podemos lograrlo incluso con una matriz que no sea del todo unitaria. La matriz de adyacencia, P (para "fotones").

#### Probabilidad ket
Decimos que el estado | ψ⟩ es una superposición de los estados básicos. | ψ⟩ representa la partícula como simultáneamente en todos {x0, x1,. . . , xn − 1} ubicaciones, o una combinación de todos los | xi⟩. Sin embargo, existen diferentes combinaciones posibles (al igual que en la receta para hornear un pastel de manzana, puede variar las proporciones de los ingredientes y obtener diferentes sabores). Los números complejos c0, c1, ..., cn − 1 nos dicen con precisión en qué superposición se encuentra actualmente nuestra partícula. La norma al cuadrado del número complejo ci dividido por la norma al cuadrado de | ψ⟩ nos dirá la probabilidad de que , después de observar la partícula, la detectaremos en el punto xi. Supongamos que la partícula solo puede estar en los cuatro puntos {x0, x1, x2, x3}. Por lo tanto, nos preocupa el espacio de estado C4. Calcularemos la probabilidad de que nuestra partícula se pueda encontrar en la posición x2.

#### Amplitud ket
La amplitud de transición entre dos estados puede ser cero. De hecho, eso sucede precisamente cuando los dos estados son ortogonales entre sí. Este simple hecho sugiere el contenido físico de la ortogonalidad: los estados ortogonales están lo más separados posible. Podemos pensar en ellas como alternativas mutuamente excluyentes: por ejemplo, un electrón puede estar en una superposición arbitraria de giro hacia arriba y hacia abajo, pero después de medirlo en la dirección z, siempre estará hacia arriba o hacia abajo, nunca hacia arriba y hacia abajo. abajo. Si nuestro electrón ya estaba en el estado ascendente antes de la medición de la dirección z, nunca pasará al estado inactivo como resultado de la medición.

#### Valor promedio
Si el conmutador de dos operadores hermitianos es cero, o equivalente, los dos operadores conmutan, no hay dificultad en asignar su producto (en cualquier orden) como el equivalente matemático del producto físico de sus observables asociados. Pero, ¿qué pasa con los otros casos, cuando los dos operadores no conmutan? El principio de incertidumbre de Heisenberg, que vamos a encontrar al final de esta sección, proporcionará una respuesta.
Existe otro aspecto más de la asociación entre los observables y los operadores hermitianos que pueden proporcionar una visión física sustancial: sabemos por el Capítulo 2 que los operadores hermitianos son precisamente aquellos operadores que se comportan bien con respecto al producto interno.

#### Varianza
Ahora podemos ver que si λ1 y λ2 están muy cerca de μ, el término en la ecuación estará cerca de cero. Por el contrario, si cualquiera de los dos valores propios está lejos de μ (no es importante ya sea por encima o por debajo, porque estamos tomando cuadrados), la varianza será un gran número real. Conclusión: la varianza nos informa sobre la propagación de los valores propios alrededor de su media.
Nuestro lector aún puede estar un poco insatisfecho después de este ejemplo: después de todo, lo que muestra es que la definición de varianza dada anteriormente funciona como debería en el caso de las matrices diagonales. En realidad, es un hecho conocido que todas las matrices hermitianas pueden ser des- diagonalizadas cambiando a una base de vectores propios, por lo que el ejemplo es lo suficientemente completo como para legitimar nuestra definición.

#### Estados propios
¿Cuál es la probabilidad de que un estado de inicio normalizado | ψ⟩ pase a un vector propio específico, digamos, | e⟩? Debemos volver a lo que dijimos en la Sección 4.1: la probabilidad de la transición al vector propio viene dada por el cuadrado del producto interno de los dos estados: | ⟨e | ψ⟩ | 2. Esta expresión tiene un significado simple: es la proyección de | ψ⟩ a lo largo de | e⟩.
