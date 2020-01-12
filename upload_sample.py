from selenium import webdriver
driver = webdriver.Chrome()
# sample upload 페이지 열기
driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")

# upload를 위한 "파일선택" 버튼 클릭
driver.find_element_by_xpath('//input[@name="upfile"]').click()

# autoit library import
import autoit

# 창 이름이 "열기"인 windows창 보일때까지 3초 대기
autoit.win_wait_active("열기", 3)

# 해당 객체에 Edit1객체에 download url을 입력
autoit.control_send("열기", "Edit1", "C:\\Users\\Administrator\\Downloads\\inpect.exe")