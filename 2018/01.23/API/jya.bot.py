
# 함수 가져옵니다
import requests, threading
def getPrice(coin):
	A = ['btc','bch','btg','bcd','ubtc','eth','etc','ada','qtum','xlm','neo','gas','rpx','hsr','knc','tsl','tron','omg','wtc','mco','storm','gto','pxs','chat','ink','hlc','ent','qbt','spc','put']
	if coin not in A:
		return 'false'
	r = requests.get('https://api.coinnest.co.kr/api/pub/ticker/?coin={0}'.format(coin))
	j = r.json()
	last = j['last']
	return last

# 10만원 보유
money = 100000
# 가진 돈으로 구매할 수 있는 퀀텀 모두 구매 (코인 수는 정수로...)
while money:
    print("퀀텀 구매합니다")
    money = money - getPrice('qtum')
    if money < getPrice('qtum'):
        break