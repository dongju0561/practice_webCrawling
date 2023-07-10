import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup
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
    print(makeURLList(ojc))
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