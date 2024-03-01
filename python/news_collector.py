#크롤링시 필요한 라이브러리 불러오기
from bs4 import BeautifulSoup
import requests
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#웹드라이버 설정
# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get(url='https://korea.kr/news/policyNewsList.do')
for i in range(2,10):
    driver.find_element(By.XPATH,f'//*[@id="container"]/div/div/div[2]/div[4]/span[{i}]/a').click()
    for j in range(1,10):
        driver.find_element(By.XPATH, f'//*[@id="container"]/div/div/div[2]/div[3]/ul/li[1]/a/span[2]/strong').click()
        cont = driver.find_element(By.XPATH,'//*[@id="container"]/div/div').text
        print(cont)
        driver.back()

driver.quit()
