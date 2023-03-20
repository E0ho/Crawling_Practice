import requests

# BeautifulSoup(html 분석 파이썬 라이브러리) 라이브러리 파일로 불러오기
from bs4 import BeautifulSoup

response = requests.get("https://www.naver.com")
html = response.text

# 받아온 html 코드를 'html.parser'를 이용하여 soup로 분리
soup = BeautifulSoup(html,'html.parser')

# parsing 된 soup에서 원하는 정보 word에 저장
word = soup.select_one('#NM_set_home_btn')
print(word)