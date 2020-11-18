import unittest


# def optimal_weight(capacity, weights):
#     dp = [[0 for _ in weights] for _ in weights]
#     w_len = len(weights)
#     for w1 in range(w_len):
#         for w2 in range(w_len):
#             if w1 == w2:
#                 dp[w1][w2] = 0
#             elif (w1 == 0 or w2 == 0) and weights[w1] + weights[w2] <= capacity:
#                 dp[w1][w2] = weights[w1] + weights[w2]
#     return dp
def optimal_weight(capacity, weight):
    dp=[]
    w_len = len(weight)
    for w1 in range(w_len):
        
        

method_under_test = optimal_weight

class OptimalWeight(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(method_under_test(10, [1, 4, 8]), 9)
