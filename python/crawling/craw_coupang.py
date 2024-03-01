from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 크롬드라이버
driver = webdriver.Chrome('E:\python\crawling\chromedriver')

# 쿠팡으로 이동
driver.get('https://www.coupang.com/np/categories/178255')

lis = driver.find_element(By.ID, 'productList').find_elements(By.TAG_NAME, 'li')

for li in lis:
    try:
        print("Product :" + li.find_element(By.CLASS_NAME, 'name').text)
        print("Price :" + li.find_element(By.CLASS_NAME,'price-value').text)
        print("delivery" + li.find_element(By.CLASS_NAME,'delivery').text)
        print("URL: " + li.find_element(By.CLASS_NAME,'baby-product-link').get_attribute('href'))
        print('-'*100)
    except Exception:
        pass

# 성공!
# 쿠팡 카테코리 별 인기제품 가져오기
