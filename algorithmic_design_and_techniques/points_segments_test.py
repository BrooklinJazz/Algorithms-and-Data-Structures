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


def count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i, start in enumerate(starts):
        end = ends[i]
        low, high = find_low_high(start, end, points)
        if points[low] >= start and points[high] <= end:
            for j in range(low, high + 1):
                cnt[j] += 1
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

    def test_non_matching_segment_matching_segment_single_point(self):
        self.assertEquals(tested_count_segments([0, 5], [4, 10], [7]), [1])

    def test_against_naive_random_input(self):
        starts = list(range(100))
        ends = list(range(100))
        points = list(range(100))
        random.shuffle(starts)
        random.shuffle(ends)
        random.shuffle(points)
        self.assertEqual(tested_count_segments(starts, ends, points),
                         naive_count_segments(starts, ends, points))
