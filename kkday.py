# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 15:29:46 2021

@author: USER
"""

import json 
import requests

url = "https://www.kkday.com/zh-tw/area_api/ajax_get_recommend_top_products?areaCode=A01-001-00020"

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
    }
data = requests.get(url,headers = header)
data.encoding="utf-8"
data = data.text

travel = json.loads(data)

goods = travel['data']

for row in goods:
    title = row['name']
    imgurl = row['img_url']
    price = row['price']
    link = row['url']
    
    print('標題:',title)
    print('價格:',price)
    print('網址:',link)
    print('圖片:',imgurl)