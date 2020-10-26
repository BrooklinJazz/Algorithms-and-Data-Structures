import unittest
import random
from divide_and_conquer import binary_search


class DivideAndConquer(unittest.TestCase):

    def binary_search(self):
        elements = [1, 5, 8, 12, 13]
        search_input = [5, 8, 1, 23, 1, 11]
        self.assertEqual(binary_search(
            elements, search_input), [2, 0, -1, 0, -1])
