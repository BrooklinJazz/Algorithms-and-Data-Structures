# Uses python3
from math import sqrt
from functools import lru_cache


@lru_cache(100)
def memoized_fib(n):
    if n < 2:
        return n
    else:
        return memoized_fib(n-1) + memoized_fib(n-2)


def table_fib(n):
    if n < 2:
        return n
    table = [-1] * (n+1)
    table[0] = 0
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    return table[n]


def iterative_fib(n):
    if n <= 1:
        return n
    previous, current = (0, 1)
    for i in range(2, n):
        previous, current = (current, previous + current)
    return current


def golden_fib(n):
    root_five = sqrt(5)
    phi = (root_five + 1) / 2
    return round((phi ** n) / root_five)


def matrix_exponentiation_fib(N):
    if N == 0:
        return (0, 1)
    half_N, is_N_odd = divmod(N, 2)
    f_n, f_n_plus_1 = matrix_exponentiation_fib(half_N)
    f_n_squared = f_n * f_n
    f_n_plus_1_squared = f_n_plus_1 * f_n_plus_1
    f_2n = 2 * f_n * f_n_plus_1 - f_n_squared
    f_2n_plus_1 = f_n_squared + f_n_plus_1_squared
    value = 0
    if is_N_odd:
        value = (f_2n_plus_1, f_2n + f_2n_plus_1)
    else:
        value = (f_2n, f_2n_plus_1)
    return value


def matrix_exponentiation_fib2(n):
    f_n, f_n_plus_1 = 0, 1
    for i in range(n.bit_length() - 1, -1, -1):
        f_n_squared = f_n * f_n
        f_n_plus_1_squared = f_n_plus_1 * f_n_plus_1
        f_2n = 2 * f_n * f_n_plus_1 - f_n_squared
        f_2n_plus_1 = f_n_squared + f_n_plus_1_squared
        if n >> i & 1:
            f_n, f_n_plus_1 = f_2n_plus_1, f_2n + f_2n_plus_1
        else:
            f_n, f_n_plus_1 = f_2n, f_2n_plus_1
    return f_n


def fast_fib(n):
    return matrix_exponentiation_fib(n)[0]


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def find_pisano_period(m):
    previous, current = 0, 1
    n = 0
    while True:
        previous, current = current, (previous + current) % m
        n += 1
        if (previous == 0 and current == 1):
            return n


def fib_n_modulo_m(n, m):
    pisano = find_pisano_period(m)
    n = n % pisano
    return fast_fib(n) % m


def last_digit_of_summed_fib_numbers(n):
    return 4
