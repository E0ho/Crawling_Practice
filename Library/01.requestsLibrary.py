# requests(http 통신을 위한 파이썬 라이브러리) 라이브러리 파일로 불러오기
import requests

# 특정 url 받아오기
response = requests.get("https://www.naver.com")

# 응답중 html 코드 가져오려면 .text 사용
html = response.text
print(html)