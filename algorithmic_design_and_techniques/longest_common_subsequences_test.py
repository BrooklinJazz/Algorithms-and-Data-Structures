import unittest
import random


def longest_common_subsequences(a_list, b_list):
    dp = [[0 for _ in b_list] for _ in a_list]
    a_len = len(a_list)
    b_len = len(b_list)
    for a in range(a_len):
        for b in range(b_len):
            matching = a_list[a] == b_list[b]
            if a == 0:
                dp[0][b] = 1 if matching else dp[0][max(b-1, 0)]
            elif b == 0:
                dp[a][0] = 1 if matching else dp[max(a - 1, 0)][b]
            elif matching:
                dp[a][b] = 1 + dp[a - 1][b - 1]
            else:
                dp[a][b] = max(dp[a - 1][b - 1], dp[a - 1][b], dp[a][b - 1])
    return dp[a_len - 1][b_len - 1]


class LongestCommonSubsequences(unittest.TestCase):
    def test_2_matching(self):
        self.assertEqual(longest_common_subsequences([2, 5], [2, 7, 5]), 2)

    def test_0_matching(self):
        self.assertEqual(longest_common_subsequences([4], [5]), 0)

    def test_5_matching_with_repeat(self):
        self.assertEqual(longest_common_subsequences(
            [1, 2, 3, 4, 5], [1, 2, 2, 3, 4, 5]), 5)


def longest_common_three_subsequences(a_list, b_list, c_list):
    dp = [[[0 for _ in c_list]for _ in b_list]for _ in a_list]
    a_len = len(a_list)
    b_len = len(b_list)
    c_len = len(c_list)
    for a in range(a_len):
        for b in range(b_len):
            for c in range(c_len):
                matching = a_list[a] == b_list[b] == c_list[c]
                if a == 0:
                    dp[0][b][c] = 1 if matching else dp[0][max(
                        b-1, 0)][max(c - 1, 0)]
                elif b == 0:
                    dp[a][0][c] = 1 if matching else dp[max(
                        a - 1, 0)][0][max(c - 1, 0)]
                elif c == 0:
                    dp[a][b][0] = 1 if matching else dp[max(
                        a - 1, 0)][max(b-1, 0)][0]
                else:
                    dp[a][b][c] = max(
                        dp[a-1][b][c],
                        dp[a][b - 1][c],
                        dp[a][b][c - 1],
                        dp[a - 1][b - 1][c],
                        dp[a - 1][b][c - 1],
                        dp[a][b - 1][c - 1],
                        dp[a - 1][b - 1][c - 1]
                    )
                    if matching:
                        dp[a][b][c] = dp[a][b][c] + 1
    return dp[a_len - 1][b_len - 1][c_len - 1]


def lcsOf3(X, Y, Z):
    m = len(X)
    n = len(Y)
    o = len(Z)
    L = [[[0 for i in range(o+1)] for j in range(n+1)]
         for k in range(m+1)]

    ''' Following steps build L[m+1][n+1][o+1] in 
    bottom up fashion. Note that L[i][j][k] 
    contains length of LCS of X[0..i-1] and 
    Y[0..j-1] and Z[0.....k-1] '''
    for i in range(m+1):
        for j in range(n+1):
            for k in range(o+1):
                if (i == 0 or j == 0 or k == 0):
                    L[i][j][k] = 0

                elif (X[i-1] == Y[j-1] and
                      X[i-1] == Z[k-1]):
                    L[i][j][k] = L[i-1][j-1][k-1] + 1

                else:
                    L[i][j][k] = max(max(L[i-1][j][k],
                                         L[i][j-1][k]),
                                     L[i][j][k-1])

    # L[m][n][o] contains length of LCS for
    # X[0..n-1] and Y[0..m-1] and Z[0..o-1]
    return L[m][n][o]


method_under_test = longest_common_three_subsequences


class LongestThreeCommonSubsequences(unittest.TestCase):
    def test_2_matching(self):
        self.assertEqual(method_under_test(
            [1, 2, 3], [2, 1, 3], [1, 3, 5]), 2)

    def test_3_matching(self):
        self.assertEqual(method_under_test(
            [8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7], [6, 8, 3, 1, 4, 7]), 3)

    def test_against_proven(self):
        num = 50
        seq1 = list(range(num))
        seq2 = list(range(num))
        seq3 = list(range(num))
        random.shuffle(seq1)
        random.shuffle(seq2)
        random.shuffle(seq3)
        self.assertEqual(lcsOf3(seq1, seq2, seq3),
                         method_under_test(seq1, seq2, seq3))
