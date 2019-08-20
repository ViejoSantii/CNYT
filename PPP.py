from sys import stdin
import math
import unittest

"""Operaciones con complejos"""

def adicion (c1, c2):
     a1 = c1 [0]; a2 = c2 [0]
     b1 = c1 [1]; b2 = c2 [1]
     x = a1 + a2
     y = b1 + b2
     z = (x, y)
     return z

def producto (c1, c2):
     a1 = c1 [0]; a2 = c2 [0]
     b1 = c1 [1]; b2 = c2 [1]
     x = (a1 * a2) - (b1 * b2)
     y = (a1 * b2) + (a2 * b1)
     z = (x, y)
     return z

def sustraccion (c1, c2):
     a1 = c1 [0]; a2 = c2 [0]
     b1 = c1 [1]; b2 = c2 [1]
     x = a1 - a2
     y = b1 - b2
     z = (x, y)
     return z

def division (c1, c2):
     a1 = c1 [0]; a2 = c2 [0]
     b1 = c1 [1]; b2 = c2 [1]
     x = ((a1 * a2) + (b1 * b2)) / ((a2 ** 2) + (b2 ** 2))
     y = ((a2 * b1) - (a1 * b2)) / ((a2 ** 2) + (b2 ** 2))
     z = (x, y)
     return z

def modulo (c):
     x = ((c[0] ** 2) + (c[1] ** 2)) ** (1/2)
     return x

def conjugado (c):
     x = c[0]
     y = -c[1]
     z = (x, y)
     return z

def cart_a_pol (c):
     p = ((c[0] ** 2) + (c[1] ** 2)) ** (1/2)
     g = math.atan((c[1]) / (c[0]))
     z = (p, g)
     return z

def pol_a_cart (c):
     p = c[0]; g = c[1]
     a = p * (math.cos (g))
     b = p * (math.sin (g))
     z = (a, b)
     return z

def inversa (c):
     x = -c[0]
     y = -c[1]
     z = (x, y)
     return z

class TestCases (unittest.TestCase):
     def test_adicion (self):
          result = adicion ((2, 5), (3, 3))
          self.assertEqual (result, (5, 8))

     def test_producto (self):
          result = producto ((2, 5), (3, 3))
          self.assertEqual (result, (-9, 21))

     def test_sustraccion (self):
          result = sustraccion ((2, 5), (3, 3))
          self.assertEqual (result, (-1, 2))

     def test_division (self):
          result = division ((2, 5), (3, 3))
          self.assertEqual (result, (1.1666666666666667, 0.5))

     def test_modulo (self):
          result = modulo ((2, 5))
          self.assertEqual (result, (5.385164807134504))

     def test_conjugado (self):
          result = conjugado ((2, 5))
          self.assertEqual (result, ((2, -5)))

     def test_cart_a_pol (self):
          result = cart_a_pol ((2, 5))
          self.assertEqual (result, (5.385164807134504, 1.1902899496825317))

     def test_pol_a_cart (self):
          result = pol_a_cart ((2, 5))
          self.assertEqual (result, (0.5673243709264525, -1.917848549326277))

     def test_inversa (self):
          result = inversa ((2, 5))
          self.assertEqual (result, ((-2, -5)))

if __name__ == '__main__':
    unittest.main()
