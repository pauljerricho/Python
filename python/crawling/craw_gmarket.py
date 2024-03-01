from bs4 import BeautifulSoup
import requests
import re
import time
from urllib.parse import quote_plus
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Web Driver

baseUrl = 'https://browse.gmarket.co.kr/search?keyword='
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

soup_info = soup.find_all('div','box__information_seller')

for sop in soup_info:
    sop = soup_info.find('span', class_ ='text__seller')
    print(sop)

# soups_score = soup.select('.image__awards-points')
# soups_info = soup.select('.box__information_seller')
# rank = 0
# list_info = []
# list_score = []
# for sop in soups_info:
#     sop_seller = sop.select_one('.text__seller')
#     rank = rank + 1
#     seller = str(sop_seller)
#     if seller == "None":
#         list_info.append("스마일배송")
#     else:
#         seller = str(sop_seller).split(">")
#         list_info.append(seller[1][:-6])

# for sop in soups_score:
#      sop_score = sop.select_one('.for-a11y').get_text()
#      list_score.append(sop_score)

# print(list_info)
# print(list_score)

# list_mer = list(map(list.__add__(list_info,list_score)))