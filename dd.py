from selenium import webdriver
from selenium.webdriver.ie.options import Options
from selenium.webdriver.common.by import By

# chromedriver
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver = webdriver.Chrome('./chromedriver', options=options)

# Load Page
driver.get(url='https://blog.naver.com/bizspringcokr/222638819175')

# 실제 페이지는 "https://blog.naver.com/PostView.naver?blogId=bizspringcokr&logNo=222638819175&redirect=Dlog&widgetTypeCall=true&directAccess=false"
# iframe으로 호출된다.
driver.switch_to.frame("mainFrame");

# 공감
print("공감")
sympathy_element = driver.find_element(By.CSS_SELECTOR,'div.area_sympathy')
em_elements = sympathy_element.find_elements(By.CSS_SELECTOR,"em.u_cnt._count")
for i, em in enumerate(em_elements):
    print("  L", i, "번째 em:", em.text)

# 댓글
print("댓글")
comment_elements = driver.find_element(By.CSS_SELECTOR,'div.area_comment')
em_elements = comment_elements.find_elements(By.CSS_SELECTOR,"#floating_bottom_commentCount")
for i, em in enumerate(em_elements):
    print("  L",i, "번째 em:", em.text)

driver.close()
#Sympathy222638819175 > div > span > em.u_cnt._count
#Sympathy222638819175 > div
#area_sympathy222638819175
#printPost1 > tbody > tr > td.bcc > div.post-btn.post_btn2
#area_sympathy222638819175 > div
#area_sympathy222638819175
#commentCount
#floating_bottom_commentCount
#Sympathy222638819175 > div > span > em.u_cnt._count
#floating_bottom > div > div > div.area_sympathy
#floating_bottom > div > div > div.area_sympathy > a > div
