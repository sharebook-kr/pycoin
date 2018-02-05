from base import *


class Korbit(CoinApi):
    @HttpParam.get
    def _get_price(self, coin):
        params = {"currency_pair": self._to_ticker[coin]}
        return HttpParam("https://api.korbit.co.kr/v1/ticker", params)

    def get_price(self, coin=Coin.BTC):
        resp = self._get_price(coin)
        return resp['last']

    def buy(self, currency, type, price, volume):
        pass

    def sell(self, currency, type, price, volume):
        pass

    def cancel(self, currency, type, price, volume):
        pass

    def status(self, id):
        pass

    def history(self, currency, type, price, volume):
        pass

    _to_ticker = {
        Coin.BTC: "btc_krw",
        Coin.ETH: "etc_krw",
        Coin.ETC: "etc_krw",
        Coin.XRP: "xrp_krw"
    }

if __name__ == "__main__":
    kb = Korbit()
    print(kb.get_price(Coin.BTC))