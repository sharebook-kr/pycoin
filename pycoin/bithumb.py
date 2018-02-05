from base import *


class Bithumb(CoinApi):
    @HttpParam.get
    def _get_price(self, coin):
        ticker = self._to_ticker[coin]
        return HttpParam("https://api.bithumb.com/public/ticker/" + ticker)

    def get_price(self, coin):
        resp = self._get_price(coin)
        return resp['data']['closing_price']

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
    b = Bithumb()
    print(b.get_price(Coin.BTC))
