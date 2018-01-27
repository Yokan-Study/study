from openpyxl import workbook

wb = workbook()
ws = wb.active

ws['A1'] = 'jya9055'

wb.save('../datas/jya-save.xlsx') 

