# -*- coding: utf-8 -*-
from openpyxl import Workbook

wb = Workbook() # Workbook 생성
ws = wb.active # 현재 워크시크 가져오기

ws['A1'] = 'sanghaklee' # A1 셀에 문자 입력

wb.save('../datas/lsh-save.xlsx') # 엑셀 파일 저장