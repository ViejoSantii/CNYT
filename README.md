# Calculadora de complejos

Este proyecto es acerca de las operaciones con complejos de ecuaciones, matrices y vectores.
### Introducción

Cada funcion lee tuplas "(a,b)", donde "a" representa la parte real y "b" representa la parte imaginaria.

------------

[readme](https://github.com/ViejoSantii/CNYT/upload/master "readme")

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

The second part is composed for addition, subtraction, product, scalar, traspouse, conjugate, adjoint, inverse, trace, identity, equals, unitary, hermitiania, action, inner product; on matrix.
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

Hay pruebas en el archivo "pruebas" donde se encuentra la funcion que verifica casos bases.

