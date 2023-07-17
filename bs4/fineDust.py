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

#문제: 동적인 페이지여서 그런가?
rows = obj.select("body > div > div > div.tblList.topFixScroll > table > tbody > tr:nth-child(2) > td")
cnt = 0
eList = [tag.get_text(strip=True) for tag in rows if tag.get_text(strip=True) != ""]
eList[1]
# for e in eList:
#     print(e)
# for e in rows:
#     cnt += 1
#     print(cnt)
#     print(e.get_text(strip=True))
