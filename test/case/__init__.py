import os
import unittest
import time

from test.suite.driver import GetDriver
from utils.config import REPORT_DIR
from utils.log import logger
from test.suite.mobile_operating import MobileOperating

def save_picture(driver):
    '''保存截图到指定目录'''
    path1 = os.path.join(REPORT_DIR, "picture_save")
    dir_name ="%s"%time.strftime("%Y%m%d")
    try:
        os.mkdir(path1 + "\\"+dir_name)
        path_new_dir = os.path.join(path1,dir_name)
    except:
        path_new_dir = os.path.join(path1, dir_name)
    path_new = os.path.join(path_new_dir,time.strftime("%H%M%S")+".png")
    MobileOperating(driver).save_screenshut(path_new)
def assert_ture(driver,expr):
    '''判断正确，如果错误就截图到指定目录'''
    if not expr:
        save_picture(driver)
        raise Exception('判断【{}】正确-----失败'.format(expr))

def assert_false(driver,expr):
    '''判断错误，如果正确就截图到指定目录'''
    if expr:
        save_picture(driver)
        raise Exception('判断【{}】失败-----失败'.format(expr))


if __name__ == '__main__':
    # unittest.main()
    driver = GetDriver().get_driver()
    save_picture(driver)
    driver.quit()