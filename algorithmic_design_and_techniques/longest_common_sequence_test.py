import random
import unittest


def naive_longest_common_subsequence(seq1, seq2):
    max_count = 0
    for char_1_index, char_1 in enumerate(seq1):
        for char_2_index, char_2 in enumerate(seq2):
            if char_2 == char_1:
                count = 0
                seq_2_crawler = char_2_index
                seq_1_crawler = char_1_index
                while seq_2_crawler < len(seq2) and seq_1_crawler < len(seq1) and seq1[seq_1_crawler] == seq2[seq_2_crawler]:
                    count += 1
                    seq_1_crawler += 1
                    seq_2_crawler += 1
                max_count = max(max_count, count)
    return max_count


def longest_common_sequence(a, b):
    a_len = len(a)
    b_len = len(b)
    dp = [[0 for x in range(b_len)] for x in range(a_len)]
    max_count = 0
    for a_i in range(a_len):
        for b_i in range(b_len):
            if a_i == 0:
                dp[a_i][b_i] = 1 if a[a_i] == b[b_i] else 0
            elif b_i == 0:
                dp[a_i][b_i] = 1 if a[a_i] == b[b_i] else 0
            elif a[a_i] == b[b_i]:
                res = 1 + dp[a_i - 1][b_i - 1]
                dp[a_i][b_i] = res
                max_count = max(res, max_count)
    return max_count


method_under_test = longest_common_sequence


class LongestCommonSubsequence(unittest.TestCase):
    def test_no_matching(self):
        self.assertEqual(method_under_test([2, 5], [7, 7, 7]), 0)

    def test_2_matching(self):
        self.assertEqual(method_under_test([2, 5], [2, 5, 7]), 2)

    def test_against_naive(self):

        seq1 = list(range(10))
        seq2 = list(range(10))
        random.shuffle(seq1)
        random.shuffle(seq2)
        self.assertEqual(naive_longest_common_subsequence(
            seq1, seq2), method_under_test(seq1, seq2))
