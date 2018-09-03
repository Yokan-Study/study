# 오늘 작업
# 1. 마켓 플레이스에서 html snippets, html preview, auto close tag 설치 

#2. 터미널에 python3 -m http.server 8000 입력
#Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
#127.0.0.1 - - [17/Jul/2018 18:43:19] "GET / HTTP/1.1" 200 -
#127.0.0.1 - - [17/Jul/2018 18:43:20] code 404, message File not found
#127.0.0.1 - - [17/Jul/2018 18:43:20] "GET /favicon.ico HTTP/1.1" 404 -
#127.0.0.1 - - [17/Jul/2018 18:43:24] "GET /07.17/ HTTP/1.1" 200 -

#3. 80번은 http의 디폴트 port 값 
## 1~1023까지는 보통 well-known 포트라고 한다. 그래서 쓰면 안됨. 
### 포트는 0 ~ 65535 까지 열수 있다. 

#4. python3 -m SimpleHTTServer 9999
## ssh kmk@10.222.222.227

#5. netstat -tpln : 어떤 포트가 열려있는지 확인할 수 있다. 
## 8001이나 8002 사용
