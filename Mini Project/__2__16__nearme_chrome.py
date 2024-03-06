from bs4 import BeautifulSoup
from selenium import webdriver

#셀레니움에 다양한 옵션을 적용시키기 위한 패키지
from selenium.webdriver.chrome.options import Options

#크롬 드라이버 매니저를 실행시키기 위해 설치해주는 패키지
from selenium.webdriver.chrome.service import Service
#자동으로 크롬 드라이브를 최신으로 유지해주는 패키지 
from webdriver_manager.chrome import ChromeDriverManager
#클래스, 아이디, css_selector를 이용하고자 할때
from selenium.webdriver.common.by import By
#키보드 입력
from selenium.webdriver.common.keys import Keys

import time

user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

#크롬 드라이버 매니저를 자동으로 설치되도록 실행시키는 코드
options_ = Options()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options_)


## 1. 데이터 스크래핑

# 근처맛집 검색페이지를 url로 설정
url = "https://map.naver.com/p/search/%EA%B7%BC%EC%B2%98%EB%A7%9B%EC%A7%91?searchType=place&c=13.00,0,0,0,dh"
driver.get(url)

driver.find_element(By.CLASS_NAME, "place_bluelink.N_KDL").click()
time.sleep(0.5)

current_url = driver.current_url
print("Current URL:", current_url)

driver.quit()