import unittest
from math_utils import es_par

class TestEsPar(unittest.TestCase):
    def test_4_es_par(self):
        self.assertTrue(es_par(4))
    
    def test_5_es_par(self):
        self.assertTrue(es_par(5))

    def test_menos5_es_par(self):
        self.assertTrue(es_par(-5))
    


if __name__ == "__main__":
    unittest.main()