import unittest
import sys

def m2(n):
    return n / 2


def m3(n):
    return n / 3


def p1(n):
    return n - 1


operations = [m2, m3, p1]

def primitive_calculator(n):
    res = [n + 1] * n
    res[0] = 1
    sequence = [[1]]
    for i in range(1, n):
        current = i + 1
        prev_number_fewest_steps = sys.maxsize
        for fn in operations:
            val = fn(current)
            if val % 1 == 0:
                if (res[i] > res[int(val) - 1] + 1):
                    res[i] = res[int(val) - 1] + 1
                    prev_number_fewest_steps = int(val)
        sequence.append(sequence[prev_number_fewest_steps - 1] + [current])
    return sequence[n - 1]

class PrimitiveCalculator(unittest.TestCase):
    def test_against_5(self):
        self.assertEqual(primitive_calculator(5), [1, 2, 4, 5])

    def test_against_1(self):
        self.assertEqual(primitive_calculator(1), [1])
