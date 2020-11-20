import unittest

method_under_test = formingMagicSquare


class FormMagicSquares(unittest.TestCase):
    def test_1_change(self):
        s = [[4, 9, 1], [3, 5, 7], [8, 1, 5]]
        self.assertEqual(formingMagicSquare(s))
        # test
