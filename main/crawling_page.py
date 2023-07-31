import ssl
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
ssl._create_default_https_context = ssl._create_unverified_context

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get('https://www.jeongseon.go.kr/portal/jeongseongun/healthcenter/healthadmin')
print(driver.current_url)
time.sleep(0.5)
firstImage = driver.find_element(By.CSS_SELECTOR, '#A-Contents > div.skinMb-small > table > tbody > tr:nth-child(2) > td > a')
firstImage.click()
time.sleep(0.5)
print(driver.current_url)

#---전역 변수---
url = "https://www.jeongseon.go.kr/portal/jeongseongun/healthcenter/healthadmin"
div_line = "--------------------------------------------\n"
file_path = "/Users/DJ/Desktop/webCrawling/main/crawling_result.txt"

#---함수---
#반복문을 통해 selector 조정
def iter_selector():
    selector_list = []
    for num in range(1,15):
        selector_list.append(f"#A-Contents > div.skinMb-small > table > tbody > tr:nth-child({num}) > td")
    return selector_list

#BS 객체 생성
def makeBSOjc(url):
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    return bsObject

#파일 작성 초기화
def init_write(file_path):
    #file 입력
    try:
        #with open() as file file변수에 파일객체를 생성하는 코드이다 이때 with명령어를 사용함으로서 추후에 free를 해주지 않아도 된다.
        with open(file_path, 'w') as file:
            file.writelines(div_line)
            init_string = " # | title | writer | date | detail url|"
            file.writelines(init_string)
            file.writelines("\n")
            file.writelines(div_line)
        print("File initialization successful.")
    except IOError:
        print("File initialization failed")

#tbody의 일련의 td 택스트 데이터 row 구성
def stack_row(file_path:str, target_url:str, selector:str):
    div = " | "
    row_data = "| "
    row_list = []
    num = 0

    obj = makeBSOjc(target_url)
    tbody = obj.select(selector)

    #string concat 반복
    for e in range(0,len(tbody)):
        row_list.append(tbody[e].get_text(strip=True)) #가져온 데이터 넣기
        if e != 1:
            row_data += tbody[e].get_text(strip=True)
        else:
            #너무 노가다이겠는걸...
            link = obj.select_one(f"#A-Contents > div.skinMb-small > table > tbody > tr:nth-child({e+1}) > td.skinTb-sbj > a").get('href')
            #link에 javascript:goPage2('275716')이게 존재함..
            row_data += link
        row_data += div

    #file 입력
    try:
        with open(file_path, 'a') as file:
            file.writelines("\n")
            file.writelines(row_data)
            row_data = ""
            file.writelines("\n")
    except IOError:
        print("Adding row failed")

"""
crawling한 데이터 list에 append하는 함수

자료구조?? dictionary로 할까? list로 할까?
list:[num,title,writor,date,url]
dic:[num: ,title: ,writor: ,date: ,url: ]

우선은 자료구조를 따로 사용하지 않고 string concat
"""

#---main---
init_write(file_path)

selectors = iter_selector()
for selector in selectors:
    stack_row(file_path,url,selector)

#---main end---
