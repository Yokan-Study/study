# 2018.02.13

## base64
https://ko.wikipedia.org/wiki/%EB%B2%A0%EC%9D%B4%EC%8A%A464

```javascript
btoa('lsh') 
atob('bHNo')
```

### python base64
https://docs.python.org/3.5/library/base64.html

---

## <목표>
```
62번 템플릿을 이용하여 수동 메일 발송하기
```

## <요구 사항 분석>

1. 메일 발송을 위해 필요한 정보

	- 회원 이름 - {hanname}
	- 작성일 - {regist_date}
	- 서비스명 - {service_name}
	- 도메인 - {domain}
	- 만기일 - {expiration_date}
	- 기준 금액 - {extension_expense}
	- 연장 가능 기한 - {extendable_limit}
	- 총 서비스 건수 - {total_count}


2. 필수 입력 정보

	- [회원 ID] → 회원 이름 
	- [서비스 번호] → 서비스명, 도메인, 만기일, 기준 금액


3. 자동 입력 정보

	- 작성일
	- 연장 가능 기한
	- 총 서비스 건 수



## <순서>

① 메일 템플릿 API를 통해 62번 템플릿을 불러온다

② 입력받은 회원 ID, 서비스 번호를 기준으로 1), 3), 4), 5), 6)번 정보를 조회한다

③ 각 변수 위치에 넣어준다

④ 2), 7), 8)은 자동으로 입력 또는 카운트되게 처리한다

⑤ 메일 발송 API를 통해 메일을 보낸다
