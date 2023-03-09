from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# 인터넷 열기

driver = webdriver.Chrome('C:/sel/chromedriver_win32/chromedriver')


# 원하는 사이트 접속
driver.get('https://www.naver.com')


# 원하는 요소를 찾기
first_sel = driver.find_element(By.ID,'query')

# 원하는 요소에 데이터를 입력하기
first_sel.send_keys('김민수')


# 원하는 요소를 클릭하기
second_sel = driver.find_element(By.CLASS_NAME,'ico_search_submit' )
second_sel.click()
# time.sleep(10)

# 원하는 요소의 데이터를 가져오기(문자)
third_sel = driver.find_element(By.ID,'main_pack')
print(third_sel.text)

# 원하는 요소의 데이터를 가져오기(html)
third_sel = driver.find_element(By.ID,'main_pack')
print(third_sel.get_attribute('innerHTML'))

sel_list = driver.find_elements(By.TAG_NAME,'li')

my_list = []
for a in sel_list:
    # print(a.text)
    my_list.append(a.text)
    
import pandas as pd
df = pd.DataFrame(my_list)
df.to_excel('test.xlsx')
