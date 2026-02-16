import unittest
from math_utils import es_multiplo

class Testesmultiplo(unittest.TestCase):
    def es_multiplo_6_2(self):
        self.assertTrue(es_multiplo(6,2))

    def es_multiplo_menos6_2(self):
        self.assertTrue(es_multiplo(-6,2))

    def es_multiplo_0_3(self):
        self.assertTrue(es_multiplo(0,3))

    def es_multiplo_5_3(self):
        self.assertTrue(es_multiplo(5,3))


if __name__ == "__main__":
    unittest.main()