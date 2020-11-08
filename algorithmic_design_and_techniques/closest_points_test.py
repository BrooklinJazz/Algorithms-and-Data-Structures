import unittest
import math
import time
import random


def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# def bdrute_force(xs, ys):
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
        j = i + 1
        while (j < len(strip) and (strip[j][y] - strip[i][y]) < min_d):
            new_dist = dist(strip[i], strip[j])
            if new_dist < min_d:
                min_d = new_dist
            j += 1
    return min_d

# split points into sorted Px and Py
# brute force values <= 3
# create Pyl and Pyr
# find d = min(dl, dr) where dl are recursively calculated for Pyl and Pyr
# create strip of all possible candidates Py where distance to mid_point is smaller than d
# strip_closest: for each point calculate the smallest distance ignoring y differences greater than min_d


def CP(Px, Py, n):
    if n <= 3:
        return brute_force(Px)
    mid = n // 2
    mid_point = Px[mid]
    Pyl = []
    Pyr = []
    li, ri = 0, 0

    for i in range(len(Py)):
        if Py[i][x] <= mid_point[x] and li < mid:
            Pyl.append(Py[i])
            li += 1
        else:
            Pyr.append(Py[i])

    dl = CP(Px, Pyl, mid)
    dr = CP(Px, Pyr, n-mid)
    d = min(dl, dr)

    strip = []
    j = 0
    for i in range(len(Py)):
        if abs((Py[i][x] - mid_point[x]) < d):
            strip.append(Py[i])

    return strip_closest(strip, d)


def format_points(xs, ys):
    points = []
    for x, y in zip(xs, ys):
        points.append([x, y])
    return points


tested_closest_points = closest_points


class ClosestPoints(unittest.TestCase):
    def test_sort_x(self):
        self.assertEqual(sortX([[1, 0], [0, 2]]), [[0, 2], [1, 0]])

    def test_sort_y(self):
        self.assertEqual(sortY([[0, 2], [1, 0]]), [[1, 0], [0, 2]])

    def test_elapsed_time(self):

        num = 1000
        xs = list(range(num))
        ys = list(range(num))
        random.shuffle(xs)
        random.shuffle(ys)
        points = []
        for x, y in zip(xs, ys):
            points.append([x, y])
        start = time.monotonic()
        tested_closest_points(points)
        end = time.monotonic()
        elapsed = end - start
        self.assertTrue(elapsed < 5)

    def test_simple(self):
        points = [[0, 0], [3, 4]]
        self.assertEqual(tested_closest_points(points), 5)

    def test_against_naive(self):
        num = 100
        xs = list(range(num))
        ys = list(range(num))
        random.shuffle(xs)
        random.shuffle(ys)
        points = format_points(xs, ys)
        self.assertEqual(tested_closest_points(points),
                         brute_force(points))

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
