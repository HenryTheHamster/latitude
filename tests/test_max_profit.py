import unittest
from max_profit import max_profit

class TestMaxProfit(unittest.TestCase):
    def test_exceptions(self):
        """
        Test that raises an exception with insufficient data
        """
        data = [1]
        self.assertRaises(Exception, max_profit, data)

    def test_max_profit_simple(self):
        """
        Test that it works with the bare minimum data
        """
        data = [1, 100]
        result = max_profit(data)
        self.assertEqual(result, 99)

    def test_max_profit_complex(self):
        """
        Test that it works on the sample data
        """
        data = [10, 7, 5, 8, 11, 9]
        result = max_profit(data)
        self.assertEqual(result, 6)

    def test_max_profit_none(self):
        """
        Test that it works when no profit opportunity exists
        """
        data = [10, 5]
        result = max_profit(data)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
