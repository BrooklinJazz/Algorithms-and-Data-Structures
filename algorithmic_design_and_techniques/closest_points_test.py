import unittest
import math
import time


def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def naive_closest_points(xs, ys):
    smallest = calculate_distance(xs[0], ys[0], xs[1], ys[1])
    for i in range(len(xs)):
        for j in range(len(xs)):
            if i != j:
                current = calculate_distance(xs[i], ys[i], xs[j], ys[j])
                smallest = min(smallest, current)
    return smallest


def qsort(arr, x_or_y_index=0):
    if len(arr) <= 1:
        return arr
    else:
        return qsort([x for x in arr[1:] if x[x_or_y_index] < arr[0][x_or_y_index]]) + \
            [arr[0]] + \
            qsort([x for x in arr[1:] if x[x_or_y_index] >= arr[0][x_or_y_index]])


def sortX(arr):
    return qsort(arr, 0)


def sortY(arr):
    return qsort(arr, 1)


def closest_points():
    pass


tested_closest_points = closest_points


class ClosestPoints(unittest.TestCase):
    def test_sort_x(self):
        self.assertEqual(sortX([[1, 0], [0, 2]]), [[0, 2], [1, 0]])

    def test_sort_y(self):
        self.assertEqual(sortY([[0, 2], [1, 0]]), [[1, 0], [0, 2]])

    def test_elapsed_time(self):
        start = time.monotonic()
        num = 3000
        xs = list(range(num))
        ys = list(range(num))
        tested_closest_points(xs, ys)
        end = time.monotonic()
        elapsed = end - start
        self.assertTrue(elapsed < 5)

    def test_simple(self):
        xs = [0, 3]
        ys = [0, 4]
        self.assertEqual(tested_closest_points(xs, ys), 5)

    def test_against_naive(self):
        num = 100
        xs = list(range(num))
        ys = list(range(num))
        self.assertEqual(tested_closest_points(xs, ys),
                         naive_closest_points(xs, ys))

    def test_naive_coinciding(self):
        xs = [7, 1, 4, 7]
        ys = [7, 100, 8, 7]
        self.assertEqual(naive_closest_points(xs, ys), 0)

    def test_naive(self):
        xs = [0, 3]
        ys = [0, 4]
        self.assertEqual(naive_closest_points(xs, ys), 5)

    def test_calculate_distance(self):
        self.assertEqual(calculate_distance(0, 0, 3, 4), 5)

    def test_calculate_distance_coinciding(self):
        self.assertEqual(calculate_distance(0, 0, 0, 0), 0)
