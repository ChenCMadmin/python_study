# -*- coding:utf-8 -*-
# 带json的post
import requests
import json

host = "http://httpbin.org/"
endpoint = "post"

url = ''.join([host,endpoint])
data = {
    "sites": [
                { "name":"test" , "url":"www.test.com" },
                { "name":"google" , "url":"www.google.com" },
                { "name":"weibo" , "url":"www.weibo.com" }
    ]
}

r = requests.post(url,json=data)
# r = requests.post(url,data=json.dumps(data))
# response = r.json()
# print(r.text)
print(eval(r.text))