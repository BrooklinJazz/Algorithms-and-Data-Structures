import unittest
import random
from greedy_algorithms import money_change, maximum_loot


class MoneyChange(unittest.TestCase):

    def test_simple_cases(self):
        self.assertEqual(money_change(2), 2)
        self.assertEqual(money_change(10), 1)
        self.assertEqual(money_change(30), 3)


class MaximumLoot(unittest.TestCase):

    def test_simple_cases(self):
        result = maximum_loot(
            [3, 50, 60, 20, 100, 50, 120, 30])
        self.assertEquals(result, 180.0000)


if __name__ == '__main__':
    unittest.main()
