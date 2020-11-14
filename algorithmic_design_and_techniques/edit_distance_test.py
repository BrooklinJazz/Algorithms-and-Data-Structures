import unittest
import sys


operations = []


def edit_distance(a_str, b_str):
    a_len = len(a_str)
    b_len = len(b_str)
    dp = [[0 for b in range(b_len + 1)] for a in range(a_len + 1)]
    if a_len == 0 or b_len == 0:
        return max(b_len, a_len)
    for a_index in range(a_len + 1):
        for b_index in range(b_len + 1):
            b_char = b_str[b_index - 1]
            a_char = a_str[a_index - 1]
            if a_index == 0:
                dp[a_index][b_index] = b_index
            elif b_index == 0:
                dp[a_index][b_index] = a_index
            elif a_char == b_char:
                dp[a_index][b_index] = dp[a_index - 1][b_index - 1]
            else:
                # [b1a1, b1a2]
                # [b2a1, b2a2]
                b1a1 = dp[a_index - 1][b_index - 1]
                b1a2 = dp[a_index][b_index - 1]
                b2a1 = dp[a_index - 1][b_index]
                dp[a_index][b_index] = 1 + min(b1a1, b1a2, b2a1)
    return dp[a_len][b_len]


def create_sequence_matrix(a_str, b_str):
    pass


def score(a_row, b_row):
    score = 0
    for a, b in zip(a_row, b_row):
        if a == b:
            score += 1
    return score


def alignment_cost(a_row, b_row):
    return max(len(a_row), len(b_row)) - score(a_row, b_row)


class EditDistance(unittest.TestCase):
    # Edit Distance
    def test_matching(self):
        self.assertEqual(edit_distance("ab", "ab"), 0)

    def test_short_ports(self):
        self.assertEqual(edit_distance("short", "ports"), 3)

    def test_0_char_str(self):
        self.assertEqual(edit_distance("e", ""), 1)

    def test_1_and_7_char_str(self):
        self.assertEqual(edit_distance("e", "editing"), 6)

    def test_1_char_str(self):
        self.assertEqual(edit_distance("e", "d"), 1)

    def test_2_char_str(self):
        self.assertEqual(edit_distance("ed", "di"), 2)

    def test_3_char_str(self):
        self.assertEqual(edit_distance("edi", "dis"), 2)

    def test_4_char_str(self):
        self.assertEqual(edit_distance("edit", "dist"), 2)

    def test_5_char_str(self):
        self.assertEqual(edit_distance("editi", "dista"), 3)

    def test_6_char_str(self):
        self.assertEqual(edit_distance("editin", "distan"), 3)

    def test_7_char_str(self):
        self.assertEqual(edit_distance("editing", "distanc"), 4)

    def test_8_char_str(self):
        self.assertEqual(edit_distance("editing", "distance"), 5)

    def test_failing(self):
        self.assertEqual(edit_distance(
            "zoologicoarchaeologist", "zoogeologist"), 10)
