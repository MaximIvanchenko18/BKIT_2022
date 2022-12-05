import types
from fibonachi_func import fibonachi
import unittest


class FibonachiTestCase(unittest.TestCase):
    def test_n_is_not_positive(self):
        n = 0
        self.assertEqual([elem for elem in fibonachi(n)], [])
        n = -5
        self.assertEqual([elem for elem in fibonachi(n)], [])

    def test_n_is_one(self):
        n = 1
        self.assertEqual([elem for elem in fibonachi(n)], [e for e in [0]])

    def test_n_is_two(self):
        n = 2
        self.assertEqual([elem for elem in fibonachi(n)], [e for e in [0, 1]])

    def test_n_is_some(self):
        n = 13
        self.assertEqual([elem for elem in fibonachi(n)], [e for e in [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]])

    def test_lazy_calculations(self):
        for n in -5, 0, 1, 2, 13:
            self.assertEqual(type(fibonachi(n)), types.GeneratorType)


if __name__ == '__main__':
    unittest.main()
