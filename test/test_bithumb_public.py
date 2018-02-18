import unittest
import random
import time
from pycoin.bithumb import *


class BithumPulicTest(unittest.TestCase):
    def setUp(self):
        self.bithumb = BithumbPublic()

    def test_get_price(self):
        for coin in self.bithumb.get_support_coins():
            count = random.randrange(1, 6)
            result = self.bithumb.get_prices(coin=coin, count=count)
            print(coin, count, result)
            self.assertTrue(len(result) == count)
            time.sleep(0.1)

if __name__ == '__main__':
    unittest.main()