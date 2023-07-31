import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.naver.com")
response_html = response.text

soup = BeautifulSoup(response_html, "html.parser")
word = soup.select_one("#query")
print(word)
