# 导包
import logging
import unittest
from utils import assert_common
from api.IHRM_login_api import TestIHRMLoginApi

# 创建unittest的类

class TestIHRMLogin(unittest.TestCase):
    # 进行初始化
    def setUp(self):
        self.login_api = TestIHRMLoginApi()

    def tearDown(self):
        pass

    # 编写登录成功函数
    def test01_login_success(self):
        response = self.login_api.login({"mobile":"13800000002","password":"123456"}, {"Content-Type":"application/json"})
        logging.info("登录成功的结果为：{}".format(response.json()))
        assert_common(self,200,True,10000,"操作成功",response)

    # 用户名错误
    def test02_mobile_is_error(self):
        # 使用封装的接口调用登录接口，并接收返回的响应数据
        response = self.login_api.login({"mobile": "13900000002", "password": "123456"},
                                        {"Content-Type": "application/json"})
        logging.info("用户名错误的结果为：{}".format(response.json()))
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    # 用户名为空
    def test03_mobile_is_empty(self):
        response = self.login_api.login({"mobile": "", "password": "123456"},
                                        {"Content-Type": "application/json"})
        logging.info("用户名为空的结果为：{}".format(response.json()))
        assert_common(self, 200, True, 10000, "操作成功", response)

    # 密码错误
    def test04_password_is_error(self):
        response = self.login_api.login({"mobile": "13800000002", "password": "12345678"},
                                        {"Content-Type": "application/json"})
        logging.info("密码错误的结果为：{}".format(response.json()))
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    # 密码为空
    def test05_password_is_empty(self):
        # 使用封装的接口调用登录接口，并接收返回的响应数据
        response = self.login_api.login({"mobile": "13800000002", "password": ""},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("密码为空的结果为：{}".format(response.json()))
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    # 多参
    def test06_more_params(self):
        response = self.login_api.login({"mobile": "13800000002", "password": "123456", "verify":"1234567890"},
                                            {"Content-Type": "application/json"})
        logging.info("多参的结果为：{}".format(response.json()))
        assert_common(self, 200, True, 10000, "操作成功", response)

    # 传入Null
    def test07_params_is_null(self):
        response = self.login_api.login(None, {"Content-Type": "application/json"})
        logging.info("传入None的结果为：{}".format(response.json()))
        assert_common(self, 200, False, 99999, "抱歉，系统繁忙，请稍后重试！", response)

    # 少参-缺少用户名
    def test08_less_params_mobile(self):
        response = self.login_api.login({"password": "123456"},
                                        {"Content-Type": "application/json"})
        logging.info("少参-缺少mobile的结果为：{}".format(response.json()))
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    # 少参-缺少密码
    def test09_less_password(self):
        response = self.login_api.login({"mobile": "13800000002"},
                                        {"Content-Type": "application/json"})
        logging.info("少参-缺少Passowrd的结果为：{}".format(response.json()))
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    # 无参
    def test10_params_is_none(self):
        response = self.login_api.login({}, {"Content-Type": "application/json"})
        logging.info("无参的结果为：{}".format(response.json()))
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    # 错误参数
    def test11_params_is_error(self):
        response = self.login_api.login({"mobiled":"13800000002","password":"123456"},
                                        {"Content-Type": "application/json"})
        logging.info("错误参数的结果为：{}".format(response.json()))
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    # 用户名大于11位
    def test12_big_11(self):
        response = self.login_api.login({"mobiled": "138000000025", "password": "123456"},
                                        {"Content-Type": "application/json"})
        logging.info("错误参数的结果为：{}".format(response.json()))
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    # 用户名小于11位
    def test13_small_11(self):
        response = self.login_api.login({"mobiled": "1380000000", "password": "123456"},
                                        {"Content-Type": "application/json"})
        logging.info("错误参数的结果为：{}".format(response.json()))
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)