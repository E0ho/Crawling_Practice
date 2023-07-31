import openpyxl

# 엑셀 생성
workbook = openpyxl.Workbook()

# 엑셀 워크시트 생성
worksheet = workbook.create_sheet('관심 종목')

# 데이터 추가(입력)하기
worksheet['A1'] = '종목명'
worksheet['B1'] = '현재 가격'
worksheet['A2'] = '삼성전자'
worksheet['B2'] = 10000
worksheet['A3'] = '현대차'
worksheet['B3'] = 5000

# 엑셀 저장하기
workbook.save('./Extra_Library/Stock_data.xlsx')