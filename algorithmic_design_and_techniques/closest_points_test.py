import unittest
import math
import time


def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# def brute_force(xs, ys):
#     smallest = calculate_distance(xs[0], ys[0], xs[1], ys[1])
#     for i in range(len(xs)):
#         for j in range(len(xs)):
#             if i != j:
#                 current = calculate_distance(xs[i], ys[i], xs[j], ys[j])
#                 smallest = min(smallest, current)
#     return smallest


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


def brute_force(arr):
    l = len(arr)
    min_d = dist(arr[0], arr[1])
    for i in range(l):
        for j in range(i + 1, l):
            next_dist = dist(arr[i], arr[j])
            if next_dist < min_d:
                min_d = next_dist
    return min_d


def closest_points(points):
    n = len(points)
    if len(points) <= 3:
        return brute_force(points)
    points_by_x = sortX(points)
    points_by_y = sortY(points)
    return CP(points_by_x, points_by_y, n)


x = 0
y = 1


def dist(p1, p2):
    return math.sqrt((p1[x] - p2[x]) ** 2 + (p1[y] - p2[y]) ** 2)


def strip_closest(strip, d):
    min_d = d

    for i, p1 in enumerate(strip):
        j = i
        while (j < len(strip) and strip[j][y] - strip[i][y] < min_d):
            new_dist = dist(strip[i], strip[j])
            if new_dist < min_d:
                min_d = new_dist
            j += 1
    return min_d


def CP(Px, Py, n):
    mid = n // 2
    mid_point = Px[mid]
    Pyl = []
    Pyr = []  # can't this just be mid + 1?
    li, ri = 0, 0

    for i in range(n):
        if Py[i][x] <= mid_point[x] and li < mid:
            Pyl.append(Py[i])
            li += 1
        else:
            Pyr.append(Py[i])

    dl = CP(Px, Pyl, mid)
    # won't Px + mid break?
    dr = CP(Px + mid, Pyr, n-mid)
    d = min(dl, dr)

    strip = []
    j = 0
    for i in range(n):
        if abs((Py[i][x] - mid_point[x]) < d):
            strip.append(Py[i])

    return strip_closest(strip, d)


tested_closest_points = closest_points


class ClosestPoints(unittest.TestCase):
    def test_sort_x(self):
        self.assertEqual(sortX([[1, 0], [0, 2]]), [[0, 2], [1, 0]])

    def test_sort_y(self):
        self.assertEqual(sortY([[0, 2], [1, 0]]), [[1, 0], [0, 2]])

    # def test_elapsed_time(self):
    #     start = time.monotonic()
    #     num = 3000
    #     xs = list(range(num))
    #     ys = list(range(num))
    #     tested_closest_points(xs, ys)
    #     end = time.monotonic()
    #     elapsed = end - start
    #     self.assertTrue(elapsed < 5)

    def test_simple(self):
        points = [[0, 0], [3, 4]]
        self.assertEqual(tested_closest_points(points), 5)

    # def test_against_naive(self):
    #     num = 100
    #     xs = list(range(num))
    #     ys = list(range(num))
    #     self.assertEqual(tested_closest_points(xs, ys),
    #                      brute_force(xs, ys))

    def test_naive_coinciding(self):
        points = [[7, 7], [1, 100], [4, 8], [7, 7]]
        self.assertEqual(brute_force(points), 0)

    def test_naive(self):
        points = [[0, 0], [3, 4]]
        self.assertEqual(brute_force(points), 5)

    def test_calculate_distance(self):
        self.assertEqual(calculate_distance(0, 0, 3, 4), 5)

    def test_calculate_distance_coinciding(self):
        self.assertEqual(calculate_distance(0, 0, 0, 0), 0)