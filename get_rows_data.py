import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import requests
from bs4 import BeautifulSoup

# 웹 페이지에 접속하여 HTML 데이터 가져오기
url = 'https://www.samcheok.go.kr/specialty/00463/00990.web'
response = requests.get(url)
html = response.text

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html, 'html.parser')

# 표에서 데이터가 있는 행 요소들 선택
rows = soup.select('#body_content > div:nth-child(2) > div > table > tbody > tr')

# 데이터 추출
location_data = []
print(rows)
for row in rows:
    # 각 행에서 위치 데이터가 있는 특정 열 선택
    location_element = row.select_one('td:nth-child(2)')
    print(type(location_element))
    if location_element:
        # .get_text(strip=True)를 이용해서 텍스트 데이터를 가져오고 공백을 저거한 문자열을 변수에 할당
        location = location_element.get_text(strip=True)
        location_data.append(location)

# 결과 출력
for location in location_data:
    print(location)