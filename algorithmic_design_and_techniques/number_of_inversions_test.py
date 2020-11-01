import unittest
import math


def merge(arr, left, right):
    # while the temp array is not of size right - left
    if (left == right):
        return
    temp = []
    mid = math.ceil((right + left) / 2)
    left_crawl = left
    right_crawl = mid
    while (left_crawl < mid and right_crawl <= right):
        if arr[left_crawl] < arr[right_crawl]:
            temp.append(arr[left_crawl])
            left_crawl += 1
        else:
            temp.append(arr[right_crawl])
            right_crawl += 1
    if left_crawl < mid:
        temp = temp + arr[left_crawl:mid]
    if right_crawl < right:
        temp = temp + arr[right_crawl:right]
    arr[left: right + 1] = temp


def mergesort(arr, l, r):
    mid = (r + l) // 2
    if (l == r):
        return
    mergesort(arr, l, mid)
    mergesort(arr, mid + 1, r)
    merge(arr, l, r)


class NumberOfInversions(unittest.TestCase):
    def test_merge_1_el_array(self):
        arr = [2, 1]
        merge(arr, 1, 1)
        self.assertEqual(arr, [2, 1])

    def test_merge_2_el_array(self):
        arr = [2, 1]
        merge(arr, 0, 1)
        self.assertEqual(arr, [1, 2])

    def test_merge_4_el_array(self):
        arr = [3, 4, 1, 2]
        merge(arr, 0, 3)
        self.assertEqual(arr, [1, 2, 3, 4])

    def test_merge_4_el_array_half(self):
        arr = [3, 4, 2, 1]
        merge(arr, 2, 3)
        self.assertEqual(arr, [3, 4, 1, 2])

    def test_merge_sort(self):
        arr = [4, 3, 2, 1]
        mergesort(arr, 0, 3)
        self.assertEqual(arr, [1, 2, 3, 4])

    # def test_case1(self):
    #     self.assertEqual(count_inversions([2, 3, 9, 2, 9])
