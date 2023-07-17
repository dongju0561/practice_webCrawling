"""
    selenium 라이브러리를 이용해서 실제로 사용자가 입력을 통해 웹페이지를 돌아다니면서 페이지의 데이터를 수집이 가능하다
    css선택자으로 다른 페이지로 이동할 수 있는 경로
"""

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def makeBSOjc(url):
    html = urlopen(url)  
    bsObject = BeautifulSoup(html, "html.parser")
    return bsObject

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get('https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%EA%B0%95%EC%95%84%EC%A7%80')
time.sleep(0.5)
firstImage = driver.find_element(By.CSS_SELECTOR, '#imageColl > div.cont_img > div.image_main > div.list_row > div:nth-child(5) > div:nth-child(1) > div.wrap_thumb > a > img')
firstImage.click()
time.sleep(0.5)
secondImage = driver.find_element(By.CSS_SELECTOR, '#imageColl > div.cont_img > div.image_viewer > div > div.viewer_card > div.card_image > div.item_info > a')
secondImage.click()
time.sleep(0.5)
print(driver.current_url) #현재 위치의 url을 출력
html = urlopen(driver.current_url)
obj = BeautifulSoup(html, "html.parser")
print(obj)

print(driver.title)
time.sleep(3)
driver.quit()

# # 텍스트 필드에 문자 입력
# text_field = driver.find_element_by_css_selector("#stx")
# text_field.clear()  # 필드 내용  초기화
# text_field.send_keys("입력할 텍스트")

# # 버튼 클릭
# button = driver.find_element_by_css_selector("#bo_sch > form > button")
# button.click()

# # 웹 페이지 유지 시간을 위해 대기
# driver.implicitly_wait(5)  # 5초 대기

# # 브라우저 닫기
# driver.quit()


