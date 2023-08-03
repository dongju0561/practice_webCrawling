from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

file_path = "/Users/DJ/Desktop/gitRes/webCrawling/main/crawling_result.txt"
div = " | "
row_data = "| "

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

def init_write(file_path):
    div_line = "--------------------------------------------\n"

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

#파일 초기화
init_write(file_path)

# 웹드라이버 초기화
driver = webdriver.Chrome()

# 사이트 접속
driver.get('https://www.chuncheon.go.kr/cityhall/citizen-participation/participation-forum/free/')
page_url_list = [] #pager-numlist안에 있는 url들을 담은 list

# 페이저안에 있는 10개의 url데이터를 page_url_list에 추가
span = driver.find_element(By.CSS_SELECTOR,'#main > div.content > div.sub-section > div > div.pager > div.mobhide > span')

aS = span.find_elements(By.TAG_NAME,'a')
for a in aS:
    page_url_list.append(a.get_attribute('href'))

#수집한 url데이터를 가지고 페이지들을 순회하면 ul안에 있는 텍스트들을 수집

for url in page_url_list:
    driver.get(url)
    ul = driver.find_element(By.CLASS_NAME,'board-list')
    rows = ul.find_elements(By.TAG_NAME,'li')
    for row in rows:
        cols = row.find_elements(By.TAG_NAME,'span')
        i_url = row.find_element(By.TAG_NAME, 'a').get_attribute('href')

        #상세 게시물 접속
        """
        코딩 플랜
        상세 게시물의 내용은 태그들간 계층구조로 구성되어 있으며 높은 레벨부터 순서대로 텍스트들을 concat 작업 진행
        """
        driver.get(i_url)
        s = Stack()
        ps = driver.find_elements(By.CLASS_NAME, 'boardview-con')
        for p in ps:
            l1s = p.find_elements(By.XPATH, './/*') #p태그 내부에 있는 모든 span태그들을 가져옴 레벨과 상관없이 그냥 다 가져옴
            for l1 in l1s:
                if(l1.text != ""):
                    s.push(l1.text)
                    print(len(s.stack))
                    # print(s.stack)
                    l2s = l1.find_elements(By.XPATH, './/*')
                    for e in l2s:
                        print(e.tag_name)
                    for l2 in l2s:
                        if(l2.text != ""):
                            s.push(l2.text)
                            l3s = l2.find_elements(By.XPATH, './/*')
                            for l3 in l3s:
                                if(l3.text != ""):
                                    s.push(l3.text)
                                    l2s = l3.find_elements(By.XPATH, './/*')
            print(s.stack)
            # for span in spans:
            #     print(span.text)
            #     try: #span 내부 text가 strong태그로 감싸져 있는 경우 예외처리
            #         strong = span.find_element(By.TAG_NAME,"strong")
            #     except NoSuchElementException:
            #         pass
        print("---------------------------------------------------------")
        driver.back()
        #상세 게시물 접속 끝

        for col in cols:
            current_class=col.get_attribute('class')
            if current_class == 'num' or current_class == '' or current_class == 'day' or current_class == 'writer dotdot' or current_class == 'view': #클래스 이름을 가지고 태그ul 안에 데이터들 중에 원하는 데이터를 골라 수집
                # print(col.text)
                row_data += col.text
                row_data += div
        
        try:
            with open(file_path, 'a') as file:
                file.writelines("\n")
                file.writelines(row_data)
                row_data = ""
                file.writelines("\n")
                
        except IOError:
            print("Adding row failed")    











# # 테이블 요소 가져오기
# table = driver.find_element(By.CLASS_NAME, 'board-list')
# print(type(table))

# # 테이블의 모든 행 가져오기
# rows = table.find_elements(By.TAG_NAME, 'li')

# for row in rows:
#     # 각 행의 모든 열 가져오기
#     cols = row.find_elements(By.TAG_NAME, 'span')
    
#     for col in cols:
#         # 각 열의 텍스트 출력
#         print(col.text)

# # 웹드라이버 종료
# driver.quit()
