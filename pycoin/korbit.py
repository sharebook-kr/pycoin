from base import *
import time

# Reference
# - https://apidocs.korbit.co.kr/


class KorbitPublic(CoinPublicApi):
    """
    Korbit Public API
     - Restriction : Ticker 기능은 60초에 60번 / 그 외의 기능은 1초에 12번 호출
    """
    def __init__(self):
        self.korbit = _KorbitPublic()

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
        response = self.korbit.get_transactions(coin=coin)
        return [(int(x['price']), float(x['amount']), int(x['price']) * float(x['amount'])) for x in response[:count]]


class _KorbitPublic():
    @HttpMethod.get
    def get_transactions(self, coin=Coin.BTC):
        """
        거래소 거래 체결 완료 내역s
        :param coin: Coin Class Enumerator        
        :return: 
        """
        params = {"currency_pair": _ticker[coin]}
        return HttpParam("https://api.korbit.co.kr/v1/transactions", params)

    @HttpMethod.get
    def get_last_price(self, coin=Coin.BTC):
        """
        최종 체결된 암호 화폐의 가격 정보
        :param coin:  Coin Class Enumerator
        :return: json type
        {
          "timestamp"   : 최종 체결 시각 timestamp
          "last"        : 최종 체결 가격
        }
        """
        params = {"currency_pair": _ticker[coin]}
        return HttpParam("https://api.korbit.co.kr/v1/ticker", params)

    @HttpMethod.get
    def get_detailed(self, coin=Coin.BTC):
        """
        시장 현황 상세정보를 반환한다.
        :param coin:  Coin Class Enumerator
        :return: json type
        {
          "timestamp"   : 최종 체결 시각
          "last"        : 최종 체결 가격
          "bid"         : 최우선 매수호가
          "ask"         : 최우선 매도호가
          "low"         : 최근 24시간 동안의 체결 가격 중 가장 낮 가격
          "high"        : 최근 24시간 동안의 체결 가격 중 가장 높은 가격
          "volume"      : 거래량
        }
        """
        params = {"currency_pair": _ticker[coin]}
        return HttpParam("https://api.korbit.co.kr/v1/detailed", params)

    @HttpMethod.get
    def get_order_book(self, coin=Coin.BTC):
        """
        매수/매도 호가 정보
        :param coin:  Coin Class Enumerator
        :return: json type
        {
          " timestamp"   : 최종 체결 시각          
            "ask"         : [
                [[가격, 미체결잔량, 1],...]
            ]
            "bid"         : [
                [[가격, 미체결잔량, 1],...]
            ]
        }
        """
        params = {"currency_pair": _ticker[coin]}
        return HttpParam("https://api.korbit.co.kr/v1/orderbook", params)

_ticker = {
    Coin.BTC: "btc_krw",
    Coin.BCH: "bch_krw",
    Coin.ETH: "etc_krw",
    Coin.ETC: "etc_krw",
    Coin.XRP: "xrp_krw"
}


if __name__ == "__main__":
    kb = KorbitPublic()
    print(kb.get_prices(Coin.BTC))
    print(kb.get_prices(Coin.BTC, count=2))

