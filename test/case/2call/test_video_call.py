# -*- coding: utf-8 -*-
# @Author: 罗湘飞
# @Time  : 2019/4/29 0029 15:53

import time
import allure
import pytest
import unittest
from test.case import assert_false,assert_ture
from test.page.add_list.home_page import AddressList,HomeView
from test.page.common.video_call_page import VideoCallPage
from test.page.common.personal_details_page import PersonalDetailsPage
from test.suite.mobile_operating import MobileOperating
from test.suite.driver import GetDriver
from utils.log import logger


num=(i for i in range(1,10000))
@allure.feature('登录模块测试用例')
class TestVideoCall(object):
    def setup(self):
        logger.info("========登录模块测试用例执行开始========【{}】========".format(next(num)))
        self.driver_x620 = GetDriver().get_driver()                 #获取driver1，默认手机LE_X620
        self.m_x620 = MobileOperating(self.driver_x620)
        self.address_x620 = AddressList(self.driver_x620)
        self.home_x620 = HomeView(self.driver_x620)
        self.video_x620 = VideoCallPage(self.driver_x620)
        self.personal_page = PersonalDetailsPage(self.driver_x620)
    def teardown(self):
        logger.info("=============登录模块测试用例执行结束=============")
        self.driver_x620.quit()

    @allure.story('验证测试视频通话对方接通后页面')
    def test_video_1(self):
        logger.info('测试视频通话对方接通后页面')
        driver_pixel = GetDriver("PIXEL_XL").get_driver()           #获取driver2，指定设备PIXEL_XL
        time.sleep(5)
        try:
            self.home_x620.click_address_list_tab()                     #点击通讯录
            time.sleep(2)
            self.address_x620.uiautomator_text_click(self.address_x620.activity,'13694245189')     #点击手机号码为13694245189号码联系人
            self.address_x620.click_ele('拨打视频通话按钮',self.personal_page.video_call_btn,self.personal_page.activity)
            result1 = self.address_x620.check_ele_text(self.video_x620.activity,self.video_x620.video_tv_text,'正在等待对方接听...')
            assert_ture(self.driver_x620,result1)                #为接听前  验证是不是显示【正在等待对方接听...】
            video_pixel = VideoCallPage(driver_pixel)
            video_pixel.click_ele('接听按钮',video_pixel.ivVideoAnswer,video_pixel.activity)
            result2=self.address_x620.no_element(self.video_x620.video_tv_text)
            assert_false(self.driver_x620,result2)               #接听成功后，验证【正在等待对方接听...】是否不存在
            time.sleep(10)
            driver_pixel.quit()
        except:
            driver_pixel.quit()
if __name__ == '__main__':
    unittest.main()