''' 
(1) 하단 url에서 UEzoS VHJNR 클래스를 클릭해서 나오는 url 수집
https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EA%B7%BC%EC%B2%98+%EB%A7%9B%EC%A7%91

(2) 페이지 넘기는 버튼으로 
'''


#(1)

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

# 옵션 설정
options = Options()
user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)"
options.add_argument(f"User_Agent={user}")
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)


url = None
for i in range(5) :
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EA%B7%BC%EC%B2%98+%EB%A7%9B%EC%A7%91"
    driver.get(url)

    driver.find_element(By.CLASS_NAME, ".cmm_pg_next").click()
    
    current_url = 