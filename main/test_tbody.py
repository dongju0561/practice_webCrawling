from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.jeongseon.go.kr/portal/jeongseongun/healthcenter/healthadmin"

def makeBSOjc(url):
    html = urlopen(url)  
    bsObject = BeautifulSoup(html, "html.parser")
    return bsObject

obj = makeBSOjc(url)
value_list = []
tbody = obj.select("#A-Contents > div.skinMb-small > table > tbody > tr:nth-child(1) > td")

for e in range(0,len(tbody)):
    value_list.append(tbody[e].get_text(strip=True))

print(value_list)






"""
    error
    div 접근문제
    "https://gwijed.gwe.go.kr/boardCnts/list.do?boardID=2080&m=0101&s=kwije"
    "#subContent > div.subContent_body > :nth-child(3) > div.clearfix"

    SSL 문제
"""