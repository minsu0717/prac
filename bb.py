from selenium import webdriver
from selenium.webdriver.ie.options import Options
import time

# chromedriver
driver = webdriver.Chrome('./chromedriver')

# load page
driver.get(url='https://blog.naver.com/bizspringcokr/222638819175')
time.sleep(40)
print(driver.current_url)

driver.close()