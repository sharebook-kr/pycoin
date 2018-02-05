import unittest
from pycoin.bithumb import *


class BithumPulicTest(unittest.TestCase):
    def setUp(self):
        self.bithumb = BithumbPublic()

    def test_get_last_trading(self):
        for coin in self.bithumb._get_support_coins():
            result = self.bithumb.get_last_trading_info(coin)
            self.assertEqual(result['status'], "0000")

    def test_get_order_book(self):
        for coin in self.bithumb._get_support_coins():
            result = self.bithumb.get_order_book(coin)
            self.assertEqual(result['status'], "0000")

    def test_get_recent_transactions(self):
        for coin in self.bithumb._get_support_coins():
            result = self.bithumb.get_recent_transactions(coin)
            self.assertEqual(result['status'], "0000")

if __name__ == '__main__':
    unittest.main()