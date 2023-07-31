import requests
from bs4 import BeautifulSoup
import pyautogui
import openpyxl

workbook = openpyxl.Workbook()
worksheet = workbook.create_sheet('주식 관심종목')

key = pyautogui.prompt("관심종목 증권표준코드를 입력하세요")
#[005930, 000660, 005380, 011200, 005490]

lists = list(key.split(", "))
i = 2

for list in lists:
    response = requests.get(f"https://finance.naver.com/item/sise.naver?code={list}")
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    name = soup.select_one('.wrap_company > h2 > a').text
    price = soup.select_one('#_nowVal').text
    price = price.replace(',','')
    amount = soup.select_one('#_quant').text
    top = soup.select_one('#_high').text
    bottom = soup.select_one('#_low').text

    
    worksheet['A1'] = '종목'
    worksheet['B1'] = '현재가'
    worksheet['C1'] = '거래량'
    worksheet['D1'] = '상한가'
    worksheet['E1'] = '하한가'
    worksheet[f'A{i}'] = name
    worksheet[f'B{i}'] = price
    worksheet[f'C{i}'] = amount
    worksheet[f'D{i}'] = top
    worksheet[f'E{i}'] = bottom
    i = i+1

workbook.save('./Extra_Library/Stock_Price.xlsx')