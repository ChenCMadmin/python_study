# -*- coding: utf-8 -*-
import requests

class web_requests(object):
    def __init__(self):
        pass

    def Interface(self,Interface_path,data):
         url = "http://113.31.114.204:5000/%s" %(Interface_path) # 测试的接口url
         r = requests.post(url=url, json=data)  # 发送请求
         return r.json()
         # print (r.text)  # 获取响应报文
         # print (r.status_code)  # 状态代码

a = web_requests()
data1 = {"spotPrice":3.325,"strikePrice":2.55,"riskFreeRate":0.030019999999999998,"calculationDate":{"year":2020,"month":9,"day":23},"maturityDate":{"year":2020,"month":9,"day":23},"optionType":"CALL","volatility":0.2883}  # 接口传送的参数

print(a.Interface('pricing',data1))