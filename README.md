# Crawling-Parsing practice
### Crawling 및 Parsing 실습에 도움이 되는 Library
- Requset Library
- Beautifulsoup Library
- Pyautogui Library
- Openpyxl Library


## 1. Requests Library
> HTTP 통신을 위한 Crawling 파이썬 라이브러리

  ```python
  pip install requests
   ```

> 호출
```python
import requests
```

> 예제
```python
response = requests.get("https://www.naver.com")    // 서버로부터 HTML 요청
html = response.text
print(html)
```

## 2. Beautifulsoup Library
> HTML 분석을 위한 Parsing 파이썬 라이브러리

```python
pip install beautifulsoup4
```

> 호출
```python
from bs4 import beautifulsoup
```

> 예제
```python
soup = BeautifulSoup(html,'html.parser')     // Requests Libaray로 받아온 HTML 파일 'html.parser'을 이용하여 Parsing
word = soup.select_one("#id")                // Parsing된 HTML 파일에서 선택자를 활용해 원하는 Tag 추출
print (word.text)                            // Tag 갖은 text 내용 print 
print (word.attrs['href'] )                  // Tag 갖은 href 속성값 print  
```

## 3. Pyautogui Library
> 마우스와 키보드로 입력을 받을 수 있는 간단한 입력 창 라이브러리 (간단한 입력 창 띄우기)

```python
pip install pyautogui
```

> 호출
```python
import pyautogui
```

> 예제
```python
pyautogui.prompt("검색어를 입력하세요")      // 간단한 입력창 Prompt 호출
```

## 4. Openpyxl Library
> 엑셀 활용 라이브러리

```python
pip install openpyxl
```

> 호출
```python
import pyautogui
```

> 예제 - 엑셀 저장
```python
#openpyxl 라이브러리 불러오기
import openpyxl

#엑셀 만들기
workbook = openpyxl.Workbook()

#엑셀 워크시트 만들기
worksheet = workbook.create_sheet('관심 종목')

#데이터 추가(입력)하기
worksheet['A1'] = '종목명'
worksheet['B1'] = '현재 가격'
worksheet['A2'] = '삼성전자'
worksheet['B2'] = 10000
worksheet['A3'] = '현대차'
worksheet['B3'] = 5000

#엑셀 저장하기
workbook.save('/concept/Stock_data.xlsx')
```

> 예제 - 엑셀 호출
```
#openpyxl 라이브러리 불러오기
import openpyxl

#엑셀 불러오기
workbook = openpyxl.load_workbook('Stock_data.xlsx')

#엑셀 시트 불러오기
worksheet = workbook['관심 종목']
#만약 현재 활성화 되어있는 시트를 불러올 때 worksheet = workbook.active

#데이터 수정하기
worksheet['A4'] = '네이버'
worksheet['B4'] = '8000'

#엑셀 저장하기
workbook.save('Stock_data.xlsx')
```