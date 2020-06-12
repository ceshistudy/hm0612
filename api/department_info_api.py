# 导包
import requests

# 定义封装的类
class TestIHRMInfoApi:

    def __init__(self):
        self.info_url = "http://ihrm-test.itheima.net" + "/api/company/department/:id"

    def dep_info(self, jsonData, headers):
        return requests.post(url=self.info_url, json = jsonData,headers = headers)