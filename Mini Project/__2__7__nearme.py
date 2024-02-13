from bs4 import BeautifulSoup
from selenium import webdriver




#셀레니움에 다양한 옵션을 적용시키기 위한 패키지
from selenium.webdriver.safari.options import Options

#크롬 드라이버 매니저를 실행시키기 위해 설치해주는 패키지
from selenium.webdriver.safari.service import Service
#자동으로 크롬 드라이브를 최신으로 유지해주는 패키지 
from webdriver_manager import SafariManager
#클래스, 아이디, css_selector를 이용하고자 할때
from selenium.webdriver.common.by import By
#키보드 입력
from selenium.webdriver.common.keys import Keys

import time

user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36"

#크롬 드라이버 매니저를 자동으로 설치되도록 실행시키는 코드
options_ = Options()
service = Service(SafariManager().install())
driver = webdriver.Safari(service=service, options=options_)


## 1. 데이터 스크래핑

# 근처맛집 검색페이지를 url로 설정
url = "https://map.naver.com/p/search/%EA%B7%BC%EC%B2%98%20%EB%A7%9B%EC%A7%91?searchType=place&c=13.00,0,0,0,dh"
driver.get(url)
time.sleep(1)

# 스크롤 반복 하강시켜서 데이터 수집
# 각 가게를 클릭하면 url 주소가 바뀜 -> 이걸 list로 받아와서 ...

urls = []

for i in range(10):
    # 현재 페이지를 맨 아래로 스크롤하여 많은 가게 목록 확보
    scrollBox = driver.find_element(By.ID, "_pcmap_list_scroll_container") # 얘 id가 _pcmap_list_scroll_container라고 ㅜㅜ
    driver.execute_script("arguments[0].scrollIntoView(true);", scrollBox)
    # 페이지 로드 시간 확보
    time.sleep(3)
    
    # 클릭해서 가게의 상세페이지를 불러올 요소
    elements = driver.find_elements(By.CLASS_NAME, "Fc1rA")
    
    for element in elements:
        element.click() # 각 요소들을 클릭
        time.sleep(2) # 페이지 로드 시간 확보
        current_url = driver.current_url
        urls.append(current_url)
    

    print(urls)
    
    
# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")

# store_name= soup.select(".Fc1rA")

# for i in store_name :
#     print(i)


