# 실시간 주가 정보 엑셀 자동화 실습

import requests
from bs4 import BeautifulSoup
import openpyxl

workbook = openpyxl.Workbook()
worksheet = workbook.create_sheet('주식 관심종목')
i = 2

lists=['005930','073490']
for list in lists:
    response = requests.get(f"https://finance.naver.com/item/sise.naver?code={list}")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    name = soup.select_one('.wrap_company > h2').text
    price = soup.select_one('#_nowVal').text
    price = price.replace(',','')

    worksheet['A1'] = '관심종목'
    worksheet['B1'] = '가격'
    worksheet[f'A{i}'] = name
    worksheet[f'B{i}'] = price
    i = i+1

workbook.save('/Practice/My_Stock_code.xlsx')