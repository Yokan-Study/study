#한 줄로 요약
#: VOC 서비스 개선 건에 도메인사업팀을 작업자로 지정하여 올라온 건에 대해 이메일로 자동 발송되는 프로세스

#필요 기능/조건
#1) 서비스 개선 건에 대해 하루 2번(오전 8시, 오후 3시) 주기로 get 요청 한다. 
#2)<row id=""> 기준으로 신규 건이 접수되었는지 확인 
#2) 검색 조건에서 서비스 = 도메인, 상태 = 접수 or 확인중 인 건만 추출한다 
#3) 2)에 해당하는 건 중에서 작업자가 '이영숙'으로 지정된 건이 있을 경우 kmk@gabia.com으로 발송한다.
#4) 2)와 3)에 해당하는 조건이 없을 경우, index를 업데이트 한 후 프로세스 종료 

#데이터 가져오는 곳 
#http://admin2.gabia.com/voc/improve/getData/service_imp_list_data.php?orderBy=0&direction=des&period=im.request_date&start=2017-11-30&end=2018-05-30&search_item=im.subject&search_txt=

#궁금증
#메일 발송하는데 메일 서버 이런거 고려안해도 되는지? 발송이 그렇게 쉬운건지..? 
