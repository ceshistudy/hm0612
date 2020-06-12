# 导包
import requests

# 定义封装部门类
class TestIHRMDepartmentApi:
    def __init__(self):
        self.department_url = "http://ihrm-test.itheima.net" + "/api/company/department"

    def add_dep(self,name,code_bianhao,headers):
        jsonData = {
                   "username": name,
                   "mobile": code_bianhao,
                   "timeOfEntry": "2020-05-05",
                   "formOfEmployment": 1,
                   "departmentName": "测试部",
                   "departmentId": "1063678149528784896",
                   "correctionTime": "2020-05-19T16:00:00.000Z"
               }
        return requests.post(url=self.department_url,json=jsonData,headers=headers)

    def query_dep(self,dep_id,headers):
        query_url = self.department_url + "/" + dep_id
        return requests.get(url=query_url,headers=headers)

    def modify_dep(self,dep_id,jsonData,headers):
        modify_url = self.department_url + "/" + dep_id
        return requests.put(url=modify_url,json=jsonData,headers=headers)

    def delete_dep(self,dep_id,headers):
        delete_url = self.department_url + "/" + dep_id
        return requests.delete(url=delete_url,headers=headers)