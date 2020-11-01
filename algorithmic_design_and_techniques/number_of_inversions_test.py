import unittest
import math


def merge(arr, left, right):
    mid = math.ceil((right + left) / 2)
    while left <= right:
        if arr[left] <= arr[mid]:
            left += 1
        elif arr[right] <= arr[left]:
            # count 1
            arr[left], arr[mid] = arr[mid], arr[left]

# def merge_count(arr, left, right):
#     mid = (left + right) // 2
#     if (left == right):
#         return;
#     merge_count(arr, left, mid)
#     merge_count(arr, mid + 1, right)
#     merge()


# def count_inversions(arr):
#     merge_count(arr, 0, len(arr) - 1)


class NumberOfInversions(unittest.TestCase):
    def test_merge(self):
        arr = [2, 1]
        merge(arr, 0, 1)
        self.assertEqual(arr, [1, 2])
    # def test_case1(self):
    #     self.assertEqual(count_inversions([2, 3, 9, 2, 9])
