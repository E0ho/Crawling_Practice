import requests

response = requests.get("https://www.naver.com")
response_html = response.text
print(response_html)