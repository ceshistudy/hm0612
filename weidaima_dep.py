# 需求：实现员工管理模块的登录
# 导包
import requests

# 发送IHRM登录的接口请求
response = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                         json={"mobile": "13800000002", "password": "123456"},
                         headers={"Content-Type": "application/json"})
# 查看登录的结果
print("登录的结果为：", response.json())

# 获取登录返回的令牌
token = "Bearer " + response.json().get("data")
print("提取的令牌为：",token)
# 发送添加员工接口
headers = {"Content-Type":"application/json","Authorization":token}     # 添加部门的请求头
response = requests.post(url="http://ihrm-test.itheima.net" + "/api/company/department/",
                         json={
                                "name":"唐皓666",
                                "code_bianhao": "009",
                                "timeOfEntry":"2020-05-05",
                                "formOfEmployment":1,
                                "departmentName":"测试部",
                                "departmentId":"1063678149528784896",
                                "correctionTime":"2020-05-19T16:00:00.000Z"
                                },
                         headers = headers)
# 打印添加部门的接口
print("添加部门的接口返回数据为：",response.json())
# 提取添加部门接口返回的部门id
dep_id = response.json().get("data").get("id")
print("提取的部门id为：",dep_id)


# 拼接查询部门接口的URL
query_url = "http://ihrm-test.itheima.net" +  "/api/company/department/" + "/" + dep_id
# 发送查询部门接口的请求
response = requests.get(url=query_url, headers=headers)
# 打印添加部门的结果
print("查询部门的结果为：",response.json())


# 拼接修改部门接口的URL
modify_url = "http://ihrm-test.itheima.net" +  "/api/company/department/" + "/" + dep_id
# 发送修改部门接口的请求
response = requests.put(url=modify_url,json={"name":"牛顿"},headers=headers)
# 打印修改部门的结果
print("修改部门的结果为：",response.json())

# 拼接删除部门的URL
delete_url = "http://ihrm-test.itheima.net" +  "/api/company/department/" + "/" +dep_id
# 发送删除部门的接口请求
response = requests.delete(url=delete_url,headers=headers)
# 打印删除部门的结果
print("删除部门的结果为：",response.json())

