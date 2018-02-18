import unittest
import time
import random
from pycoin.upbit import *


class UpbitPulicTest(unittest.TestCase):
    def setUp(self):
        self.upbit = UpbitPublic()

    def test_get_price(self):
        for coin in self.upbit.get_support_coins():
            count = random.randrange(1, 6)
            result = self.upbit.get_prices(coin, count)
            print(coin, count, result)
            self.assertTrue(len(result) == count)
            time.sleep(0.1)

if __name__ == '__main__':
    unittest.main()