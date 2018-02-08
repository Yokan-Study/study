import requests

r = requests.get('https://api.coinone.co.kr/ticker?currency={}.format(type)') # 포맷 함수로 코인 타입 변수화 
j = r.json() # 코인 티커 정보를 json 형태로 출력

type = j["currency"] #여기 맞는지 모르겠음... 
coin = j["currency"] #coin은 코인 타입 
last = j["last"] #last는 해당 코인의 최종 가격

coin_modu = ["btc", "bch", "eth", "etc", "xrp", "qtum", "iota", "ltc", "btg", "all"] #취급하는 코인 리스트 
def getLastPrice(coin): #코인의 최종 가격 데이터 불러오기
    if coin not in coin_modu: #코인 리스트 상에 해당 코인 타입이 없으면 false 리턴 
        return false
    else:
        print ("최종 가격: ", last)
