from bs4 import BeautifulSoup
from selenium import webdriver
import time

# 웹드라이버 옵션 설정
options = webdriver.SafariOptions()
options.add_argument('-headless')  # 브라우저 창을 띄우지 않고 실행
options.add_argument('-no-sandbox')
options.add_argument('-disable-dev-shm-usage')

# 드라이버 실행
driver = webdriver.Safari(options=options)

# 근처맛집 검색페이지를 url로 설정
url = "https://map.naver.com/p/search/%EA%B7%BC%EC%B2%98%20%EB%A7%9B%EC%A7%91?searchType=place&c=13.00,0,0,0,dh"
driver.get(url)
time.sleep(2)  # 페이지가 로딩될 때까지 충분한 시간 대기

# 스크롤을 내려서 많은 가게 목록을 확보
for i in range(5):  # 예시로 5번 스크롤
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # 스크롤 이후에 충분한 시간 대기

# 가게 URL 수집
urls = []
elements = driver.find_elements_by_css_selector(".search_title")  # 가게 타이틀 요소들
for element in elements:
    urls.append(element.get_attribute("href"))  # 각 가게의 URL을 리스트에 추가

# 수집된 가게 URL 출력
for url in urls:
    print(url)

# 드라이버 종료
driver.quit()
