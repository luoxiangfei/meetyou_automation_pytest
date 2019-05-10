#!/usr/bin/env python 
# encoding: utf-8 
#@contact: 罗湘飞
#@time: 2019/4/20 14:01

import warnings
import os
import pytest
import subprocess
import allure
import time
from utils.mail import send_email
from utils.config import CASE_DIT,REPORT_ORIGINAL_DIR,REPORT_FINAL_DIR
from utils.zip_file import zip_files
from test.suite.get_test_suite import GetTestSuite_HTML
class main_test(object):
    def __init__(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.testcase_path=CASE_DIT
        self.html_title="密友圈测试用例执行结果"
        self.testcase_file ="%s--test_report"%time.strftime("%Y%m%d-%H%M")
        self.report_original_name = os.path.join(REPORT_ORIGINAL_DIR,self.testcase_file)    #测试报告原件名称路径
        self.report_final_name = os.path.join(REPORT_FINAL_DIR,self.testcase_file)    #测试报告最终文件路径
        self.zip_name = '{}.zip'.format(self.testcase_file)
        self.zip_file=os.path.join(REPORT_FINAL_DIR,self.testcase_file)
        self.email_zip_file = os.path.join(REPORT_FINAL_DIR,self.zip_name)
    def run_test(self):
        '''总程序执行'''
        p = subprocess.Popen('pytest -s -v {} --alluredir {}'.format(CASE_DIT,self.report_original_name))
        p.wait()
        cmd_new='allure generate {} -o {}'.format(self.report_original_name, self.report_final_name)
        os.system(cmd_new)
        zip_files(self.zip_file,self.email_zip_file)
        send_email().email_init(self.email_zip_file,self.zip_name)
if __name__ == '__main__':
    m=main_test()
    m.run_test()