from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws['A1'] = 'Minkyeong Kim'

wb.save('../datas/kmk-save.xlsx')