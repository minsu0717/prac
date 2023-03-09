from selenium import webdriver


# driver 경로를 파일경로와 같은 곳에 둘 경우
driver = webdriver.Chrome()
url = 'https://www.google.com'
driver.get(url)

# driver 경로를 파일경로와 다른 곳에 둘 경우
# driver = webdriver.Chrome('driver의 경로')
# url = 'https://www.google.com'
# driver.get(url)