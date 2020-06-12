# 导包
import requests

# 定义封装的类
class TestIHRMJiagouApi:

    def __init__(self):
        self.jiagou_url = "http://ihrm-test.itheima.net" + "/api/company/department"

    def Dep_Jiagou(self, jsonData, headers):
        return requests.post(url=self.jiagou_url, json = jsonData,headers = headers)