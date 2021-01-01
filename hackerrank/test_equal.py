import pytest
increments = [0, 1, 2, 5]


def arrays_contain_matching_element(arr_of_arr):
    for arr in arr_of_arr:


def equal(arr):
    dp = [[[] for _ in increments] for _ in arr]
    # todo handle case where all el in arr are the same
    for i, el in enumerate(arr):
        for j, inc in enumerate(increments):
            dp[i][j] = el + inc
    pytest.set_trace()
    return dp


def test_no_operations():
    assert equal([1, 1, 1]) == 0


def test_1_operation():
    assert equal([1, 2]) == 1


def test_2_operations():
    assert equal([2, 2, 3, 7]) == 3
