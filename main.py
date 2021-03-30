import unittest
import os
from HTMLTestRunner import HTMLTestRunner
from Common.dir_config import *

s = unittest.TestSuite()
loader = unittest.TestLoader()
s.addTests(loader.discover(testcase_dir))

fp = open(htmlreport_dir + "/autoTest_report.html", "wb")
runner = HTMLTestRunner(
    stream=fp,
    title="单元测试报告",
    description="单元测试报告",
    # tester="Cobb"
)
runner.run(s)
# 日志生成还有问题
#加一条备注123

# 为什么登录页执行except时会执行到封装里except的截图操作


# pytest的运行命令
# pytest --reruns 2 --reruns-delay 5 -s --junitxml=Outputs/Reports/report.xml --html=Outputs/Reports/html_report.html
