import unittest
from calculadora import *

class TestCases (unittest.TestCase):
     """--------------------Pruebas numeros complejos--------------------"""
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
          
     """--------------------Pruebas vectores--------------------"""
          
     def test_adicion_vect (self):
          result = adicion_vect (([(3,2),(0,0),(5,-6)]), ([(1,0),(4,2),(0,1)]))
          self.assertEqual (result, ([(4, 2), (4, 2), (5, -5)]))
          
     def test_producto_vect (self):
          result = producto_vect (((3,2)), ([(1,0),(4,2),(0,1)]))
          self.assertEqual (result, ([(3, 2), (8, 14), (-2, 3)]))

     def test_sustracc_vect (self):
          result = sustracc_vect (([(3,2),(0,0),(5,-6)]), ([(1,0),(4,2),(0,1)]))
          self.assertEqual (result, ([(2, 2), (-4, -2), (5, -7)]))

     def test_inversa_vect (self):
          result = inversa_vect (([(3,2),(0,0),(5,-6)]))
          self.assertEqual (result, ([(-3, -2), (0, 0), (-5, 6)]))

     def test_conjugado_vect (self):
          result = conjugado_vect (([(3,2),(0,0),(5,-6)]))
          self.assertEqual (result, ([(3, -2), (0, 0), (5, 6)]))

     def test_norma_vect (self):
          result = norma_vect (([(3,2),(0,0),(5,-6)]))
          self.assertEqual (result, (11.415800951370644))

     def test_vectores_iguales (self):
          result = vectores_iguales (([(3,2),(0,0),(5,-6)]), ([(1,0),(4,2),(0,1)]))
          self.assertEqual (result, (False))

     def test_producto_interno_vect (self):
          result = producto_interno_vect (([(3,2),(0,0),(5,-6)]), ([(1,0),(4,2),(0,1)]))
          self.assertEqual (result, ((-3, 3)))

     def test_distancia_vecto (self):
          result = distancia_vecto (([(3,2),(0,0),(5,-6)]), ([(1,0),(4,2),(0,1)]))
          self.assertEqual (result, (102.0))

     def test_product_tensor (self):
          result = product_tensor (([(3,2),(0,0),(5,-6)]), ([(1,0),(4,2),(0,1)]))
          self.assertEqual (result, ([[(3, 2), (8, 14), (-2, 3)], [(0, 0), (0, 0), (0, 0)], [(5, -6), (32, -14), (6, 5)]]))
     """--------------------Pruebas matrices--------------------"""
     def test_ad_mat (self):
          result = ad_mat (([[(3,2),(0,0),(5,-6)],[(1,0),(4,2),(0,1)],[(4,-1),(0,0),(4,0)]]), ([[(5,0),(2,-1),(6,-4)],[(0,0),(4,5),(2,0)],[(7,-4),(2,7),(0,0)]]))
          self.assertEqual (result, [[(8, 2), (2, -1), (11, -10)], [(1, 0), (8, 7), (2, 1)], [(11, -5), (2, 7), (4, 0)]])

     def test_m_subtraction (self):
          result = m_subtraction (([[(3,2),(0,0),(5,-6)],[(1,0),(4,2),(0,1)],[(4,-1),(0,0),(4,0)]]), ([[(5,0),(2,-1),(6,-4)],[(0,0),(4,5),(2,0)],[(7,-4),(2,7),(0,0)]]))
          self.assertEqual (result, [[(-2, 2), (-2, 1), (-1, -2)], [(1, 0), (0, -3), (-2, 1)], [(-3, 3), (-2, -7), (4, 0)]])

if __name__ == '__main__':
    unittest.main()
