# 生成测试报告时，是要先执行测试用例的
# 我们可以把测试用例添加到测试套件中，然后执行测试套件生成测试报告

# 1 导包
import os
import unittest
import HTMLTestRunner_PY3
from script.test_ihrm_department import TestIHRMDepartment
from script.test_ihrm_login import TestIHRMLogin
import time

# os.path.dirname(os.path.abspath(__file__)) 可以定位到当前项目的目录


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2 创建测试套件
suite1 = unittest.TestSuite()
suite2 = unittest.TestSuite()
# 3 将测试用例添加到测试套件
suite1.addTest(unittest.makeSuite(TestIHRMLogin))
suite2.addTest(unittest.makeSuite(TestIHRMDepartment))

# 4 定义测试报告的目录和报告名称
report_path1 = BASE_DIR + "/report/IHRMLogin{}.html"
report_path2 = BASE_DIR + "/report/IHRMDepartment{}.html"
# 5 使用HTMLTestRunner_PY3生成测试报告
with open(report_path1, mode='wb') as f:
    # 实例化HTMLTestRunner_PY3
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f, verbosity=1, title="ihrm的登录功能测试",
                                               description="这是一个更加美观的报告")
    # 使用实例化的runner运行测试套件，生成测试报告
    runner.run(suite1)

with open(report_path2, mode='wb') as f:
    # 实例化HTMLTestRunner_PY3
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f, verbosity=1, title="ihrm的部门测试",
                                               description="这是一个更加美观的报告")
    # 使用实例化的runner运行测试套件，生成测试报告
    runner.run(suite2)