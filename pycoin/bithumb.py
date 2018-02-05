from base import *
import time

# 결과 상태코드 표
# 0000 정상
# 5100 Bad Request
# 5200 Not Member
# 5300 Invalid Apikey
# 5302 Method Not Allowed
# 5400 Database Fail
# 5500 Invalid Parameter
# 5600 CUSTOM NOTICE (상황별 에러 메시지 출력)
# 5900 Unknown Error

# Reference
# - https://www.bithumb.com/u1/US127


class BithumbAdapter(CoinApi):
    def sell(self, coin, price, volume):
        pass

    def history(self, coin, price, volume):
        pass

    def status(self, order_id):
        pass

    def buy(self, coin, price, volume):
        pass

    def get_ticker(self):
        pass

    def cancel(self, coin, price, volume):
        pass

    def get_price(self, coin):
        pass


class BithumbPublic:
    """
    Restriction : 1초당 20회 요청 가능
    """
    @staticmethod
    def _get_support_coins():
        """
        Korbit Public API가 지원하는 코인의 리스트를 반환
        :return: Coin Enumerator 리스트
        """
        return _ticker.keys()

    @HttpMethod.get
    def get_last_trading_info(self, coin=Coin.BTC):
        """
        거래소 마지막 거래 정보
        :param coin: Coin Class Enumerator
        :return: json type
        {
            "status": 결과 상태 코드
            "data": {
                "opening_price" : 최근 24시간 내 시작 거래금액
                "closing_price" : 최근 24시간 내 마지막 거래금액
                "min_price"     : 최근 24시간 내 최저 거래금액
                "max_price"     : 최근 24시간 내 최고 거래금액
                "average_price" : 최근 24시간 내 평균 거래금액
                "units_traded"  : 최근 24시간 내 Currency 거래량
                "volume_1day"   : 최근 1일간 Currency 거래량
                "volume_7day"   : 최근 7일간 Currency 거래량
                "buy_price"     : 거래 대기건 최고 구매가
                "sell_price"    : 거래 대기건 최소 판매가
                "date"          : 현재 시간 Timestamp
            }
        }         
        """
        time.sleep(0.1)
        return HttpParam("https://api.bithumb.com/public/ticker/" + _ticker[coin])

    @HttpMethod.get
    def get_order_book(self, coin=Coin.BTC):
        """
            매수/매도 호가 정보
            :param coin: Coin Class Enumerator
            :return: json type
            {
                "status"    : 결과 상태 코드
                "data"      : {
                    "timestamp"         : 1417142049868,
                    "order_currency"    : 주문 암호 화폐
                    "payment_currency"  : 결제 화폐 (KRW)
                    "bids": [
                        {
                            "quantity"  : 구매요청 수량 (Currency)
                            "price"     : 구매요청 단가 (기준 1 Currency) 
                        }...                     
                    ],
                    "asks": [
                        {
                            "quantity"  : 판매요청 수량 (Currency)
                            "price"     : 판매요청 단가 (기준 1 Currency) 
                        }...
                    ]
                }
            }     
            """
        time.sleep(0.1)
        return HttpParam("https://api.bithumb.com/public/orderbook/" + _ticker[coin])

    @HttpMethod.get
    def get_recent_transactions(self, coin=Coin.BTC):
        """
        거래소 거래 체결 완료 내역
        :param coin: Coin Class Enumerator
        :return: json type
        {
            "status"    : 결과 상태 코드
            "data"      : [
                {
                    "transaction_date"  : 거래 채결 시간
                    "type"              : 판/구매 (ask, bid)
                    "units_traded"      : 거래 Currency 수량
                    "price"             : 1Currency 거래 금액
                    "total"             : 총 거래금액
                }...               
            ]
        }
        """
        time.sleep(0.1)
        return HttpParam("https://api.bithumb.com/public/recent_transactions/" + _ticker[coin])


_ticker = {
    Coin.BTC: "BTC",
    Coin.ETH: "ETH",
    Coin.DASH: "DASH",
    Coin.LTC: "LTC",
    Coin.ETC: "ETC",
    Coin.XRP: "XRP",
    Coin.BCH: "BCH",
    Coin.XMR: "XMR",
    Coin.ZEC: "ZEC",
    Coin.QTUM: "QTUM",
    Coin.BTG: "BTG",
    Coin.EOS: "EOS"
}

if __name__ == "__main__":
    bp = BithumbPublic()
    print(bp.get_last_trading_info(Coin.BTC))
    print(bp.get_order_book(Coin.BTC))
    print(bp.get_recent_transactions(Coin.BTC))
