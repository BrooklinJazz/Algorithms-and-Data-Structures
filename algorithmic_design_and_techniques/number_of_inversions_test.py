import unittest
import math


def merge(arr, l, r) -> int:
    count = 0
    if l == r:
        return count
    left_crawl = l
    mid = math.ceil((r + l) / 2)
    right_crawl = mid
    temp = []
    while(left_crawl < mid and right_crawl <= r):
        if arr[left_crawl] <= arr[right_crawl]:
            temp.append(arr[left_crawl])
            left_crawl += 1
        else:
            count += 1
            temp.append(arr[right_crawl])
            right_crawl += 1

    while(right_crawl <= r):
        temp.append(arr[right_crawl])
        right_crawl += 1

    count_multiplyer = 0
    while(left_crawl < mid):
        temp.append(arr[left_crawl])
        left_crawl += 1
        count_multiplyer += 1

    if count_multiplyer > 0:
        count = count * count_multiplyer
        pass

    for i, el in enumerate(temp):
        arr[i + l] = el

    return count


def count_inversions(arr, l, r) -> int:
    # mid = (r + l) // 2
    mid = math.ceil((r + l) / 2)
    if (l == r):
        return 0
    count1 = count_inversions(arr, l, mid - 1)
    count2 = count_inversions(arr, mid, r)
    count3 = merge(arr, l, r)
    total = count1 + count2 + count3

    return total


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
        count_inversions(arr, 0, 3)
        self.assertEqual(arr, [1, 2, 3, 4])

    def test_merge_sort_count_inversions(self):
        arr = [4, 3, 2, 1]
        count_inversions(arr, 0, 3)
        self.assertEqual(arr, [1, 2, 3, 4])

    def test_merge_sort_count_inversions_5_el(self):
        arr = [2, 3, 9, 2, 9]
        count_inversions(arr, 0, 4)
        self.assertEqual(arr, [2, 2, 3, 9, 9])

    def test_case1(self):
        self.assertEqual(count_inversions([2, 3, 9, 2, 9], 0, 4), 2)

    def test_failed_case(self):
        self.assertEqual(count_inversions([9, 8, 7, 3, 2, 1], 0, 5), 15)

    def test_failed_case_sort(self):
        arr = [9, 8, 7, 3, 2, 1]
        count_inversions(arr, 0, 5)
        self.assertEqual(arr, [1, 2, 3, 7, 8, 9])

    def test_failed_case_sort_edge(self):
        arr = [9, 8, 7, 3, 2, 1]

        self.assertEqual(count_inversions(arr, 4, 5), 1)


# # Python 3 program to count inversions in an array

# # Function to Use Inversion Count
# def mergeSort(arr, n):
#     # A temp_arr is created to store
#     # sorted array in merge function
#     temp_arr = [0]*n
#     return _mergeSort(arr, temp_arr, 0, n-1)

# # This Function will use MergeSort to count inversions


# def _mergeSort(arr, temp_arr, left, right):

#     # A variable inv_count is used to store
#     # inversion counts in each recursive call

#     inv_count = 0

#     # We will make a recursive call if and only if
#     # we have more than one elements

#     if left < right:

#         # mid is calculated to divide the array into two subarrays
#         # Floor division is must in case of python

#         mid = (left + right)//2

#         # It will calculate inversion
#         # counts in the left subarray

#         inv_count += _mergeSort(arr, temp_arr,
#                                 left, mid)

#         # It will calculate inversion
#         # counts in right subarray

#         inv_count += _mergeSort(arr, temp_arr,
#                                 mid + 1, right)

#         # It will merge two subarrays in
#         # a sorted subarray

#         inv_count += merge(arr, temp_arr, left, mid, right)
#     return inv_count

# # This function will merge two subarrays
# # in a single sorted subarray


# def merge(arr, temp_arr, left, mid, right):
#     i = left     # Starting index of left subarray
#     j = mid + 1  # Starting index of right subarray
#     k = left     # Starting index of to be sorted subarray
#     inv_count = 0

#     # Conditions are checked to make sure that
#     # i and j don't exceed their
#     # subarray limits.

#     while i <= mid and j <= right:

#         # There will be no inversion if arr[i] <= arr[j]

#         if arr[i] <= arr[j]:
#             temp_arr[k] = arr[i]
#             k += 1
#             i += 1
#         else:
#             # Inversion will occur.
#             temp_arr[k] = arr[j]
#             inv_count += (mid-i + 1)
#             k += 1
#             j += 1

#     # Copy the remaining elements of left
#     # subarray into temporary array
#     while i <= mid:
#         temp_arr[k] = arr[i]
#         k += 1
#         i += 1

#     # Copy the remaining elements of right
#     # subarray into temporary array
#     while j <= right:
#         temp_arr[k] = arr[j]
#         k += 1
#         j += 1

#     # Copy the sorted subarray into Original array
#     for loop_var in range(left, right + 1):
#         arr[loop_var] = temp_arr[loop_var]

#     return inv_count


# # Driver Code
# # Given array is
# arr = [1, 20, 6, 4, 5]
# n = len(arr)
# result = mergeSort(arr, n)
