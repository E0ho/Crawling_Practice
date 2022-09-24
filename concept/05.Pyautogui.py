import requests
from bs4 import BeautifulSoup

#pyautogui 라이브러리 불러오기
import pyautogui

# pyautogui.prompt로 입력받은 값은 무조건 string 형태이다. 정수로 사용하고 싶다면 형변환이 필요하다.
key = pyautogui.prompt("검색어를 입력하세요>>>")
# f {변수} 함수로 ("string" + 변수) 대체가능
response = requests.get(f"https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query={key}")

html = response.text
soup = BeautifulSoup(html, 'html.parser')

lists = soup.select('.news_tit')
for list in lists:
    title = list.text
    print(title)