from bs4 import BeautifulSoup
import requests
import re
import time
from urllib.parse import quote_plus
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Web Driver

baseUrl = 'https://browse.auction.co.kr/search?keyword='
plusUrl = input('검색어를 입력하세요: ')
url = baseUrl + quote_plus(plusUrl)

# chromedriver path input
driver = webdriver.Chrome('E:\python\crawling\chromedriver')
driver.get(url)
driver.implicitly_wait(10)
rank = 0
html = driver.page_source
soup = BeautifulSoup(html)
# Gmarket _ 판매점 랭킹
soups = soup.select('.itemcard > .section--itemcard')

for sop in soups:    
    sop_t = sop.select_one('.text--title').get_text()
    sop_p = sop.select_one('.text--price_seller').get_text()
    sop_l = sop.select_one('.section--itemcard_info_score')
    rank = rank + 1

    print(f"판매점 랭킹 {rank}위 \n 물품명 : {sop_t} \n 가격 : {sop_p} \n 평점 : {sop_l}")

driver.close()
