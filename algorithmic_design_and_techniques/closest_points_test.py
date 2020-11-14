import unittest
import math
import time
import random


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


def brute_force(arr, n):
    min_d = dist(arr[0], arr[1])
    for i in range(n):
        for j in range(i + 1, n):
            min_d = min(min_d, dist(arr[i], arr[j]))
    return min_d


def closest_points(points, n):
    return CP(sortX(points), sortY(points))


x = 0
y = 1


def dist(p1, p2):
    return math.sqrt((p1[x] - p2[x]) ** 2 + (p1[y] - p2[y]) ** 2)


def CP(Pxs, Pys):
    n = len(Pxs)
    # refactor n to be param
    if n <= 3:
        return brute_force(Pxs, n)
    mid = n // 2
    mid_x = Pxs[mid][x]
    Pyl = []
    Pyr = []
    li = 0
    for P in Pys:
        if P[x] < mid_x:
            Pyl.append(P)
            li += 1
        else:
            Pyr.append(P)

    dl = CP(Pxs[:mid], Pyl)
    dr = CP(Pxs[mid:], Pyr)
    d = min(dl, dr)

    strip = list(filter(lambda point: abs(point[x] - mid_x) < d, Pys))

    min_d = d
    length = len(strip)
    for i in range(length):
        j = i + 1
        while (j < length and (strip[j][y] - strip[i][y]) < min_d):
            min_d = min(dist(strip[i], strip[j]), min_d)
            j += 1
    return min_d


def fast_format(points, n):
    return list(divide_chunks(points, n))


def divide_chunks(l, n):
    for i in range(0, n, 2):
        yield l[i:i + 2]


tested_closest_points = closest_points


# class ClosestPoints(unittest.TestCase):
#     def test_sort_x(self):
#         self.assertEqual(sortX([[1, 0], [0, 2]]), [[0, 2], [1, 0]])

#     def test_sort_y(self):
#         self.assertEqual(sortY([[0, 2], [1, 0]]), [[1, 0], [0, 2]])

#     def test_elapsed_time(self):
#         num = 10 ** 5
#         points = list(range(num * 2))
#         random.shuffle(points)
#         start = time.monotonic()
#         points = fast_format(points, len(points))
#         tested_closest_points(points, len(points))
#         end = time.monotonic()
#         elapsed = end - start
#         self.assertTrue(elapsed < 5)

#     def test_simple(self):
#         points = [[0, 0], [3, 4]]
#         self.assertEqual(tested_closest_points(points, len(points)), 5)

#     def test_against_naive(self):
#         num = 100
#         points = list(range(num * 2))
#         random.shuffle(points)
#         points = fast_format(points, len(points))
#         self.assertEqual(tested_closest_points(points, len(points)),
#                          brute_force(points, len(points)))

#     def test_naive_coinciding(self):
#         points = [[7, 7], [1, 100], [4, 8], [7, 7]]
#         self.assertEqual(brute_force(points, len(points)), 0)

#     def test_naive(self):
#         points = [[0, 0], [3, 4]]
#         self.assertEqual(brute_force(points, len(points)), 5)

#     def test_fast_format(self):
#         self.assertEqual(fast_format([0, 1, 2, 3], 4), [[0, 1], [2, 3]])


# def brute(ax):
#     mi = dist(ax[0], ax[1])
#     p1 = ax[0]
#     p2 = ax[1]
#     ln_ax = len(ax)
#     if ln_ax == 2:
#         return p1, p2, mi
#     for i in range(ln_ax-1):
#         for j in range(i + 1, ln_ax):
#             if i != 0 and j != 1:
#                 d = dist(ax[i], ax[j])
#                 if d < mi:  # Update min_dist and points
#                     mi = d
#                     p1, p2 = ax[i], ax[j]
#     return p1, p2, mi


# def closest_split_pair(p_x, p_y, delta, best_pair):
#     ln_x = len(p_x)  # store length - quicker
#     mx_x = p_x[ln_x // 2][0]  # select midpoint on x-sorted array
#     # Create a subarray of points not further than delta from
#     # midpoint on x-sorted array
#     s_y = [x for x in p_y if mx_x - delta <= x[0] <= mx_x + delta]
#     best = delta  # assign best value to delta
#     ln_y = len(s_y)  # store length of subarray for quickness
#     for i in range(ln_y - 1):
#         for j in range(i+1, min(i + 7, ln_y)):
#             p, q = s_y[i], s_y[j]
#             dst = dist(p, q)
#             if dst < best:
#                 best_pair = p, q
#                 best = dst
#     return best_pair[0], best_pair[1], best

# def solution(x, y):
#     a = list(zip(x, y))  # This produces list of tuples
#     ax = sorted(a, key=lambda x: x[0])  # Presorting x-wise
#     ay = sorted(a, key=lambda x: x[1])  # Presorting y-wise
#     p1, p2, mi = closest_pair(ax, ay)  # Recursive D&C function
#     return mi

# def closest_pair(ax, ay):
#     ln_ax = len(ax)  # It's quicker to assign variable
#     if ln_ax <= 3:
#         return brute(ax)  # A call to bruteforce comparison
#     mid = ln_ax // 2  # Division without remainder, need int
#     Qx = ax[:mid]  # Two-part split
#     Rx = ax[mid:]
#     # Determine midpoint on x-axis
#     midpoint = ax[mid][0]
#     Qy = list()
#     Ry = list()
#     for x in ay:  # split ay into 2 arrays using midpoint
#         if x[0] <= midpoint:
#             Qy.append(x)
#         else:
#             Ry.append(x)
#     # Call recursively both arrays after split
#     (p1, q1, mi1) = closest_pair(Qx, Qy)
#     (p2, q2, mi2) = closest_pair(Rx, Ry)
#     # Determine smaller distance between points of 2 arrays
#     if mi1 <= mi2:
#         d = mi1
#         mn = (p1, q1)
#     else:
#         d = mi2
#         mn = (p2, q2)
#     # Call function to account for points on the boundary
#     (p3, q3, mi3) = closest_split_pair(ax, ay, d, mn)
#     # Determine smallest distance for the array
#     if d <= mi3:
#         return mn[0], mn[1], d
#     else:
#         return p3, q3, mi3
