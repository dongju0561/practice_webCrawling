from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#---전역 변수---
url = "https://www.jeongseon.go.kr/portal/jeongseongun/healthcenter/healthadmin"
div_line = "--------------------------------------------\n"
file_path = "/Users/DJ/Desktop/webCrawling/main_crawling/output1.txt"

#---함수---
#반복문을 통해 selector 조정
def iter_selector():
    selector_list = []
    for num in range(1,10):
        selector_list.append(f"#A-Contents > div.skinMb-small > table > tbody > tr:nth-child({num}) > td")
    return selector_list

#bs 객체 생성
def makeBSOjc(url):
    html = urlopen(url)  
    bsObject = BeautifulSoup(html, "html.parser")
    return bsObject

#파일 작성 초기화
def init_write(file_path):
    try:
        #with open() as file file변수에 파일객체를 생성하는 코드이다 이때 with명령어를 사용함으로서 추후에 free를 해주지 않아도 된다.
        with open(file_path, 'w') as file:
            file.writelines(div_line)
            init_string = " # | title | writer | date | detail url|"
            file.writelines(init_string)
            file.writelines("\n")
            file.writelines(div_line)
        print("파일에 쓰기가 성공적으로 완료되었습니다.")
    except IOError:
        print("파일에 쓰기를 할 수 없습니다.")

#tbody의 일련의 td 택스트 데이터 row 구성
def stack_row(file_path:str, target_url:str, selector:str):
    div = " | "
    row_data = "| "
    row_list = []

    obj = makeBSOjc(target_url)
    tbody = obj.select(selector)

    #string concat 반복
    for e in range(0,len(tbody)):
        row_list.append(tbody[e].get_text(strip=True)) #가져온 데이터 넣기
        if tbody[e].get_text(strip=True) != "":
            row_data += tbody[e].get_text(strip=True)
        # else:
        #     row_data = ""
        row_data += div

    try:
        with open(file_path, 'a') as file:
            file.writelines("\n")
            file.writelines(row_data)
            file.writelines("\n")
        print("row 추가")
    except IOError:
        print("row 추가할 수 없습니다.")

    """
        crawling한 데이터 list에 append하는 함수
        
        자료구조?? dictionary로 할까? list로 할까?
        list:[num,title,writor,date,url]
        dic:[num: ,title: ,writor: ,date: ,url: ]

        우선은 자료구조를 따로 사용하지 않고 string concat
    """

#main

init_write(file_path)

selectors = iter_selector()
for selector in selectors:
    stack_row(file_path,url,selector)

#main end
