# -*- coding:utf-8 -*-
#带参数的get

import requests
import json

host = "http://httpbin.org/"
endpoint = "get"

url = ''.join([host,endpoint])
params = {"show_env":"1"}   #参数
r = requests.get(url=url,params=params)

print(eval(r.text))
