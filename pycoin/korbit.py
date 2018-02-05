from base import *
import time

# Reference
# - https://apidocs.korbit.co.kr/


class KorbitPublic():
    """
    Restriction : API 호출 빈도 
     - Ticker 기능은 60초에 60번 호출
     - 그 외의 기능은 1초에 12번 호출
    """
    @staticmethod
    def _get_support_coins():
        """
        Korbit Public API가 지원하는 코인의 리스트를 반환
        :return: Coin Enumerator 리스트
        """
        return _ticker.keys()

    @HttpMethod.get
    def get_last_trading_price(self, coin=Coin.BTC):
        """
        최종 체결된 암호 화폐의 가격 정보
        :param coin:  Coin Class Enumerator
        :return: json type
        {
          "timestamp"   : 최종 체결 시각 timestamp
          "last"        : 최종 체결 가격
        }
        """
        time.sleep(1)
        params = {"currency_pair": _ticker[coin]}
        return HttpParam("https://api.korbit.co.kr/v1/ticker", params)

    @HttpMethod.get
    def get_last_trading_info(self, coin=Coin.BTC):
        """

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
        time.sleep(0.1)
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
        time.sleep(0.1)
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
    print(kb.get_last_trading_price(Coin.BTC))
    # Not support in v1
    #print(kb.get_last_trading_info(Coin.BTC))

    print(kb.get_order_book(Coin.BTC))
    bids = kb.get_order_book(Coin.BTC)['bids']
    for bid in bids:
        print (bid)
