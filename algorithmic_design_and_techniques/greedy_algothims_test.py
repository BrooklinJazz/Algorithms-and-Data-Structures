import unittest
import random
from greedy_algorithms import is_greater_digit, maximize_salary, optimal_summands, collect_signatures_from_string, has_disjointed, money_change, maximum_loot, maximum_advertising_revenue, collect_signatures, number_of_overlapping


class MoneyChange(unittest.TestCase):

    def test_simple_cases(self):
        self.assertEqual(money_change(2), 2)
        self.assertEqual(money_change(10), 1)
        self.assertEqual(money_change(30), 3)


class MaximumLoot(unittest.TestCase):

    def test_simple_case(self):
        result = maximum_loot(
            [3, 50, 60, 20, 100, 50, 120, 30])
        self.assertEquals(result, 180.0000)


class MaxAdvertisingRevenue(unittest.TestCase):
    def test_array_length_1(self):
        slots = 1
        profit_per_click = [23]
        clicks_per_day = [39]
        result = maximum_advertising_revenue(
            slots, profit_per_click, clicks_per_day)
        self.assertEquals(result, 897)

    def test_array_length_3(self):
        slots = 3
        profit_per_click = [1, 3, -5]
        clicks_per_day = [-2, 4, 1]
        result = maximum_advertising_revenue(
            slots, profit_per_click, clicks_per_day)
        self.assertEquals(result, 23)


class CollectingSignatures(unittest.TestCase):
    def test_list_with_single_result(self):
        segments = [[1, 3], [2, 5], [3, 6]]
        self.assertEqual(collect_signatures(segments), [3])

    def test_list_with_two_results(self):
        segments = [[4, 7], [1, 3], [2, 5], [5, 6]]
        self.assertEquals(collect_signatures(segments), [3, 6])

    def test_single_segment(self):
        self.assertEquals(collect_signatures([[4, 7]]), [7])

    def test_single_segment_same_values(self):
        self.assertEquals(collect_signatures([[3, 3]]), [3])

    def test_large_data(self):
        large_data = []
        for i in range(100):
            large_data.append([random.randint(0, 100), 10 ** 9])
        self.assertEquals(collect_signatures(large_data), [10 ** 9])

    def test_string_input(self):
        self.assertEquals(collect_signatures_from_string(
            "3 1 3 2 5 3 6"), [3])

    def test_has_disjointed(self):
        segments = [[4, 7], [1, 3], [2, 5], [5, 6]]
        self.assertTrue(has_disjointed([2], segments))
        self.assertTrue(has_disjointed([7, 3], segments))
        self.assertFalse(has_disjointed([3, 6], segments))


class MaximumNumberOfPrizes(unittest.TestCase):
    def test_case_1(self):
        self.assertEquals(optimal_summands(6), [1, 2, 3])

    def test_case_2(self):
        self.assertEquals(optimal_summands(8), [1, 2, 5])

    def test_case_3(self):
        self.assertEquals(optimal_summands(2), [2])


class MaximumSalary(unittest.TestCase):
    def test_greater_digit(self):
        self.assertTrue(is_greater_digit("999", "998"))
        self.assertTrue(is_greater_digit("999", "989"))
        self.assertTrue(is_greater_digit("999", "9997"))
        self.assertTrue(is_greater_digit("798", "777"))
        self.assertTrue(is_greater_digit("9", "99"))
        self.assertTrue(is_greater_digit("2", "21"))

    def test_stress_greater_digit(self):
        for i in range(100000):
            a = random.randint(0, 100000)
            b = random.randint(0, 100000)
            a = "99999" + str(a)
            b = "99998" + str(b)
            self.assertTrue(is_greater_digit(int(a), int(b)),
                            msg=f'failed with {a} and {b}')

    def test_case_1(self):
        self.assertEquals(maximize_salary(["21", "2"]), 221)

    def test_case_2(self):
        self.assertEquals(maximize_salary(["9", "4", "6", "1", "9"]), 99641)

    def test_case_3(self):
        self.assertEquals(maximize_salary(["222", "212"]), 222212)
        self.assertEquals(maximize_salary(["212", "222"]), 222212)

    def test_against_strings(self):
        self.assertEquals(maximize_salary(["222", "212"]), 222212)
        self.assertEquals(maximize_salary(["212", "222"]), 222212)

    def test_large_dataset(self):
        arr = list(map(str, range(0, 1000)))
        self.assertEquals(str(maximize_salary(arr))[0:12], "999998997996")


if __name__ == '__main__':
    unittest.main()
