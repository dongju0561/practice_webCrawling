
"""
    https://www.pc.go.kr/portal/intro/intro-countyoffice/intro-countyoffice-facilities/intro-countyoffice-facilities-athletic/athletic
    페이지에 존재하는 모든 링크들을 긁어모으는 코드
    

    problem!
    Traceback (most recent call last):
    File "/Users/DJ/Desktop/webCrawling/bs4/appendURL.py", line 31, in <module>
    list_url = makeURLList(ojc)
    File "/Users/DJ/Desktop/webCrawling/bs4/appendURL.py", line 15, in makeURLList
    if "http" in a.get('href'):

    TypeError: argument of type 'NoneType' is not iterable
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#search url on a page 
def makeURLList(BSojc):
    list_url = []
    for a in BSojc.find_all('a'): #모든 a태그 데이터 조회
        if "http" in a.get('href'):
            list_url.append(a.get('href'))
    return list_url

# change to object can control with url
def makeBSOjc(url):
    html = urlopen(url)  
    bsObject = BeautifulSoup(html, "html.parser")
    return bsObject

bsObject = makeBSOjc("https://www.pc.go.kr/portal/intro/intro-countyoffice/intro-countyoffice-facilities/intro-countyoffice-facilities-athletic/athletic")
list_url = makeURLList(bsObject)

for num in range(0,len(list_url)):
    print("-----------------------------start")
    ojc = makeBSOjc(list_url[num])
    list_url = makeURLList(ojc)
    if len(list_url) != 0:
        print(list_url)
    print("-----------------------------end")

# html = urlopen(makeURLList(bsObject)[0])
# print(makeURLList(bsObject)[0])
# bsObject = BeautifulSoup(html, "html.parser")

# html = urlopen(list_url[0])
# bsObject = BeautifulSoup(html,"html.parser")


for a in bsObject.find_all('a'): #모든 a태그 데이터 조회
    if "http" in a.get('href'):
        list_url.append(a.get('href'))
        # list_url.append(urlopen(a.get('href')))