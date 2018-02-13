import requests

def getPrice(coin):
	A = ['btc','bch','btg','bcd','ubtc','eth','etc','ada','qtum','xlm','neo','gas','rpx','hsr','knc','tsl','tron','omg','wtc','mco','storm','gto','pxs','chat','ink','hlc','ent','qbt','spc','put']
	if coin not in A:
		return 'false'
	r = requests.get('https://api.coinnest.co.kr/api/pub/ticker/?coin={0}'.format(coin))
	j = r.json()
	last = j['last']
	return last

# 확인해보기
a = getPrice('btc')
b = getPrice('dbc')
print(a, b)