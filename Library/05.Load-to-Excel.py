#openpyxl 라이브러리 불러오기
import openpyxl

#엑셀 불러오기
workbook = openpyxl.load_workbook('Stock_data.xlsx')

#엑셀 시트 불러오기
worksheet = workbook['관심 종목']
#만약 현재 활성화 되어있는 시트를 불러올 때 worksheet = workbook.active

#데이터 수정하기
worksheet['A4'] = '네이버'
worksheet['B4'] = '8000'

#엑셀 저장하기
workbook.save('Stock_data.xlsx')