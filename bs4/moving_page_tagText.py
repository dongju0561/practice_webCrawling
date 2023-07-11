import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup
ssl._create_default_https_context = ssl._create_unverified_context

html = urlopen("https://www.pc.go.kr/portal/intro/intro-countyoffice/intro-countyoffice-facilities/intro-countyoffice-facilities-athletic/athletic")  
URLstr = "https://www.pc.go.kr/portal/intro/intro-countyoffice/intro-countyoffice-facilities/intro-countyoffice-facilities-athletic/athletic"
bsObject = BeautifulSoup(html, "html.parser")
target_text = "평창종합운동장"

print(URLstr)

for a in bsObject.find_all('a'): #모든 a태그 데이터 조회
    if target_text in a.text: #문자열에서 특정문자 찾는 방법
        URLstr = a.get('href')
        print("https://www.pc.go.kr"+URLstr)

