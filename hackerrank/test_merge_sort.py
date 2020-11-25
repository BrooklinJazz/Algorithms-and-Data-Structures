import pytest
import random


def merge_sort(arr):
    msort(arr, 0, len(arr) - 1)


def msort(arr, l, r):
    if l >= r:
        return
    m = (l + r) // 2
    msort(arr, l, m)
    msort(arr, m + 1, r)
    merge(arr, l, r)


def merge(arr, l, r):
    m = (r + l) // 2
    left_c = l
    right_c = m + 1
    temp_arr = []
    while left_c <= m and right_c <= r:
        if (arr[left_c] < arr[right_c]):
            temp_arr.append(arr[left_c])
            left_c += 1
        elif (arr[right_c] < arr[left_c]):
            temp_arr.append(arr[right_c])
            right_c += 1

    while left_c <= m:
        temp_arr.append(arr[left_c])
        left_c += 1

    while right_c <= r:
        temp_arr.append(arr[right_c])
        right_c += 1

    for i, el in enumerate(temp_arr):
        arr[i + l] = el


def test_merge():
    arr = [1, 3, 2, 4]
    merge(arr, 0, 3)
    assert arr == [1, 2, 3, 4]


def test_partial_merge():
    arr = [3, 4, 2, 1]
    merge(arr, 2, 3)
    assert arr == [3, 4, 1, 2]


def test_merge_5el():
    arr = [3, 4, 5, 1, 2]
    merge(arr, 0, 4)
    assert arr == [1, 2, 3, 4, 5]


def test_against_1el():
    arr = [4]
    merge_sort(arr)
    assert arr == [4]


def test_against_2_el():
    arr = [4, 2]
    merge_sort(arr)
    assert arr == [2, 4]


def test_against_4_el():
    arr = [4, 2, 3, 1]
    merge_sort(arr)
    assert arr == [1, 2, 3, 4]


def test_against_5_el():
    arr = [4, 2, 3, 1, 5]
    merge_sort(arr)
    assert arr == [1, 2, 3, 4, 5]


def test_against_large_data():
    num = 1000
    arr = list(range(num))
    unsorted_arr = arr.copy()
    random.shuffle(unsorted_arr)
    merge_sort(unsorted_arr)
    assert unsorted_arr == arr
