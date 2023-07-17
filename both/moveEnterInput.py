from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup
ssl._create_default_https_context = ssl._create_unverified_context

def makeBSOjc(url):
    html = urlopen(url)  
    bsObject = BeautifulSoup(html, "html.parser")
    return bsObject

driver = webdriver.Chrome()
driver.get(url='https://www.google.com/')


text_field = driver.find_element(By.ID,"APjFqb")
text_field.clear()  # 필드 내용  초기화
text_field.send_keys("shu") #검색창 입력
text_field.submit() #검색


link = driver.find_element(By.CSS_SELECTOR,f'#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e > div > a > h3')
link.click()
time.sleep(0.2)
driver.back()
link = driver.find_element(By.CSS_SELECTOR,f'#rso > div:nth-child(2) > div > div > div > div.Z26q7c.UK95Uc.jGGQ5e > div > a > h3')
link.click()
time.sleep(5)

driver.quit()
