import unittest
from EXP import *
class TestCases (unittest.TestCase):
    def test_canics (self):
          result = canicas (([[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],[(0, 0), (1, 0), (0, 0), (0, 0), (0, 0), (1, 0)],[(0, 0), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0)],[(0, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)],[(1, 0), (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)]]), [[(6, 0), (2, 0), (1, 0), (5, 0), (3, 0), (10, 0)]], 1)
          self.assertEqual (result, [[(0, 0)], [(0, 0)], [(12, 0)], [(5, 0)], [(1, 0)], [(9, 0)]])
          
    def test_bullets (self):
          result = bullets ([[(0, 0), (1/6, 0), (5/6, 0)],[(1/3, 0), (1/2, 0), (1/6, 0)],[(2/3, 0), (1/3, 0), (0, 0)]], [[(1/6, 0), (1/6, 0), (2/3, 0)]], 1)
          self.assertEqual (result, [[(0.5833333333333334, 0.0)], [(0.25, 0.0)], [(0.16666666666666666, 0.0)]])
    def test_count_bullets (self):
          result = count_bullets ([[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],[(1/(2)**(1/2), 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],[(1/(2)**(1/2), 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],[(0, 0), (-1/(6)**(1/2), 1/(6)**(1/2)), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)],[(0, 0), (-1/(6)**(1/2), -1/(6)**(1/2)), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)],[(0, 0), (1/(6)**(1/2), -1/(6)**(1/2)), (-1/(6)**(1/2), 1/(6)**(1/2)), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0)],[(0, 0), (0, 0), (-1/(6)**(1/2), -1/(6)**(1/2)), (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)],[(0, 0), (0, 0), (1/(6)**(1/2), -1/(6)**(1/2)), (0, 0), (0, 0), (0, 0), (0, 0), (1, 0)]], 1)
          self.assertEqual (result, [[0, 0, 0, 0, 0, 0, 0, 0], [0.4999999999999999, 0, 0, 0, 0, 0, 0, 0], [0.4999999999999999, 0, 0, 0, 0, 0, 0, 0], [0, 0.3333333333333334, 0, 1, 0, 0, 0, 0], [0, 0.3333333333333334, 0, 0, 1, 0, 0, 0], [0, 0.3333333333333334, 0.3333333333333334, 0, 0, 1, 0, 0], [0, 0, 0.3333333333333334, 0, 0, 0, 1, 0], [0, 0, 0.3333333333333334, 0, 0, 0, 0, 1]])

if __name__ == '__main__':
    unittest.main()
