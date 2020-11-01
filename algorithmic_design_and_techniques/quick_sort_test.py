import random
import unittest


def partition(arr, l, r, pivot):
    while(l <= r):
        while(arr[l] < pivot):
            l += 1
        while(arr[r] > pivot):
            r -= 1

        if (l <= r):
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    return l


def quicksort(a, l, r):
    if l >= r:
        return
    pivot = a[(l + r) // 2]
    index = partition(a, l, r, pivot)
    quicksort(a, l, index - 1)
    quicksort(a, index, r)


class QuickSortWillNotBeatMe(unittest.TestCase):

    def test_mine(self):
        num = 10
        arr = list(range(num))
        arr2 = list(range(num))
        random.shuffle(arr)
        quicksort(arr, 0, num - 1)
        self.assertEquals(arr, arr2)
