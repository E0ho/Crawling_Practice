# 주가 정보 호출 실습

import requests
from bs4 import BeautifulSoup

lists = ['005930','073490']
for list in lists:
    response = requests.get(f"https://finance.naver.com/item/sise.naver?code={list}")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

# 가져오는 정보는 모두 sting 상태 (형변환전 형변환이 불가능한 string값을 replace 메소드 사용하여 없애기)
    name = soup.select_one('.wrap_company > h2').text
    price = soup.select_one('#_nowVal').text

# replace method 이용하여 값 교체 replace('원치않는 값', '원하는 값')
    price = price.replace(',','')

    print(name ,price)