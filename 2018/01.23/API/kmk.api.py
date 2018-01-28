import requests

r = requests.get('https://api.coinone.co.kr/ticker?currency=all')
j = r.json()

coin = j["currency"]
last = j["last"]

def qtum_last_price():
    if coin == "qtum":
        print("퀀텀 최종 시세: ", last)

    else:
        return false

