import unittest
import random
from divide_and_conquer import binary_search, majority_element, proven_majority_element, quicksort, find_pivot_index, swap, should_swap, insert_pivot, increment_partition_trackers, partition


class DivideAndConquer(unittest.TestCase):
    elements = [1, 5, 8, 12, 13]

    def test_binary_search_against_findable_numbers(self):
        self.assertEqual(binary_search(self.elements, 12), 3)
        self.assertEqual(binary_search(self.elements, 5), 1)

    def test_binary_search_non_findable_numbers(self):
        self.assertEqual(binary_search(self.elements, 21), -1)

    def test_binary_search_large_search_data(self):
        self.assertEqual(binary_search(range(0, 10001), 10000), 10000)


class MajorityElement(unittest.TestCase):
    def test_case_with_majority(self):
        self.assertEqual(majority_element([2, 3, 9, 2, 2]), 1)

    def test_case_no_majority(self):
        self.assertEqual(majority_element([1, 3, 9, 5, 2]), 0)

    def test_case_large_random_dataset(self):
        arr = []
        for n in range(5000):
            arr.append(1)
            arr.append(random.randint(2, 100))
        self.assertEquals(majority_element(arr), 0)
        arr.append(1)
        self.assertEquals(majority_element(arr), 1)

    def test_against_proven_fn(self):
        arr = []
        for i in range(10000):
            arr.append(random.randint(0, 10000))
        self.assertEquals(majority_element(arr), proven_majority_element(arr))


class QuickSort(unittest.TestCase):
    def test_quicksort_end_case(self):
        arr = [1, 1, 1, 20, 5]
        quicksort(arr, 3, 4)
        self.assertEqual(arr, [1, 1, 1, 5, 20])

    def test_quicksort_right_half(self):
        arr = [1, 1, 30, 20, 10]
        quicksort(arr, 2, 4)
        self.assertEqual(arr, [1, 1, 10, 20, 30])

    def test_quicksort_odd_number_of_elements(self):
        arr = [5, 4, 3, 2, 1]
        quicksort(arr, 0, 4)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_find_pivot_index(self):
        arr = [1, 2, 3, 4, 5]
        l = 0
        r = len(arr) - 1
        self.assertEqual(find_pivot_index(arr, l, r), 2)

    def test_partition_end_case(self):
        arr = [2, 3, 9, 2, 2]
        l = 4
        r = 4
        pivot_index = 2
        partition(arr, pivot_index, l, r)
        self.assertEqual(arr, [2, 3, 2, 2, 9])

    def test_partition_against_right_only_dataset(self):
        arr = [21, 28, 9, 22, 19]
        l = 0
        r = 4
        pivot_index = 2
        partition(arr, pivot_index, l, r)
        self.assertEqual(arr[0], 9)

    def test_partition_against_left_only_dataset(self):
        arr = [2, 3, 9, 2, 2]
        l = 0
        r = 4
        pivot_index = 2
        partition(arr, pivot_index, l, r)
        self.assertEqual(arr[r], 9)

    def test_partition_against_mixed_dataset(self):
        arr = [20, 8, 9, 12, 2]
        l = 0
        r = 4
        pivot_index = 2
        partition(arr, pivot_index, l, r)
        self.assertEqual(arr, [2, 8, 9, 12, 20])

    def test_increment_counters(self):
        left_most = 0
        right_most = 4
        arr = [2, 3, 9, 2, 2]
        pivot_index = 2
        (l, r) = increment_partition_trackers(
            arr, pivot_index, left_most, right_most)
        self.assertEqual(l, 1)
        self.assertEqual(r, 4)
        (l, r) = increment_partition_trackers(arr, pivot_index, l, r)
        self.assertEqual(l, 3)
        self.assertEqual(r, 4)

    def test_insert_pivot_to_right(self):
        arr = [2, 3, 9, 2, 2]
        left_most = 4
        right_most = 4
        pivot_index = 2
        insert_pivot(arr, pivot_index, left_most, right_most)
        self.assertEqual(arr, [2, 3, 2, 2, 9])

    def test_insert_pivot_to_left(self):
        arr = [2, 3, 22, 10, 12]
        left_most = 1
        right_most = 2
        pivot_index = 3
        insert_pivot(arr, pivot_index, left_most, right_most)
        self.assertEqual(arr, [2, 3, 10, 22, 12])

    def test_should_swap(self):
        arr = [10, 3, 9, 2, 2]
        l = 0
        r = len(arr) - 1
        pivot_index = find_pivot_index(arr, l, r)
        self.assertTrue(should_swap(arr, pivot_index, l, r))

    def test_swap(self):
        arr = [10, 3, 9, 2, 2]
        l = 0
        r = len(arr) - 1
        swap(arr, l, r)
        self.assertEqual(arr, [2, 3, 9, 2, 10])
