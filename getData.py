from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#tbody 하위에 있는 요소 갯수
# print(len(tbody))
slot_name_list = []
slot_position_list = []

# 파일 경로와 출력할 내용을 지정합니다.
file_path = 'output1.txt'

#search url on a page 
def makeURLList(BSojc):
    list_url = []
    for a in BSojc.find_all('a'): #모든 a태그 데이터 조회
        if "http" in a.get('href'):#href태그 내용중에 문자열 "http"가 포함되었다면
            list_url.append(a.get('href'))
    return list_url

# change to object can control with url
def makeBSOjc(url):
    html = urlopen(url)  
    bsObject = BeautifulSoup(html, "html.parser")
    return bsObject

# print each elements of a list
def make_Str(list, content):
    content += "------------------------------------" 
    for element in list:
        content += "\n"+element
    return content

#file_path안에 경로에 content 내용을 작성하여 파일을 작성
def write_to_file(file_path, list):
    try:
        #with open() as file file변수에 파일객체를 생성하는 코드이다 이때 with명령어를 사용함으로서 추후에 free를 해주지 않아도 된다.
        with open(file_path, 'w') as file:
            file.writelines(list)
        print("파일에 쓰기가 성공적으로 완료되었습니다.")
    except IOError:
        print("파일에 쓰기를 할 수 없습니다.")

obj = makeBSOjc("https://www.chuncheon.go.kr/traffic/facilities/public-parking-lot/")

#div중 id가 heatwaveSection02인 tag중 하위 tr까지 접근하여 내용 추출
tbody = obj.select("#heatwaveSection02 > ul > li > div > table > tbody > tr")

for col in range(2,3+1):
    if col == 2:
        for num in range(2,len(tbody)+1):
            objR = obj.select("#heatwaveSection02 > ul > li > div > table > tbody > tr:nth-child("+str(num)+") > td:nth-child("+str(col)+")")
            #ResultSet = list처럼 생각하면 된다.
            slot_name_list.append(objR[0].text)
    if col == 3:
        for num in range(2,len(tbody)+1):
            objR = obj.select("#heatwaveSection02 > ul > li > div > table > tbody > tr:nth-child("+str(num)+") > td:nth-child("+str(col)+")")
            #ResultSet = list처럼 생각하면 된다.
            slot_position_list.append(objR[0].text)

# 함수를 호출하여 파일에 내용을 출력합니다.
write_to_file(file_path, slot_name_list)

