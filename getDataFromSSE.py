#-*- coding:utf-8 -*-
import requests

url = 'http://www.baidu/com'
r = requests.get(url)
print("-----begin to get -------")
print(r.text)

