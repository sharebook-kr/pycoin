from base import *


class UpbitPublic(CoinPublicApi):
    """
    Upbit Public API
     - Restriction : 없으나 도의적으로 초당 10회로 제한
    """
    def __init__(self):
        self.upbit = _UpbitPublic()

    def get_support_coins(self):
        """
        지원하는 Coin의 Enum List를 반환한다. 
        :return: Coin의 Enum List (예:[Coin.BTC, Coin.ETH, Coin.XRP]
        """
        return _ticker.keys()

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
        if date is not None :
            # Korbit 공개 API는 특정 일자의 가격 정보 조회 기능을 지원하지 않음
            raise NotImplementedError
        response = self.upbit.get_price(coin, count, market, date)
        return [(int(x['tradePrice']), None, None) for x in response[:count]]


class _UpbitPublic():
    @HttpMethod.get
    def get_price(self, coin=Coin.BTC, count=1, market=Market.KRW, date=None):
        """
        체결된 코인의 가격 정보 리스트
        :param coin: 
        :param count: 
        :param market: 
        :param date: 
        :return: 
        """
        headers = {"User-Agent": "HACK"}
        url = 'https://crix-api-endpoint.upbit.com/v1/crix/candles/weeks?code=CRIX.UPBIT.{0}-{1}'.format(
            _market[Market.KRW], _ticker[Coin.BTC])
        data = "count=" + str(count)
        return HttpParam(url=url, headers=headers, data=data)

_market = {
    Market.KRW: "KRW",
    Market.BTC: "BTC",
    Market.ETH: "ETH",
    Market.USDT: "USDT"
}

_ticker = {
    Coin.BTC: "BTC",
    Coin.BCH: "BCH",
    Coin.ETH: "ETH",
    Coin.ETC: "ETC",
    Coin.XRP: "XRP"
}


if __name__ == "__main__":
    ub = UpbitPublic()
    print(ub.get_prices(Coin.BTC, 1))
    print(ub.get_prices(Coin.BTC, 1))


