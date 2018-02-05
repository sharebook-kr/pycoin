from abc import ABC, abstractmethod
from enum import IntEnum
import requests


class HttpMethod:
    def __init__(self):
        raise AttributeError

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


class HttpParam:
    def __init__(self, url, headers=None, payloads=None):
        self.url = url
        self.headers = headers
        self.payloads = payloads


class CoinApi(ABC):
    @abstractmethod
    def get_ticker(self):
        """               
        :return: 지원하는 Coin class의 Enum 리스트 [Coin.BTC, Coin.ETH]
        """
        pass

    @abstractmethod
    def get_price(self, coin):
        """                        
        :param coin: Coin Class의 Enum type
        :return: Coin의 최근 체결가를 반환
        """
        pass

    @abstractmethod
    def buy(self, coin, price, volume):
        """  

        :param coin: 
        :param price: 
        :param volume: 
        :return: 
        """
        pass

    @abstractmethod
    def sell(self, coin, price, volume):
        """

        :param coin: 
        :param price: 
        :param volume: 
        :return: 
        """
        pass

    @abstractmethod
    def cancel(self, coin, price, volume):
        """

        :param coin: 
        :param price: 
        :param volume: 
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