from enum import IntEnum
import requests


class HttpParam :
    def __init__(self, url, headers=None, payloads=None):
        self.url = url
        self.headers = headers
        self.payloads = payloads

    @staticmethod
    def get(func):
        def decorator(*args, **kwargs):
            param = func(*args, **kwargs)
            resp = requests.get(url=param.url, headers=param.headers, data=param.payloads)
            return resp.json()
        return decorator

    @staticmethod
    def post(func):
        def decorator(*args, **kwargs):
            param = func(*args, **kwargs)
            resp = requests.get(url=param.url, headers=param.headers, data=param.payloads)
            return resp.json()
        return decorator


class CoinApi:
    def get_ticker(self):
        # must be overridden in subclass
        raise NotImplementedError

    def get_price(self, currency):
        # must be overridden in subclass
        raise NotImplementedError

    def buy(self, currency, price, volume):
        # must be overridden in subclass
        raise NotImplementedError

    def sell(self, currency, price, volume):
        # must be overridden in subclass
        raise NotImplementedError

    def cancel(self, currency, price, volume):
        # must be overridden in subclass
        raise NotImplementedError

    def status(self, order_id):
        # must be overridden in subclass
        raise NotImplementedError

    def history(self, currency, price, volume):
        # must be overridden in subclass
        raise NotImplementedError


class Coin(IntEnum):
    BTC = 0
    ETH = 1
    DASH = 2
    LTC = 3
    ETC = 4
    XRP = 5
    BCH = 6
    XMR = 7
    ZEC = 8
    QTUM = 9
    BTG = 10
    EOS = 11
globals().update(Coin.__members__)