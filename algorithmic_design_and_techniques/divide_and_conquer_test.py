import unittest
import random
from divide_and_conquer import binary_search


class DivideAndConquer(unittest.TestCase):

    def binary_search(self):
        elements = [1, 5, 8, 12, 13]
        search_input = 12
        self.assertEqual(binary_search(elements, search_input), 3)
