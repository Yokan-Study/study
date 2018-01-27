# 2018.01.23

Ok~ 간만에 찾아뵙게 됐는데

## RESTful API
[REST API 제대로 알고 사용하기](http://meetup.toast.com/posts/92)

### RESTful API Docs
1. API 문서를 정독한다. (아직 API 문서가 익숙하지 않은 경우)
1. Host
1. 특정 API 분석
1. API 요청

#### Host
호스트, 즉 API의 주소를 찾아야 한다.
https://developers.kakao.com/docs/restapi/quick-reference

보통 기업의 API 주소는 `www.gabia.com`인 경우 `api.gabia.com`으로 명명한다.

#### API 분석
https://developers.kakao.com/docs/restapi/kakaotalk-api

API 문서의 기본적은 포맷은 아래와 같다.
- Host
- Request Parameter
- Response Parameter

대부분의 API 문서가 Request Sample을 `HTTP` 포맷으로 제공한다.

**가장 기본적인 요청 형태:**
```http
{Method} {Api url} {Http version}
HOST: {Host}
```

**가장 기본적인 요청 형태의 예시:**
```http
GET /v1/api/talk/profile HTTP/1.1
Host: kapi.kakao.com
```

위의 요청은 브라우저에서 `kapi.kakao.com/v1/api/talk/profile`를 입력한 것과 동일하다.

왜냐하면, HTTP 요청이 GET이기 때문에 브라우저에 해당 주소를 입력하면 GET 요청을 한 것과 동일한 작동을 하기 때문이다.

그러나, 해당 주소를 입력하면 `404(Not Found)`가 나온다. 

해당 API는 사실 HTTP 요청시 `Authorization`에 자신을 인증하는 키가 필요한데 우리는 보내지 않았다. 그렇기 때문에 제대로 된 결과를 받을 수 없었다.

`Authorization` 값은 HTTP 헤더에 입력해야 하는데 브라우저에선 그냥 할 수 없고 코드나 포스트맨을 통해서 가능하다.

개인적으론 404보단 401이 더 알맞는 에러 코드라 생각한다.
만약! `/v1/api/talk/{username}/profile`이라면 404가 맞다고 생각한다.
그러나 `/v1/api/talk/profile`은 그 자체로 완벽한 주소이고 Authorization이 없는 401 상태이기 때문에 401이 더 알맞다고 생각한다.


#### API 요청
위의 카카오 API는 인증되지 않은 사용자는 어떤 API도 테스트 해볼 수 없다.

지난번 실습과제인 [Github API](https://developer.github.com/v3/users/)를 다시 보자

[Get a single user](https://developer.github.com/v3/users/#get-a-single-user)

위의 API 문서를 통해 `sanghaklee` 계정의 정보를 가져오는 API 주소를 만들어서 PR!
- 양아: '이 내용 지우고 주소 PR'
- 민경: GET api.github.com/users/sanghaklee

아래의 내용을 다시 읽어보고 작업할 것

1. API 문서를 정독한다. (아직 API 문서가 익숙하지 않은 경우)
1. Host
1. 특정 API 분석


## Requests
http://docs.python-requests.org/en/master/




