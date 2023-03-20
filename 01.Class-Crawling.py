# 네이버 페이지 클롤링 실습

import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.naver.com")
html = response.text

soup = BeautifulSoup(html,'html.parser')

# 여러개를 한번에 가져올 때는 List 형태로 저장
lists = soup.select('.nav_item')
for list in lists :
    text = list.text            #text값을 가져온다
    url = list.a.attrs['href']    #href 속성값을 가져온다.
    print(text, url)