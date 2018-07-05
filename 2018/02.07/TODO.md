## Before

1. 회원 API - 회원 상세정보
    1. 1명의 회원 이름 정보 가져오는 함수 getMember() 만들기
        - return 한글이름 `hanadmin`(string)
    1. 리스트로 넘어온 user_id를 이용해 여러명의 이름 정보 가져와서 리스트로 만들어주는 getMembers() 만들기
        - return 한글이름 리스트(list)
        - e.g.)
            ```python
            def getMember(user_id):
                # ...
                return 'hanadmin'

            def getMembers(user_ids):
                # ...
                # hint: call  getMember()
                return []

            members = getMembers(['ryan0425', 'planning_d'])
            ```
    1. `/python/{name}.members.py` 로 저장


