import unittest
from fibonacci import find_pisano_period, get_fibonacci_huge_naive, fib_n_modulo_m, last_digit_of_summed_fib_numbers


class LastDigitOfTheSumOfFibonacciNumbers(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(last_digit_of_summed_fib_numbers(3), 4)


class FibNModuloM(unittest.TestCase):
    def test_find_pisano_period(self):
        self.assertEqual(find_pisano_period(2), 3)
        self.assertEqual(find_pisano_period(3), 8)

    def test_large_numbers(self):
        self.assertEqual(fib_n_modulo_m(2816213588, 239), 151)

    def test_simple_case(self):
        self.expect_fib_n_modulo_matches(239, 1000)

    def expect_fib_n_modulo_matches(self, n, m):
        expected = get_fibonacci_huge_naive(n, m)
        actual = fib_n_modulo_m(n, m)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
