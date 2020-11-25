import copy
import sys
import pytest


def cost_to_form_magic_square(s):
    all_magic_squares = generate_all_magic_squares()
    result = sys.maxsize
    for m in all_magic_squares:
        result = min(cost_to_form(s, m), result)

    return result


# obviously broken
def find_nearest_magic_constant(s):
    return 15


def rotate_r(s):
    temp = copy.deepcopy(s)
    temp[0][0] = s[1][0]
    temp[0][1] = s[0][0]
    temp[0][2] = s[0][1]
    temp[1][0] = s[2][0]
    temp[1][2] = s[0][2]
    temp[2][0] = s[2][1]
    temp[2][1] = s[2][2]
    temp[2][2] = s[1][2]
    return temp


def generate_all_magic_squares():
    square = [[6, 1, 8], [7, 5, 3], [2, 9, 4]]
    result = [square]
    for i in range(7):
        square = rotate_r(square)
        result.append(square)
    return result


def cost_to_form(s, m):
    cost = 0
    for a, b in zip(s, m):
        for x, y in zip(a, b):
            cost += abs(x - y)
    return cost


def is_magic_square(s):
    row0 = s[0]
    row1 = s[1]
    row2 = s[2]
    column0 = [i[0] for i in s]
    column1 = [i[1] for i in s]
    column2 = [i[2] for i in s]
    diagonal0 = [row0[0], row1[1], row2[2]]
    diagonal1 = [row0[2], row1[1], row2[0]]
    to_iterate = [
        row0, row1, row2, column0, column1, column2, diagonal0, diagonal1
    ]

    result = None
    for arr in to_iterate:
        x, y, z = arr[0], arr[1], arr[2]
        if result == None:
            result = x + y + z
        if (x + y + z) != result:
            return False
    return True


non_magic_square_static_center = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]
magic_square_option_1 = [[4, 9, 2], [4, 5, 6], [7, 1, 7]]
magic_square_option_2 = [[4, 8, 3], [4, 5, 6], [7, 2, 6]]

non_magic_square = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
magic_square = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]

non_magic_square2 = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
magic_square2 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]


def test_generate_all_magic_squares():
    assert len(generate_all_magic_squares()) == 8


def test_rotate_right():
    square = [[6, 1, 8], [7, 5, 3], [2, 9, 4]]
    assert rotate_r(square)[0] == [7, 6, 1]
    assert rotate_r(square)[1] == [2, 5, 8]
    assert rotate_r(square)[2] == [9, 4, 3]


def test_cost_to_form_magic_square():
    assert cost_to_form_magic_square(non_magic_square) == 7
    assert cost_to_form_magic_square(non_magic_square2) == 1


def test_cost_to_form_7_changes():
    assert cost_to_form(non_magic_square, magic_square) == 7


def test_cost_to_form_1_change():
    assert cost_to_form(non_magic_square2, magic_square2) == 1


def test_is_magic_square_true():
    assert is_magic_square(magic_square) == True
    assert is_magic_square(magic_square2) == True


def test_is_magic_square_false():
    assert not is_magic_square(non_magic_square)
    assert not is_magic_square(non_magic_square2)
