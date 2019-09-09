from sys import stdin
import math
"""--------------------Operaciones con complejos--------------------"""

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

def division(c1, c2):
     a1 = c1 [0]; a2 = c2 [0]
     b1 = c1 [1]; b2 = c2 [1]
     x = ((a1 * a2) + (b1 * b2)) / ((a2 ** 2) + (b2 ** 2))
     y = ((a2 * b1) - (a1 * b2)) / ((a2 ** 2) + (b2 ** 2))
     z = (x, y)
     return z

def modulo(c):
     x = ((c[0] ** 2) + (c[1] ** 2)) ** (1/2)
     return x

def conjugado(c):
     x = c[0]
     y = -c[1]
     z = (x, y)
     return z

def cart_a_pol(c):
     p = ((c[0] ** 2) + (c[1] ** 2)) ** (1/2)
     g = math.atan((c[1]) / (c[0]))
     z = (p, g)
     return z

def pol_a_cart(c):
     p = c[0]; g = c[1]
     a = p * (math.cos (g))
     b = p * (math.sin (g))
     z = (a, b)
     return z

def inversa(c):
     x = -c[0]
     y = -c[1]
     z = (x, y)
     return z

     """--------------------Operaciones vectores con complejos--------------------"""
def adicion_vect(v1, v2):
    '''v1 = [(c1, c2), (c1, c2),...,(c1, c2)] +
       v2 = [(c1, c2), (c1, c2),...,(c1, c2)] = v = [(c1, c2), (c1, c2),...,(c1, c2)]'''
    par = []
    for i in range (len (v1)):
        for j in range (len (v2)):
            if len (v1) != len (v2): print ('No es posible por dimensiones')
            else: a = adicion (v1[i], v2[i])
        par.append (a)
    return (par)

def producto_vect(c, v):
    '''c = (a1, b1) x v = [(c1, c2), (c1, c2),...,(c1, c2)]
       tupla x matriz ---> matriz'''
    pr = []
    for i in range (len (v)):
        pr.append(producto (c, v [i]))
    return (pr)

def sustracc_vect(v1, v2):
    '''v1 = [(c1, c2), (c1, c2),...,(c1, c2)] -
       v2 = [(c1, c2), (c1, c2),...,(c1, c2)] = v = [(c1, c2), (c1, c2),...,(c1, c2)]'''
    par = []
    for i in range (len (v1)):
        for j in range (len (v2)):
            if len (v1) != len (v2): print ('No es posible por dimensiones')
            else: a = sustraccion (v1[i], v2[i])
        par.append (a)
    return (par)

def inversa_vect(v):
     '''v = [(c1, c2), (c1, c2),...,(c1, c2)]
        vector ---> vector'''
     inv = []
     for i in range (len (v)):
          inv.append (inversa (v[i]))
     return inv

def conjugado_vect(v):
     '''v = [(c1, c2), (c1, c2),...,(c1, c2)]
        vector ---> vector'''
     con = []
     for i in range (len (v)):
          con.append (conjugado (v[i]))
     return con

def norma_vect (v):
     '''v = [(c1, c2), (c1, c2),...,(c1, c2)]
        vector ---> tupla'''
     c = 0
     for i in range (len (v)):
          c += (modulo (v[i]))
     return c

def vectores_iguales(v1, v2):
     '''v1 = [(c1, c2), (c1, c2),...,(c1, c2)];
        v2 = [(c1, c2), (c1, c2),...,(c1, c2)]
        vector, vector ---> booleano'''
     for i in range (len (v1)):
          if v1[i] == v2[i]:
               return True
          else: return False

def producto_interno_vect(v1, v2):
     '''vector, vector ---> tupla'''
     if len (v1) != len (v2):
          print ('No es posible por dimension')
     else:
          prod = (0, 0)
          conj = conjugado_vect (v1)
          for i in range (len (v1)):
               prod = adicion (prod, producto(conj[i], v2 [i]))
          return prod
        
def distancia_vecto(v1, v2):
     '''vector, vector ---> real'''
     solve = adicion_vect (v1, inversa_vect (v2))
     return modulo (producto_interno_vect (solve, solve))
          
def product_tensor(v1, v2):
     for i in range (len (v1)):
          product_tensor = []
          for j in range (len (v2)):
               product_tensor.append (producto (v1 [i], v2 [j]))
          v1 [i] = product_tensor
     return v1

     """--------------------Operaciones matrices con complejos--------------------"""

def adicion_matrices (m1, m2):
    '''m1 = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]] +
       m2 = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]] = M = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
       matriz, matriz ---> matriz'''
    ad = []
    for i in range (len (m1)):
        par = []
        for j in range (len(m2)):
            if len (m1 [i]) != len (m2 [i]):
                print ('No es posible por dimensiones')
            else:
                a = adicion (m1 [i][j], m2 [i][j])
                par.append (a)
        ad.append (par)
    return (ad)

def sustraccion_matrices (m1, m2):
    '''m1 = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]] -
       m2 = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]] = M = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
       matriz, matriz ---> matriz'''
    su = []
    for i in range (len (m1)):
        par = []
        for j in range (len(m2)):
            if len (m1 [i]) != len (m2 [i]):
                print ('No es posible por dimensiones')
            else:
                a = sustraccion (m1 [i][j], m2 [i][j])
                par.append (a)
        su.append (par)
    return (su)
def producto_matrices (m1, m2):
    '''m1 = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]] x
       m2 = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]] = M = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
       matriz, matriz ---> matriz'''
    if len (m1 [0]) == len (m2):
         pro = []
         for k in range (len (m1 [0])):
              res=[]
              for j in range (len (m2)):
                   add = (0,0)
                   for l in range (len (m2 [0])):
                        add = adicion (producto(m1[l][k],m2 [j][l] ), add)
                   res.append(add)
              pro.append(res)
         return pro

def escalar_matrices (c, m):
    '''c = (a, b) x
       m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]] =
       M = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
       tupla, matriz ---> matriz'''
    pro = []
    for i in range (len (m)):
         for j in range (len (m[0])):
              pro.append (producto (m [i][j]), c)
    return pro

def traspuesta_matrices (m):
     '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
        matriz ---> matriz'''
     mat = []
     for i in range (len (m[0])):
          line = []
          for j in range (len (m)):
               line.append (m[j][i])
          mat.append (line)
     return mat

def conjugado_matrices (m):
     '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
        matriz ---> matriz'''
     mat = []
     for i in range (len (m)):
          line = []
          for j in range (len (m [0])):
               line.append (conjugado (m[i][j]))
          mat.append (line)
     return mat

def adjunta_matrices (m):
     '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
        matriz ---> matriz'''
     return conjugado_matrices (traspuesta_matrices (m))

def inversa_matrices (m):
     '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
        matriz ---> matriz'''
     mat = []
     for i in range (len (m)):
          inv = []
          for j in range (len (m [0])):
               inv.append (conjugado (m[i][j]))
          mat.append (inv)
     return mat      

def traza_matrices (m):
     '''matriz ---> tupla'''
     b = (0, 0)
     for i in range (len (m)):
          b = adicion (b, m [i][i])
     return (b)

def producto_interno_matrices (m1, m2):
     '''matriz, matriz ---> tupla'''
     m = producto_matrices (adjunta_matrices (m1), m2)
     return traza_matrices (m)

def accion_matriz_vector (m, v):
     '''matriz, vector ---> tupla'''
     if len (m[0]) != len (v):
          print ('No es posible por las dimensiones vector-matriz')
     else:
          ac = (0, 0)
          for i in range (len (v)):
               for j in range (len (m[0])):
                    ac = adicion (ac, product (m[i][j], v[j]))
          return ac
   
def iguales_matrices(m1, m2):
     '''matriz, matriz ---> booleano'''
     if m1 == m2 : return True
     else: return False
                 
def hermitian_matrices (m):
     '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
        matriz ---> booleano'''
     if len (m) != len (m[0]):
          print ('Matriz no cuadrada')
     else:
          adj = adjunta_matrices (m)
     return iguales_matrices (adj, m)

def identidad_matrices (m):
     '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
        matriz ---> booleano'''
     for i in range (len (m)):
          for j in range (len (m [0])):
               if m [i][i] == (1, 0): return True
               else: return False
               
def unitaria_matrices (m):
     '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
        matriz ---> booleano'''
     if len (m) != len (m[0]):
          print ('Matriz no es cuadrada')
     else:
          mat_adj = producto_matrices (m, adjunta_matrices (m))
     return identidad_matrices (mat_adj)
