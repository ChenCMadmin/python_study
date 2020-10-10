# -*- coding:utf-8 -*-
# 带header的get：
import requests
import json

host = "http://httpbin.org/"
endpoint = "get"

url = ''.join([host,endpoint])
headers = {"User-Agent":"test request headers"} #信息头

r = requests.get(url)
r = requests.get(url,headers=headers)
#response = r.json()


print((eval(r.text))['headers']['User-Agent'])