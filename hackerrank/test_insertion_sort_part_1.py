import random


def insertion_sort(n, arr):
    if n == 1:
        return arr
    for i in range(1, n):
        is_less = arr[i] < arr[i - 1]
        if is_less:
            for j in range(i - 1):
                if arr[j] >= arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]
    return arr


def test_1_el():
    assert insertion_sort([1]) == [1]


def test_2_el_sorted():
    assert insertion_sort([1, 2]) == [1, 2]


def test_2_el_unsorted():
    assert insertion_sort([2, 1]) == [1, 2]


def test_random_el_unsorted():
    sorted_arr = list(range(10))
    arr = list(range(10))
    random.shuffle(arr)
    assert insertion_sort(arr) == sorted_arr
