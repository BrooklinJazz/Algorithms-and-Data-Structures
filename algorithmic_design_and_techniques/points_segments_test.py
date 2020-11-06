import unittest
import random


def binary_search(search_elements, to_find, high=None, low=0):
    mid = (high + low) // 2
    el = search_elements[mid]
    if el == to_find:
        return mid
    elif low == mid:
        return low
    elif el < to_find:
        return binary_search(search_elements, to_find, high, mid)
    else:
        return binary_search(search_elements, to_find, mid, low)


def find_low_high(start, end, points):
    return binary_search(points, start, len(points)), binary_search(points, end, len(points))


def point_merge_sort(x):
    if len(x) < 20:
        return sorted(x)
    result = []
    mid = int(len(x) / 2)
    y = point_merge_sort(x[:mid])
    z = point_merge_sort(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i][0] == z[j][0] and y[i][1] > z[j][1]:
            # result.append(y[i])
            # i += 1
            result.append(z[j])
            j += 1
        elif y[i][0] > z[j][0]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result


# def count_segments(starts, ends, points):
#     cnt = [0] * len(points)

#     if len(starts) == 1:
#         for i, p in enumerate(points):
#             if p >= starts[0] and p <= ends[0]:
#                 cnt[i] = 1
#         return cnt
#     points = msort4(points)
#     for i, start in enumerate(starts):
#         end = ends[i]
#         low, high = find_low_high(start, end, points)
#         if points[low] >= start and points[high] <= end:
#             for j in range(low, high + 1):
#                 cnt[j] += 1
#     return cnt

START = 0
POINT = 1
END = 2


def count_segments(starts, ends, points):
    arr = []
    for start, end in zip(starts, ends):
        arr.append([start, START])
        arr.append([end, END])
    for i, p in enumerate(points):
        arr.append([p, POINT, i])
    arr = point_merge_sort(arr)
    cnt = [0] * len(points)
    openStarts = 0
    for item in arr:
        if item[1] == START:
            openStarts += 1
        elif item[1] == END:
            openStarts -= 1
        elif item[1] == POINT:
            cnt[item[2]] = openStarts
        else:
            print("I should never happen")
    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


tested_count_segments = count_segments


class FastCountSegments(unittest.TestCase):

    def test_single_point_and_segment(self):
        self.assertEquals(tested_count_segments([0], [5], [4]), [1])

    def test_two_segments_single_point(self):
        self.assertEquals(tested_count_segments([0, 4], [5, 5], [4]), [2])

    def test_single_segment_two_points(self):
        self.assertEquals(tested_count_segments([0], [5], [2, 3]), [1, 1])

    def test_two_segments_two_points(self):
        self.assertEquals(tested_count_segments(
            [0, 3], [5, 6], [3, 4]), [2, 2])

    def test_non_matching_segment_single_point(self):
        self.assertEquals(tested_count_segments([0], [4], [6]), [0])

    def test_failed_1(self):
        self.assertEquals(tested_count_segments(
            [-10], [10], [-100, 100, 0]), [0, 0, 1])

    def test_non_matching_segment_matching_segment_single_point(self):
        self.assertEquals(tested_count_segments([0, 5], [4, 10], [7]), [1])

    # def test_against_naive_random_input(self):
    #     num = 10
    #     starts = list(range(num))
    #     ends = list(range(num))
    #     points = list(range(num))
    #     random.shuffle(starts)
    #     random.shuffle(ends)
    #     print("starts", starts)
    #     print("ends", ends)
    #     print("points", points)

    #     self.assertEqual(tested_count_segments(starts, ends, points),
    #                      naive_count_segments(starts, ends, points))
