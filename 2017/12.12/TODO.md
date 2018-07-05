## Before

1. [Requests](http://docs.python-requests.org/en/master) 문서 내용 읽고 다음 요구사항을 만족하는 코드를 작성
    - Github 사용자 정보 가져오기
    - https://developer.github.com/v3/users/#get-a-single-user
        - 해당 API 문서를 읽고 처음부터 하는 게 정석, 그러나 api 호스트는 미리 알려주겠음
        - https://api.github.com
        - 즉, GET https://api.github.com/users/sanghaklee
    - 함수 `getUser` 만들기
        - 함수의 인자값은 `문자열` 자료형 1개
        - 함수의 출력값은 `문자열` 자료형, `/users/:username`의 결과 값에서 이름(`'name'`)과 블로그(`'blog`') 정보를 `/` 로 나눠서 리턴한다.
        - **만약** 이름(`'name'`) 정보가 존재하지 않는다면, login 정보로 대체
        - **만약** 블로그(`'blog'`) 정보가 존재하지 않는다면, html_url 정보로 대체
            - 블로그 있는 경우 결과값:
                - "Sanghak,Lee / http://sanghaklee.tistory.com"
            - 블로그 없는 경우 결과값:
                - "Sanghak,Lee / https://github.com/SangHakLee"
    - **Hint:**
        1. install requests package
        1. get requests package `JSON Response Content`
