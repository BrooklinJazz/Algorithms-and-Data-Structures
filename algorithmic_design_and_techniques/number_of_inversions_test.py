import unittest
import math


def merge(arr, l, r) -> int:
    if l == r:
        return 1
    left_crawl = l
    mid = math.ceil((r + l) / 2)
    right_crawl = mid
    temp = []
    while(left_crawl < mid and right_crawl <= r):
        if arr[left_crawl] <= arr[right_crawl]:
            temp.append(arr[left_crawl])
            left_crawl += 1
        else:
            temp.append(arr[right_crawl])
            right_crawl += 1

    while(right_crawl <= r):
        temp.append(arr[right_crawl])
        right_crawl += 1

    while(left_crawl < mid):
        temp.append(arr[left_crawl])
        left_crawl += 1

    for i, el in enumerate(temp):
        arr[i + l] = el

    return 1


def mergesort(arr, l, r):
    mid = (r + l) // 2
    if (l == r):
        return
    mergesort(arr, l, mid)
    mergesort(arr, mid + 1, r)
    merge(arr, l, r)


def count_inversions(arr, l, r) -> int:
    mid = (r + l) // 2
    if (l == r):
        return 0
    count1 = count_inversions(arr, l, mid)
    count2 = count_inversions(arr, mid + 1, r)

    return merge(arr, l, r) + count1 + count2


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

    def test_merge_sort_count_inversions(self):
        arr = [4, 3, 2, 1]
        count_inversions(arr, 0, 3)
        self.assertEqual(arr, [1, 2, 3, 4])

    def test_case1(self):
        self.assertEqual(count_inversions([2, 3, 9, 2, 9], 0, 4), 2)
