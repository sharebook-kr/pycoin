import unittest
import random
import time
from pycoin.korbit import *


class KorbitPulicTest(unittest.TestCase):
    def setUp(self):
        self.korbit = KorbitPublic()

    def test_get_price(self):
        for coin in self.korbit.get_support_coins():
            count = random.randrange(1, 6)
            result = self.korbit.get_prices(coin, count)
            print(coin, count, result)
            self.assertTrue(len(result) == count)
            time.sleep(0.1)

if __name__ == '__main__':
    unittest.main()