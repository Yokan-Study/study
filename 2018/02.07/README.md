# 2018.02.07

## Gapi
http://gapi.gabia.com/apiexplorer#none

### Host
```
https://gapi.gabia.com
```

### Sample
공통 API - 주소 검색 - 시도
```
GET /roadcode HTTP/1.1
Host: gapi.gabia.com
Authorization: Basic 
Cache-Control: no-cache
```

```python
import requests
headers = {'Authorization': 'Basic {KEY}'}
r = requests.get('https://gapi.gabia.com/roadcode', headers=headers)
```

