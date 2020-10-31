# def binary_search(search_elements, to_find):
#     return slow_binary_search(search_elements, to_find)

import random


def binary_search(search_elements, to_find):
    return fast_binary_search(search_elements, to_find, len(search_elements), 0)


# def slow_binary_search(search_elements, to_find):
#     def F(low, mid, high):
#         if search_elements[mid] == to_find:
#             return mid
#         elif low == mid:
#             return -1
#         elif search_elements[mid] > to_find:
#             high = mid
#             mid = (high + low) // 2
#         elif search_elements[mid] < to_find:
#             low = mid
#             mid = (high + low) // 2
#         return F(low, mid, high)
#     return F(0, len(search_elements) // 2, len(search_elements))


def fast_binary_search(search_elements, to_find, high=None, low=0):
    mid = (high + low) // 2
    el = search_elements[mid]
    if el == to_find:
        return mid
    elif low == mid:
        return -1
    elif el < to_find:
        return fast_binary_search(search_elements, to_find, high, mid)
    else:
        return fast_binary_search(search_elements, to_find, mid, low)


def majority_element(arr):
    # find major canditate
    major_candidate = arr[0]
    greatest_count = 0
    count = 0
    minor_candidate = arr[0]
    for n in arr:
        if n == minor_candidate:
            count += 1
        else:
            count -= 1

        if count == 0:
            minor_candidate = n
            count = 1

        if count > greatest_count:
            major_candidate = minor_candidate
            greatest_count = count
    major_count = 0
    for (i, n) in enumerate(arr):
        if n == major_candidate:
            major_count += 1
    if major_count > len(arr) // 2:
        return 1
    else:
        return 0


def findCandidate(A):
    maj_index = 0
    count = 1
    for i in range(len(A)):
        if A[maj_index] == A[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            maj_index = i
            count = 1
    return A[maj_index]


def isMajority(A, cand):
    count = 0
    for i in range(len(A)):
        if A[i] == cand:
            count += 1
    if count > len(A)/2:
        return True
    else:
        return False


def proven_majority_element(A):
    # Find the candidate for Majority
    cand = findCandidate(A)

    # Print the candidate if it is Majority
    if isMajority(A, cand) == True:
        return 1
    else:
        return 0


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def quicksort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # use partition3
    m = partition2(a, l, r)
    quicksort(a, l, m - 1)
    quicksort(a, m + 1, r)
    return a


def find_pivot_index(arr, l, r):
    return (r + l) // 2


def partition(arr, pivot_index, left_most, right_most):
    (l, r) = left_most, right_most
    for i in range(right_most + 1 - left_most):
        if l >= r:
            return insert_pivot(arr, pivot_index, l, r)
        (l, r) = increment_partition_trackers(arr, pivot_index, l, r)


def increment_partition_trackers(arr, pivot_index, left_most, right_most):
    (l, r) = left_most, right_most
    if arr[l] < arr[pivot_index]:
        l += 1
    if arr[r] > arr[pivot_index]:
        r -= 1
    if r == pivot_index:
        r -= 1
    if l == pivot_index:
        l += 1
    return (l, r)


def insert_pivot(arr, pivot_index, left_most, right_most):
    if pivot_index < left_most:
        temp = arr[pivot_index]
        arr[pivot_index] = arr[left_most]
        arr[left_most] = temp
    if left_most < pivot_index:
        temp = arr[pivot_index]
        arr[pivot_index] = arr[right_most]
        arr[right_most] = temp


def should_swap(arr, pivot_index, left, right):
    return arr[left] > arr[pivot_index] and arr[right] < arr[pivot_index]


def swap(arr, l, r):
    leftNum = arr[l]
    rightNum = arr[r]
    arr[l] = rightNum
    arr[r] = leftNum
