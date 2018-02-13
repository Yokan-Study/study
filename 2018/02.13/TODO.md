## Before
1. base64 인코딩 활용한 gapi 사용 함수 만들기
    - `/2018/02.07/python/jya.token.py`에서 받아온 토큰은 바로 쓸 수 없고 postman을 통해서 `Authorization` 정보를 만들어줘야 했다.
    - 이제 Authorization: basic {KEY} 에서 `KEY`어떻게 만들어는지 알았기 때문에 이 부분도 코드로 만들어 본다.
    1. getToken() 함수 만들기
        - POST /oauth/token 로 요청
        - 파라미터 없음 함수 내부에서 data 변수 하드코딩
        - return **`access_token`(String)**
        ```python
        def getToken():
            # ...
            # ...
            return 'token'    
        ```
    1. makeHeadersAuth() 함수 만들기
        - 파라미터 **`token`(String)**
        - return **`auth`(String or Dict)** 
        ```python
        def makeHeadersAuth(token):
            # ...
            # ...
            return 'Basic {KEY}' # or {'Authorization': 'Basic {key}'}
        ```