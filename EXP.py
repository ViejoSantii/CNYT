from sys import stdin
import math
import unittest
from numpy import linalg as operation
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

def Mproducto(A, B):
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

def Mtraspuesta(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    return [[matriz[j][i] for j in range(filas)] for i in range(columnas)]

def norma_vect(v):
     '''v = [(c1, c2), (c1, c2),...,(c1, c2)]
     vector ---> tupla'''
     r = 0
     t = 0
     for i in range (len (v)):
          r += (v[i][0]**2)
          t += (v[i][1]**2)
     return (r+t)**0.5

def conjugado(c):
     '''c ---> c
     tupla ---> tupla'''
     x = c[0]
     y = -c[1]
     z = (x, y)
     return z

def conjugado_vect(v):
     '''v = [(c1, c2), (c1, c2),...,(c1, c2)]
     vector ---> vector'''
     con = []
     for i in range (len (v)):
          con.append (conjugado (v[i]))
     return con

def prod_intern(v1, v2):
     '''vector, vector ---> tupla'''
     if len (v1) != len (v2):
          print ('No es posible por dimension de los vectores')
     else:
          prod = (0, 0)
          for i in range (len (v1)):
               prod = adicion(prod, producto(v1[i], v2 [i]))
          return prod

def prod_vect(c, v):
    '''c = (a1, b1) x v = [(c1, c2), (c1, c2),...,(c1, c2)]
    tupla x matriz ---> matriz'''
    pr = []
    for i in range (len (v)):
        pr.append(producto (c, v [i]))
    return (pr)

def Mhermitiana(m):
     '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
     matriz ---> booleano'''
     if len (m) != len (m[0]):
          print ('Matriz no cuadrada')
     else:
          adj = Madjunta (m)
     return Mequal (adj, m)

def Mconjugado(m):
     '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
     matrix ---> matrix'''
     mat = []
     for i in range (len (m)):
          line = []
          for j in range (len (m [0])):
               line.append (conjugado(m[i][j]))
          mat.append (line)
     return mat

def Midentidad(n):
     m = [[(0, 0) for i in range (n)]for j in range (n)]
     for i in range (n):
          m [i][i] = (1, 0)
     return m

def Madjunta(m):
     '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
     matriz ---> matriz'''
     return Mconjugado(Mtraspuesta (m))

def Mequal(m1, m2):
     '''matriz, matriz ---> booleano'''
     if m1 == m2 : return True
     else: return False

def Mescala(c, m):
    '''c = (a, b) x
    m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]] =
    M = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
    tupla, matriz ---> matriz'''
    pro = []
    for i in range (len (m)):
         a = []
         for j in range (len (m[0])):
              a.append (producto (m [i][j], c))
         pro.append(a)
    return pro

def Msustraccion(m1, m2):
    '''m1 = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]] -
    m2 = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]] =
    SM = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
    matriz, matriz ---> matriz'''
    su = []
    for i in range (len (m1)):
        par = []
        for j in range (len(m2)):
            if len (m1 [i]) != len (m2 [i]):
                print ('No es posible por dimensiones de las matrices')
            else:
                a = sustraccion(m1 [i][j], m2 [i][j])
                par.append (a)
        su.append (par)
    return (su)

def modulo(c):
    '''|c| = |a + bi| -------> ((a)**2+(b)**2)**0.5'''
    a, b = c[0],c[1]
    return ((a)**2+(b)**2)**0.5




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
     '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]],
        v = [(c1, c2), (c1, c2),...,(c1, c2)]
        N = int; (m ** N) * v = V;
        matriz, vector, int ---> vector'''
     mat_n = m
     for i in range (1, N):
          n = Mproduct (mat_n, m)
          mat_n = n
     n = m
     for i in range (len (m)):
          for k in range (len (m [0])):
               solve = (m [i][k][0]**2 + m [i][k][1]**2)
               n [i][k] = solve
     return n

def probabilidadket(h, ket):
     '''h = indice,
        ket = vector (ket)'''
     result = norma_vect(ket)
     r = abs (sum (producto (ket[h], ket [h])))
     ans = r / (result ** 2)
     return ans 

def amplitudket (n1, n2, k1, k2):
     '''k1, k2 ---> vector'''
     k3 = conjugado_vect(k2)
     r1 = prod_vect(n1, k1)
     r2 = prod_vect(n2, k3)
     return prod_intern(r1, r2)

def valor_prom(ket, m):
     kat = []
     for i in range (len (ket)):
          kat.append([ket [i]])
     r = Mproducto(m, kat)
     r = Mconjugado(r)
     y = []
     l = []
     for i in r:
          for j in i:
               y.append (j)
     return prod_intern(y, ket)

def varianza(m, k):
     '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]],
     ket = vector (ket),
     m, k ---> tupla'''
     if Mhermitiana (m):
          n = len (m)
          mat = Mescala((valor_prom (k, m)), (Midentidad (n)))
          u = Msustraccion(m,  mat)
          sol = Mproducto(u, u)
          res = 0
          for i in range (len (k)):
               a = modulo(k [i])**2
               res += a * sol [i][i][0]
     return res

def vals_props(observable):
    aux = []
    for i in range(len(observable)):
        z = []
        for j in range(len(observable[0])):
            a = observable[i][j][0]
            b = observable[i][j][1]
            b = eval(str(b)+'j')
            z.append(a+b)
        aux.append(z)
    valores,vectores = operation.eigh(aux)
    rta = []
    for i in valores:
        rta.append(i)
    return rta

def vect_prop(observable):
    aux = []
    for i in range(len(observable)):
        z = []
        for j in range(len(observable[0])):
            a = observable[i][j][0]
            b = observable[i][j][1]
            b = eval(str(b)+'j')
            z.append(a+b)
        aux.append(z)
    valores,vectores = operation.eigh(aux)
    rta = []
    for i in vectores:
        w = []
        for j in i:
            aux = str(j)
            b = aux.index('j')
            a = b
            for i in range(len(aux)):
                if aux[::-1][i] == '-' or aux[::-1][i] == '+':
                    a = i
                    break
            try:
                a = len(aux)-a
                tupla = (float(aux[1:a-1]),float(aux[a:b]))
                w.append(tupla)
            except ValueError:
                tupla = (0,float(aux[:b]))
                w.append(tupla)
        rta.append(w)
    return rta

def transitor_probabilidad(observable,estado):
    propios = vect_prop(observable)
    valores = vals_prop(observable)
    aux = []
    for i in range(len(estado)):
        aux.append([estado[i]])
    au = Mproducto (observable,aux)
    aux = []
    for i in au:
        for j in i:
            aux.append(j)
    pn = []
    for i in aux:
        pn.append(modulo(i)**2)
    ans = 0
    for i in range(len(valores)):
        ans += valores[i]*pn[i]
    return ans

def sistema(n,M,estado):
    estado = [estado]
    for i in range(n):
        estado = Mproducto(estado,M)
    return estado[0]
