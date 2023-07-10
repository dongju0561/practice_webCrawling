import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

# change to object can control with url
def makeBSOjc(url):
    html = urlopen(url)  
    bsObject = BeautifulSoup(html, "html.parser")
    return bsObject

obj = makeBSOjc("https://www.airkorea.or.kr/web/sidoAirInfo/sidoAirInfoDay01?itemCode=10007&ymd=2023-07-05%2010&areaCode=033&tDate=2023-07-01&monthDay=31")
value_list = []
rows = obj.select("body > div > div > div.tblList.topFixScroll > table > tbody > tr:nth-child(2) > td:nth-child(0)")
print(rows)

# for row in rows:
#     row.get_text(strip=True)
#     if (row):
#         data = row.get_text(strip=True)
#         print(data)

# for row in rows:
#     element = row.select_one('')
#     if(element & element == '-'):
#         value_list.append((element.get_text(strip=True)))