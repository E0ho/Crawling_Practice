import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.naver.com/")
response_html = response.text

soup = BeautifulSoup(response_html, "html.parser")
news_title = soup.select(".cjs_t")
news_link = soup.select(".cjs_news_a")

print(len(news_title))
print(len(news_link))

for i in range(len(news_title)):
    print(f"{i+1}번째 기사 제목:{news_title[i].text}")
    print(f"{i+1}번째 기사 URL:{news_link[i].attrs['href']}")
    print()
    