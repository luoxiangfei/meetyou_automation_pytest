#!/usr/bin/env python 
# encoding: utf-8 
#@contact: 罗湘飞
#@time: 2019/4/20 21:16
import os
from utils.HTMLTestRunner import HTMLTestRunner
from utils.config import REPORT_DIR
import unittest
def GetTestSuite_HTML(testcase_path,pattern,html_title,html_des="脚本执行结果"):
    discover=unittest.defaultTestLoader.discover(testcase_path,pattern=pattern,top_level_dir=None)
    report = os.path.join(REPORT_DIR, 'report.html')
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title=html_title, description=html_des)
        runner.run(discover)
if __name__ == '__main__':
    testcase_path=r"D:/python_project/meetyou_automation/test/case/"
    pattern='test_*.py'
    html_title="密友圈自动化测试_罗"
    GetTestSuite_HTML(testcase_path,pattern,html_title)