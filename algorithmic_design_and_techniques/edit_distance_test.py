import unittest
import sys


def insert(a, b):
    pass


operations = []


def edit_distance(a_str, b_str):
    row_a, row_b = create_sequence_matrix(a_str, b_str)
    return alignment_cost(row_a, row_b)

def create_sequence_matrix

# def create_sequence_matrix(a_str, b_str):
#     a_row = list(a_str)
#     b_row = list(b_str)
#     a_crawler, b_crawler = 0, 0
#     i = 0
#     while a_crawler < len(a_str) and b_crawler < len(b_str):
#         deletion_cost, insertion_cost, current_cost = sys.maxsize, sys.maxsize, alignment_cost(
#             a_row, b_row)
#         if a_str[a_crawler] == b_str[b_crawler]:
#             b_crawler += 1
#             a_crawler += 1
#         else:
#             temp_b_row = b_row.copy()
#             temp_b_row.insert(i, " ")
#             deletion_cost = alignment_cost(a_row, temp_b_row)

#             temp_a_row = a_row.copy()
#             temp_a_row.insert(i, " ")
#             insertion_cost = alignment_cost(temp_a_row, b_row)
#             if current_cost == min(deletion_cost, insertion_cost, current_cost):
#                 b_crawler += 1
#                 a_crawler += 1
#             elif deletion_cost < insertion_cost:
#                 b_row = temp_b_row
#                 b_crawler += 1

#             elif insertion_cost < deletion_cost:
#                 a_row = temp_a_row
#                 a_crawler += 1
#             else:
#                 print("why am I here?")
#                 b_crawler += 1
#                 a_crawler += 1
#             i += 1 # should this also be on if?
#     while len(a_row) < len(b_row):
#         a_row.append(" ")
#     return a_row, b_row


def alignment_cost(a_row, b_row):
    score = 0
    for a, b in zip(a_row, b_row):
        if a == b:
            score += 1
    return max(len(a_row), len(b_row)) - score


class EditDistance(unittest.TestCase):
    # Edit Distance
    def test_matching(self):
        self.assertEqual(edit_distance("ab", "ab"), 0)

    def test_short_ports(self):
        self.assertEqual(edit_distance("short", "ports"), 3)

    def test_deletion(self):
        self.assertEqual(edit_distance("ed", "d"), 1)

    def test_insertion(self):
        self.assertEqual(edit_distance("db", "ds"), 1)

    def test_editing_distance(self):
        self.assertEqual(edit_distance("editing", "distance"), 5)

    # Sequence Matrix
    def test_sequence_matrix_editing_distance(self):
        self.assertEqual(create_sequence_matrix("editing", "distance"),
                         (
            ["e", "d", "i", " ", "t", "i", "n", "g", " "],
            [" ", "d", "i", "s", "t", "a", "n", "c", "e"]
        )
        )

    def test_sequence_matrix_short_ports(self):
        self.assertEqual(create_sequence_matrix("short", "ports"),
                         (
            ["s", "h", "o", "r", "t", " "],
            [" ", "p", "o", "r", "t", "s"]
        )
        )

    def test_sequence_matrix_matching(self):
        self.assertEqual(create_sequence_matrix(
            "ed", "ed"), (["e", "d"], ["e", "d"]))

    def test_sequence_matrix_deletion(self):
        self.assertEqual(create_sequence_matrix("ed", "d"),
                         (["e", "d"],
                          [" ", "d"])
                         )

    def test_sequence_matrix_non_matching(self):
        self.assertEqual(create_sequence_matrix("ds", "da"),
                         (["d", "s"],
                          ["d", "a"])
                         )

    def test_sequence_matrix_insertion(self):
        self.assertEqual(create_sequence_matrix("d", "ed"),
                         ([" ", "d"],
                          ["e", "d"])
                         )

    # Alignment Cost
    def test_alignment_cost_all_matching(self):
        self.assertEqual(alignment_cost(["A", "B"],
                                        ["A", "B"]), 0)

    def test_alignment_cost_diff_size(self):
        self.assertEqual(alignment_cost(["A"],
                                        ["A", "B"]), 1)

    def test_alignment_cost_with_mismatch(self):
        self.assertEqual(alignment_cost(["e", "d", "i", " ", "t", "i", "n", "g", " "],
                                        [" ", "d", "i", "s", "t", "a", "n", "c", "e"]), 5)

    def test_alignment_cost_short_ports(self):
        self.assertEqual(
            alignment_cost(
                ["S", "H", "O", "R", "T", " "],
                [" ", "P", "O", "R", "T", "S"]
            ), 3)
