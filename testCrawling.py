import ssl # 인증 모듈
from urllib.request import urlopen
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context

#urlopen을 통해 해당 url에 사이트 접속: HTTPResponse 객체 반환
html = urlopen("https://www.pc.go.kr/portal/intro/intro-countyoffice/intro-countyoffice-facilities/intro-countyoffice-facilities-athletic/athletic")  
URLstr = "https://www.pc.go.kr/portal/intro/intro-countyoffice/intro-countyoffice-facilities/intro-countyoffice-facilities-athletic/athletic"
#입력받은 데이터를 파싱
bsObject = BeautifulSoup(html, "html.parser")

#bsObject.find_all('meta')
#meta 태그의 모든 속성들을 하나의 요소로 하여 배열을 만듬
# for td in bsObject.find_all('td'):
    # print((td.text))
target_text = "평창종합운동장"
cnt = 0
url = []
for a in bsObject.find_all('a'):
    a.get(href)
    cnt += 1
    if target_text in a.text: #문자열에서 특정문자 찾는 방법
        URLstr = a.get('href')
        print("https://www.pc.go.kr"+URLstr)

#meta태그에서 속성이름이 content인것 중에 속성값이 width=1190인 태그의 모든 속성 출력
#.get() = 해당 메소드는 태그 안에 속성들중 입력한 속성의 이름에 해당하는 속성값을 반환한다.
# print(bsObject.find("meta",{"content":"IE=edge","http-equiv":"X-UA-Compatible"}))

# for a in bsObject.find_all("a"):
#     print(a.get("href"))