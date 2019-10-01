from sys import stdin
import math
import unittest
def adicion(c1, c2):
     a1 = c1 [0]; a2 = c2 [0]
     b1 = c1 [1]; b2 = c2 [1]
     x = a1 + a2
     y = b1 + b2
     z = (x, y)
     return z
def producto(c1, c2):
     a1 = c1 [0]; a2 = c2 [0]
     b1 = c1 [1]; b2 = c2 [1]
     x = (a1 * a2) - (b1 * b2)
     y = (a1 * b2) + (a2 * b1)
     z = (x, y)
     return z

def sustraccion(c1, c2):
     a1 = c1 [0]; a2 = c2 [0]
     b1 = c1 [1]; b2 = c2 [1]
     x = a1 - a2
     y = b1 - b2
     z = (x, y)
     return z

def Mproducto (A, B):
    filasB = len(B)
    columnasA = len(A[0])
    if filasB == columnasA:
        filas = len(A)
        columnas = len(B[0])
        matriz = [[(0, 0)] * columnas for x in range(filas)]
        for i in range(0, filas):
            for j in range(0, columnas):
                for k in range(0, len(B)):
                    m = producto(A[i][k], B[k][j])
                    n = matriz[i][j]
                    matriz[i][j] = (m[0]+n[0], m[1]+n[1])
        return matriz
    else:
        print("La dimensión es incorrecta")
        return False

def Mtraspuesta (matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    return [[matriz[j][i] for j in range(filas)] for i in range(columnas)]




def canicas(m, v, N):
    '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]], 
       v = [(c1, c2), (c1, c2),...,(c1, c2)]
       N = int;
    (m ** N) * v = V;
    matriz, vector, int ---> vector'''
    mat_n = m
    for i in range (1, N-1):
        n = Mproducto (mat_n, m)
        mat_n = n
    return (Mproducto (mat_n, Mtraspuesta(v)))

def bullets(m, v, N):
    '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]], 
       v = [(c1, c2), (c1, c2),...,(c1, c2)]
       N = int;
    (m ** N) * v = V;
    matriz, vector, int ---> vector'''
    mat_n = m
    for i in range (1, N-1):
        n = Mproducto (mat_n, m)
        mat_n = n
    return (Mproducto (mat_n, Mtraspuesta(v)))
def count_bullets (m, N):
     '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]], v = [(c1, c2), (c1, c2),...,(c1, c2)] N = int; (m ** N) * v = V; matrix, vector, int ---> vector'''
          mat_n = m
          for i in range (1, N):
               n = m_product (mat_n, m)
               mat_n = n
          n = m
          for i in range (len (m)):
               for k in range (len (m [0])):
                    solve = (m [i][k][0]**2 + m [i][k][1]**2)
                    n [i][k] = solve
          return n
