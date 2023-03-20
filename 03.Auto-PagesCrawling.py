import requests
from bs4 import BeautifulSoup
import pyautogui


key = pyautogui.prompt("검색어를 입력하세요>>>")
pageNum = 1
# 첫번째 페이지 start=1
# 두번째 페이지 start=11
# 세번째 페이지 start=21
# 열번째 페이지 start=91
# i 값 1부터 100까지 10간격으로 대입

for i in range(1,30,10):   
    print(f'{pageNum}번째 페이지 입니다.')  
    response = requests.get(f"https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query={key}&start={i}")

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    lists = soup.select('.news_tit')
    for list in lists:
        title = list.text
        print(title)

    pageNum = pageNum + 1