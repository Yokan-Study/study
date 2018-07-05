## Before

1. git-it 
    - https://github.com/jlord/git-it
    - [Web Version](http://jlord.us/git-it/challenges/get_git.html)
    - [App Download](https://github.com/jlord/git-it-electron/releases)
    - git-it을 설치하고 모든 과정을 완료
    - 중간에 어려워 보이거나 헷갈릴 수 있는 부분은 따로 [Wiki](https://github.com/Yokan-Study/study/wiki/git-it)에 설명해 둠
    - 최종으로 `./git-it/lsh-git-it.md` 형식으로 캡쳐본을 작성해서 올릴 것
1. What do you want
    - Python으로 만들고 싶은 프로그램 생각하기
    - @mksweetlife의 요구사항은 불가
        - KISA 시스템이 웹 스크래핑 하기 어려운 구조
        - 만약 하더라도 KISA의 정보 보안 정책에 위배될 가능성이 큼
    - Recommend
        - 엑셀 처리
            1. 결제 정보 가져와서 엑셀로 만들기
            1. 엑셀 데이터 불러와서 POST 요청하기
        - 데이터 크롤링
            1. 결제 정보 html 긁어서 보여주기
        - Bot
            1. 새 글 등록시 `텔레그램`, `슬랙`으로 알려주기