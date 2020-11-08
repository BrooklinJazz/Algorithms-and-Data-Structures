import math
import unittest

denominations = [1, 3, 4]
cache = {}


def money_change(coins=denominations, amount=0):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if c <= i:
                dp[i] = min(dp[i], dp[i - c] + 1)
    return -1 if dp[amount] > amount else dp[amount]


class MoneyChange(unittest.TestCase):
    def test_against_2(self):
        self.assertEqual(money_change(denominations, 2), 2)

    def test_against_34(self):
        self.assertEqual(money_change(denominations, 34), 9)
