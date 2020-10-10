# -*- coding:utf-8 -*-
#不带参数的get

import requests
import json

host = "http://httpbin.org/"
endpoint = "get"    #接口

url = ''.join([host,endpoint])  #http的url
# print(url)
r = requests.get(url)   #gte请求

response = r.json()
print(response)

print(type(r.text))
print(eval(r.text))   #eval 方法能使字符串本身的引号去掉，保留字符的原本属性。
print (r.text)