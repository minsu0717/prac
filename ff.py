from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

keywords = ['파이썬코딩비현코','비전공자현업코딩','멀티캠퍼스 업무효율화']
for a in keywords:
    # 인터넷 열기

    driver = webdriver.Chrome('C:/sel/chromedriver_win32/chromedriver')


    # 원하는 사이트 접속
    driver.get('https://www.naver.com')


    # 원하는 요소를 찾기
    first_sel = driver.find_element(By.ID,'query')

    # 원하는 요소에 데이터를 입력하기
    first_sel.send_keys(a)


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