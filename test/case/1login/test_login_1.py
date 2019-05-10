#!/usr/bin/env python 
# encoding: utf-8 
#@contact: 罗湘飞
#@time: 2019/4/20 21:34

import allure
import pytest
from test.case import assert_ture,assert_false
from test.page.login.login import Login
from test.suite.mobile_operating import MobileOperating
from test.suite.driver import GetDriver
from utils.log import logger
from test.page.common.home_view import HomeView
import time


num=(i for i in range(1,10000))
@allure.feature('登录模块测试用例')
class TestLogin(object):
    def setup(self):
        logger.info("========登录模块测试用例执行开始========【{}】========".format(next(num)))
        self.driver = GetDriver().get_driver()
        self.driver.implicitly_wait(20)
        self.m = MobileOperating(self.driver)
        self.m.data_mode()                              #确保手机使用数据网络状态
        self.login = Login(self.driver)
    def teardown(self):
        logger.info("=============登录模块测试用例执行结束=============")
        self.driver.quit()

    @allure.story('验证登录号码是否为指定号码')
    def test_login_1(self):
        logger.info('验证登录号码是否为指定号码')
        self.m.reset_app()          #重置APP操作
        self.login.onekey_login_skip()
        result = self.login.check_ele_text(self.login.activity, self.login.login_phone,str(self.login.get_phone_num()[0]))
        assert_ture(result,self.driver)

    @allure.story('验证断网情况下登录页面显示')
    def test_login_2(self):
        logger.info('验证断网情况下登录页面显示')
        self.m.reset_app()          #重置APP操作
        self.login.onekey_login_skip()
        self.m.airplane_mode()
        time.sleep(2)
        result = self.login.check_ele_text(self.login.activity, self.login.tv_error_content, '网络不可用，请检查网络设置')
        assert_ture(self.driver, result)
        self.m.data_mode()
        time.sleep(2)
    @allure.story('验证登录成功进入主页是否成功')
    def test_login_3(self):
        logger.info('验证登录成功进入主页是否成功')
        self.m.reset_app()  # 重置APP操作
        self.login.onekey_login_skip()
        self.login.click_ele('一键登录',self.login.one_key_login,self.login.activity)
        self.login.click_ele('登录弹窗确定',self.login.login_tv_button,self.login.activity)
        time.sleep(15)
        self.login.grant_permissions_allow()
        self.login.click_ele('通讯录tab',HomeView.address_list,HomeView.activity)
        self.login.click_ele('通讯录tab',HomeView.address_list,HomeView.activity)
        result=self.login.check_ele_text(HomeView.activity,HomeView.address_list,'通讯录')
        assert_ture(self.driver,result)

if __name__ == '__main__':
    pytest.main(['-s', '-q', 'test_login_1.py','--alluredir', './report/xml'])