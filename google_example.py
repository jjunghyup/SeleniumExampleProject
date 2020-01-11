# Browser를 조작해주는 webdriver를 import하기
from selenium import webdriver

# Chrome을 조작용 객체를 driver로 선언
driver = webdriver.Chrome()

# 구글 페이지 열기
driver.get("https://www.google.com")

# 페이지 내 검색 창에 검색어 입력
search_input = driver.find_element_by_xpath('//input[@title="검색"]')
search_input.send_keys("selenium chrome driver download ")

# HotKey를 입력할 수 있는 Keys Library를 import하기
from selenium.webdriver.common.keys import Keys

# 이미 찾아진 검색창 element에 Enter키 입력
search_input.send_keys(Keys.ENTER)