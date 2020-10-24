import unittest
import random
from fibonacci import fibonacci_partial_sum, fibonacci_faster_partial_sum_naive, fibonacci_partial_sum_naive, find_pisano_period, get_fibonacci_huge_naive, fib_modulo, fib_n_modulo_m, find_periodic, fast_fib, fibonacci_sum_last_number_naive, fibonacci_sum_last_number


def random_int(maximum=100):
    return random.randint(0, maximum)


class LastDigitOfAPartialSumOfFibonacciNumbers(unittest.TestCase):
    constraint = 10 ** 18
    start = random.randint(50, 100)
    end = random.randint(start, 200)

    def test_simple_case(self):
        self.assertEqual(fibonacci_partial_sum(3, 7), 1)

    def test_larger_case(self):
        start = 3
        end = 100
        expected = fibonacci_partial_sum_naive(start, end)
        actual = fibonacci_partial_sum(start, end)
        self.assertEqual(expected, actual)

    def test_against_naive_fn(self):
        expected = fibonacci_partial_sum_naive(self.start, self.end)
        actual = fibonacci_partial_sum(self.start, self.end)
        self.assertEqual(expected, actual)

    def test_fast_naive(self):
        expected = fibonacci_partial_sum_naive(self.start, self.end)
        actual = fibonacci_faster_partial_sum_naive(self.start, self.end)
        self.assertEqual(expected, actual)


class LastDigitOfTheSumOfFibonacciNumbers(unittest.TestCase):
    constraint = 10 ** 14

    def test_simple_case(self):
        self.assertEqual(fibonacci_sum_last_number(3), 4)

    def test_against_naive_fn(self):
        n = random_int()
        expected = fibonacci_sum_last_number_naive(n)
        actual = fibonacci_sum_last_number(n)
        self.assertEqual(expected, actual)

    def test_large_numbers(self):
        fibonacci_sum_last_number(self.constraint)

    def test_find_periodic(self):
        self.assertEqual(3, find_periodic(fib_modulo(2)))
        self.assertEqual(8, find_periodic(fib_modulo(3)))


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
