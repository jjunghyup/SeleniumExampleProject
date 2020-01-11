from selenium import webdriver

driver = webdriver.Chrome()
# iframe 샘플 사이트 접속
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe")

# swich_to.frame() function을 활용해서 iframe지정
driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@name="iframeResult"]'))
# 그 밑의 새로운 iframe을 지정
driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@src="https://www.w3schools.com"]'))

# 지정한 element를 찾아서 클릭
driver.find_element_by_xpath('//a[@title="Translate W3Schools"]').click()
