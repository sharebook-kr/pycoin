from abc import ABC, abstractmethod, abstractproperty
from enum import IntEnum
import requests


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


class Market(IntEnum):
    KRW = 0
    BTC = 1
    ETH = 2
    USDT = 3


class HttpMethod:
    def __init__(self):
        raise AttributeError

    @staticmethod
    def get(func):
        def decorator(*args, **kwargs):
            param = func(*args, **kwargs)
            resp = requests.get(url=param.url, headers=param.headers, params=param.data)
            return resp.json()
        return decorator

    @staticmethod
    def post(func):
        def decorator(*args, **kwargs):
            param = func(*args, **kwargs)
            resp = requests.get(url=param.url, headers=param.headers, data=param.data)
            return resp.json()
        return decorator


class HttpParam:
    def __init__(self, url, headers=None, data=None):
        self.url = url
        self.headers = headers
        self.data = data


class CoinPublicApi(ABC):
    @property
    @abstractmethod
    def get_support_coins(self):
        """
        지원하는 Coin의 Enum List를 반환한다. 
        :return: Coin의 Enum List (예:[Coin.BTC, Coin.ETH, Coin.XRP]
        """
        pass

    @abstractmethod
    def get_prices(self, coin=Coin.BTC, count=1, market=Market.KRW, date=None):
        """
        코인의 거래 정보 리스트를 반환한다.
        :param coin: 조회할 코인의 Enum type 
        :param count: 조회할 가격 정보의 개수
        :param market: 결제 화폐 
        :param date: 문자열 형태의 일자 (예:19/02/2018)
        :return: count 개수의 거래 정보가 저장된 리스트
                 [(거래단가, 거래수량, 거래금액), (...), ...]
        """
        pass

    def get_increase_ratio(self, coin=Coin.BTC, market=Market.KRW, start=None, end=None):
        """
        특정 코인의 가격 상승률을 반환한다.
        :param coin:
        :param market:
        :param start: 문자열 형태의 시작 일자 (예:18/02/2018)
        :param end: 문자열 형태의 끝 일자 (예:19/02/2018)
        :return: 지수 상승률을 반환
        """
        price_start = self.get_prices(coin, market, 1, start)
        price_end   = self.get_prices(coin, market, 1, end)
        return (price_end - price_start) / price_start


class CoinPrivateApi(ABC):
    @abstractmethod
    def get_price(self, coin=Coin.BTC, market=Market.KRW, count=1, start=None, end=None):
        """
        :param coin: Coin Class의 Enum type
        :param market: Market Class의 Enum type
        :param count: 조회 할 거래 수
        :param start: Starting date (defaults to today)
        :param end: Ending  date (defaults to today)
        :return: Coin의 최근 체결가를 반환
        """
        pass

    @abstractmethod
    def buy(self, price, volume, coin=Coin.BTC, market=Market.KRW):
        """
        :param price:
        :param volume:
        :param coin:
        :param market:
        :return:
        """
        pass

    @abstractmethod
    def sell(self, price, volume, coin=Coin.BTC, market=Market.KRW):
        """
        :param price:
        :param volume:
        :param coin:
        :param market:
        :return: 
        """
        pass

    @abstractmethod
    def cancel(self, order_id):
        """
        :param order_id:
        :return: 
        """
        pass

    @abstractmethod
    def status(self, order_id):
        """
        :param order_id: 
        :return: 
        """
        pass

    @abstractmethod
    def history(self, coin, price, volume):
        """

        :param coin: 
        :param price: 
        :param volume: 
        :return: 
        """
        pass


if __name__ == '__main__':
    print(Coin.BTC)