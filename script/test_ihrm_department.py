# 导包
import unittest, logging
import app
from api.IHRM_department_api import TestIHRMDepartmentApi
from api.IHRM_login_api import TestIHRMLoginApi
from utils import assert_common

# 创建测试类
class TestIHRMDepartment(unittest.TestCase):
    # 初始化unittest的函数
    def setUp(self):
        # 实例化登录
        self.login_api = TestIHRMLoginApi()
        # 实例化部门
        self.dep_api = TestIHRMDepartmentApi()

    def tearDown(self):
        pass

    # 实现登录成功的接口
    def test01_login_success(self):
        jsonData = {"mobile": "13800000002", "password": "123456"}
        response = self.login_api.login(jsonData,
                                        {"Content-Type": "application/json"})
        logging.info("登录接口返回的结果为：{}".format(response.json()))
        # 提取登录返回的令牌
        token = 'Bearer ' + response.json().get('data')
        # 把令牌拼接成HEADERS并保存到全局变量HEADERS
        app.HEADERS = {"Content-Type":"application/json", "Authorization": token}
        # 打印请求头
        logging.info("保存到全局变量中的请求头为：{}".format(app.HEADERS))
        # 断言
        assert_common(self, 200, True, 10000, "操作成功", response)

    def test02_add_dep(self):
        logging.info("app.HEADERS的值是：{}".format(app.HEADERS))
        response = self.dep_api.add_dep("祖冲之", "13986350846", app.HEADERS)
        logging.info("添加部门的结果为：{}".format(response.json()))
        # 提取员工中的令牌并把员工令牌保存到全局变量中
        app.EMP_ID = response.json().get("data").get("id")
        logging.info("保存到全局变量的部门的ID为：{}".format(app.EMP_ID))
        assert_common(self, 200, True, 10000, "操作成功", response)

    def test03_query_dep(self):
        # 发送查询员工的接口请求:
        response = self.dep_api.query_dep(app.EMP_ID, app.HEADERS)
        logging.info("查询部门的结果为：{}".format(response.json()))
        # 断言
        assert_common(self, 200, True, 10000, "操作成功", response)

    def test04_modify_dep(self):
        response = self.dep_api.modify_dep(app.EMP_ID,{"name":"杨辉"},app.HEADERS)
        logging.info("修改部门的结果为：{}".format(response.json()))
        # 断言
        assert_common(self, 200, True, 10000, "操作成功", response)

    def test05_delete_dep(self):
        response = self.dep_api.delete_dep(app.EMP_ID, app.HEADERS)
        logging.info("删除部门的结果为：{}".format(response.json()))
        # 断言
        assert_common(self, 200, True, 10000, "操作成功", response)
