import requests

r = requests.get('https://api.coinone.co.kr/ticker?currency={}.format(type)')
j = r.json()

coin = j["currency"]
last = j["last"]

coin_modu = [btc, bch, eth, etc, xrp, qtum, iota, ltc, btg, all]

def getLastPrice(coin):
    if coin not in coin_modu: 
        return false

    else: 
        print ("최종 가격: ", last)
