# Uses python3
from functools import lru_cache
import test

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

from math import sqrt

root_five = sqrt(5)
phi = (root_five + 1) / 2

def golden_fib(n):
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

# def matrix_exponentiation_fib2(n):
#     print(n.bit_length())
#     f_n, f_n_plus_1 = 0, 1
#     for i in range(n.bit_length() - 1, -1, -1):
#         f_n_squared = f_n * f_n
#         f_n_plus_1_squared = f_n_plus_1 * f_n_plus_1
#         f_2n = 2 * f_n * f_n_plus_1 - f_n_squared
#         f_2n_plus_1 = f_n_squared + f_n_plus_1_squared
#         if n >> i & 1:
#             f_n, f_n_plus_1 = f_2n_plus_1, f_2n + f_2n_plus_1
#         else:
#             f_n, f_n_plus_1 = f_2n, f_2n_plus_1
#     return f_n

# fib = {0: 0, 1: 1, 2: 1}
# def calc_large_fib(i):
#     for x in range(i + 1):
#         calc_fib(x)
#     return fib.get(i)

# def calc_fib(i):
#     value = fib.get(i)
#     if value is not None:
#         return value
#     else:
#         value = calc_fib(i - 1) + calc_fib(i - 2)
#         fib[i] = value
#     return value

# def find_last_digit(i):
#     return memoized_fib(i) % 10

# n = int(input())
# print(matrix_exponentiation_fib(n)[0])

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def fibNModuloM(n, m):
    matrix_exponentiation_fib

test.matches(get_fibonacci_huge_naive, fibNModuloM, 239, 1000)


