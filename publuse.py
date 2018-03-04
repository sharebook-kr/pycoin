from exchange.crypto import CryptoDaily
from util import *


def get_coin_list():
    pass


def get_price_list(since=None, limit=10, market="KRW", exchange="Bithumb", coin="BTC"):
    """
        거래소 (exchange)에서 day부터 limit 개수의 coin OHLCV를 가져온다.          
        - See. https://www.cryptocompare.com/api/#-api-data-histoday-
        :param since: 조사할 날짜 "년-월-일" 형태의 문자열. 예) 2018-03-03 
        :param limit: 조회할 데이터의 수 
        :param market: 결제 화폐
        :param exchange: 거래소 이름 예) Bithumb, Korbit, Bitfnex  
        :param coin: 코인 이름 약어
        :return: (날짜, open, high, low, close, vlume) 리스트
        """
    response = CryptoDaily.get_price_list(since, limit, market, exchange, coin)
    return [(timestamp_to_daystr(x['time']), x['open'], x['high'], x['low'], x['close'], x['volumefrom'])
            for x in response['Data']]


def get_price(market="KRW", exchange="Bithumb", coin="BTC"):
    """
    거래소 (exchange)에서 최근 거래된 coin 가격을 가져온다.                  
    - See. https://www.cryptocompare.com/api/#-api-data-price-
    :param day: 조사할 날짜 "년-월-일" 형태의 문자열. 예) 2018-03-03
    :param market: 결제 화폐
    :param exchange: 거래소 이름 예) Bithumb, Korbit, Bitfnex: 
    :param coin: 코인 이름 약어
    :return: 코인의 종가 가격
    """
    response = CryptoDaily.get_price(market, exchange, coin)
    return response[market]


# def get_inc_ratio(coin, start, last):
#     price_start = CryptoDaily.get_price(day=start, coin=coin)
#     price_last = CryptoDaily.get_price(day=last, coin=coin)
#     delta = datetime.strptime(last, "%Y-%m-%d") - datetime.strptime(start, "%Y-%m-%d")
#     return (price_last - price_start) / price_last / delta.days


if __name__ == "__main__":
    resp = get_price(market="KRW", exchange="Bithumb")
    print(resp)

    resp = get_price(market="KRW", exchange="Korbit")
    print(resp)

    resp = get_price(market="USD", exchange="Bitfinex")
    print(resp)

    resp = get_price_list(coin="BTC", since="2018-01-10")
    for v in resp:
        print(v)
