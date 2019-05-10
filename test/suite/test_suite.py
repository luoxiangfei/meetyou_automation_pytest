import os
from unittest import TestLoader, TestSuite
from test.case.me_test import TestMe
from utils.HTMLTestRunner import HTMLTestRunner
from utils.config import REPORT_DIR


def all_test():
    me = TestLoader().loadTestsFromTestCase(TestMe)
    return TestSuite([me])


report = os.path.join(REPORT_DIR, 'report.html')
with open(report, 'wb') as f:
    runner = HTMLTestRunner(f, verbosity=2, title='和飞信自动化测试', description='脚本执行结果')
    runner.run(all_test())
