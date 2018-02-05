import unittest
from pycoin.korbit import *


class KorbitPulicTest(unittest.TestCase):
    def setUp(self):
        self.korbit = KorbitPublic()

    def test_get_last_trading(self):
        for coin in self.korbit._get_support_coins():
            result = self.korbit.get_last_trading_price(coin)
            self.assertTrue('timestamp' in result)
            self.assertTrue('last' in result)

    def test_get_order_book(self):
        for coin in self.korbit._get_support_coins():
            result = self.korbit.get_order_book(coin)
            self.assertTrue('timestamp' in result)
            self.assertTrue('bids' in result)
            self.assertTrue('asks' in result)
if __name__ == '__main__':
    unittest.main()