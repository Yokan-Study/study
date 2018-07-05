## Before

1. `./python/lsh-save-excel.py`
    - 해당 파일 내용 확인
    - `./python/{YOUR-NAME}-save-excel.py` 엑셀 파일 생성
    - $ python {YOUR-NAME}-save-excel.py 실행시
        - `A1` 셀에 Github id 입력
        - `./datas/{YOUR-NAME}-save.xlsx` 로 저장

1. `./python/lsh-load-excel.py`
    - 해당 파일 내용 확인
    - 2017-11-23 일일현황 내역 출력하기

1. **심화 과정**
    - `./datas/daily_gabia_20171127.xlsx` 데이터 오류
    - 2017-11-21 ~ 2017-11-27 기간의 **`환불`** 데이터가 모두 2만큼 적게 나왔다.
    - 모든 기간의 해당 데이터를 +2 만큼 해서 `./datas/daily_gabia_20171127_edit.xlsx`으로 저장할 것
    - Python 파일은 `./python/{YOUR-NAME}-edit-excel.py`로 저장할 것
