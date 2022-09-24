import requests
from bs4 import BeautifulSoup

key = input("검색어를 입력하세요>>>")
# url(protocol+domain+path+parameter) 에서 parameter중 query=값이 검색어이다.
response = requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query="+key)

html = response.text
soup = BeautifulSoup(html, 'html.parser')

lists = soup.select('.news_tit')
for list in lists:
    title = list.text
    print(title)