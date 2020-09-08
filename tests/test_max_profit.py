import unittest
from max_profit import max_profit

class TestMaxProfit(unittest.TestCase):
    def test_exceptions(self):
        data = [1]
        self.assertRaises(Exception, max_profit, data)

    def test_max_profit_simple(self):
        data = [1, 100]
        result = max_profit(data)
        self.assertEqual(result, 99)

    def test_max_profit_complex(self):
        """
        Test that it can sum a list of integers
        """
        data = [10, 7, 5, 8, 11, 9]
        result = max_profit(data)
        self.assertEqual(result, 6)

    def test_max_profit_break_even(self):
        data = [10, 10]
        result = max_profit(data)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()