import unittest


def insert(a, b):
    pass


operations = []


def edit_distance(a_str, b_str):
    a_row = []
    b_row = []
    a_crawler, b_crawler = 0, 0
    while a_crawler < len(a_row) and b_crawler < len(b_row):
        temp_a = a_row
        temp_b = b_row


def alignment_cost(a_row, b_row):
    result = 0
    for a, b in zip(a_row, b_row):
        if a != b:
            result += 1
    return result


class EditDistance(unittest.TestCase):
    def test_matching(self):
        self.assertEqual(edit_distance("ab", "ab"), 0)

    def test_short_ports(self):
        self.assertEqual(edit_distance("short", "port"), 3)

    def test_editing_distance(self):
        self.assertEqual(edit_distance("editing", "distance"), 5)

    def test_score_all_matching(self):
        self.assertEqual(alignment_cost(["A", "B"],
                                        ["A", "B"]), 0)

    def test_score_with_mismatch(self):
        self.assertEqual(alignment_cost(["e", "d", "i", " ", "t", "i", "n", "g", " "],
                                        [" ", "d", "i", "s", "t", "a", "n", "c", "e"]), 5)

    def test_score_some_matching(self):
        self.assertEqual(
            alignment_cost(
                ["S", "H", "O", "R", "T", " "],
                [" ", "P", "O", "R", "T", "S"]
            ), 3)
