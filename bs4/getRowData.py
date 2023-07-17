import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import requests
from bs4 import BeautifulSoup

url = 'https://www.samcheok.go.kr/specialty/00463/00990.web'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
rows = soup.select('#body_content > div:nth-child(2) > div > table > tbody > tr')

row = rows[2]
location_data = [tag.get_text(strip=True) for tag in row if tag.get_text(strip=True) != ""]

# 결과 출력
cnt = 0
for lo in location_data:
        cnt += 1
        print(f"{cnt} : {lo}")