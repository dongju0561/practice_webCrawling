"""
    https://www.hongcheon.go.kr/www/contents.do?key=397 
    (유용한 시설 -> 체육시설)경로의 체육시설 정보 페이지로 넘어갈 수 있는 url data 수집

    coding plan
    받아온 url을 다시 bs객체로 만들어 정보수집

    problem!
    가져온 url data가 bs객체로 만들 수 없는 형식의 string값
    string값을 조정하여 bs객체를 만들 수 있게 변형!
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def makeBSOjc(url):
    html = urlopen(url)  
    bsObject = BeautifulSoup(html, "html.parser")
    return bsObject

obj = makeBSOjc("https://www.hongcheon.go.kr/www/contents.do?key=397")
ul = obj.select('#container > div > div > div.side_menu > nav > div > ul > li:nth-child(7) > div > ul > li:nth-child(3) > div > ul > li.depth_item > a')

for n in ul:
    print(n.get_text())
    url = n.get('href')
    print(url)
    # obj = makeBSOjc(url)
    print("_________________________")

