#!/usr/bin/env python 
# encoding: utf-8 
#@contact: 罗湘飞
#@time: 2019/4/23 9:44
from appium.webdriver.common.touch_action import TouchAction    #appium手机特殊操作
from selenium.webdriver.support.ui import WebDriverWait
from utils.config import REPORT_DIR
from test.suite.driver import GetDriver
from utils.log import logger
import time
import os
class MobileOperating(object):
    def __init__(self,driver):
        self.driver=driver
        self.logger=logger
    def airplane_mode(self):
        '''手机飞行模式开启'''
        self.driver.set_network_connection(1)
        self.logger.info('飞行模式开启成功')

    def wifi_mode(self):
        '''只开启wifi模式'''
        self.driver.set_network_connection(2)
        self.logger.info('wifi模式开启成功')

    def data_mode(self):
        '''只有数据网络模式'''
        self.driver.set_network_connection(4)
        self.logger.info('网络数据模式开启成功')

    def data_wifi_mode(self):
        '''wifi和数据连接一起'''
        self.driver.set_network_connection(6)
        self.logger.info('wifi和网络数据模式开启成功')

    def swipe_left(self):
        '''左滑'''
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x * 3 / 4, y / 4, x / 4, y / 4)

    def swipe_right(self):
        '''右滑'''
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x / 4, y / 4, x * 3 / 4, y / 4)

    def swipe_down(self):
        '''下滑'''
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x / 2, y * 3 / 4, x / 2, y / 4)

    def swipe_up(self):
        '''上滑'''
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x / 2, y / 4, x / 2, y * 3 / 4)

    def tap_continue(self,top_num):
        '''持续点击，需要两个参数，第一个是坐标，坐标为元组方式，第二个是点击次数'''
        for i in range(top_num):
            self.driver.tap([(295,171)], 100)
        self.logger.info('持续点击成功，点击次数为【{}】'.format(top_num))
    def long_press_operating(self,el):
        '''长按操作，需要提供参数，定位到的元素'''
        TouchAction(self.driver).long_press(el).perform()
        self.logger.info("长按元素【{}】成功".format(el))
    def reset_app(self):
        '''APP重置'''
        self.driver.reset()
        self.logger.info("APP重置成功")
    def save_screenshut(self,file_path):
        '''截图并保存，需要提供截屏路径'''
        self.driver.get_screenshot_as_file(file_path)
        self.logger.info('{}图片保存成功'.format(file_path))
    def toast(self,toast_value):
        '''获取toast信息'''
        message = '//*[@text=\'{}\']'.format(toast_value)
        try:
            toast_text=WebDriverWait(self.driver,5).until(lambda x:x.find_element_by_xpath(message))
            logger.info('{}获取成功'.format(toast_text.text))
            return True
        except:
            logger.info('{}获取失败'.format(message))
            return False
    def h5_contexts(self):
        '''切换H5页面操作'''
        contexts =self.driver.contexts
        print (contexts)
        self.driver.switch_to.context("WEBVIEW_chrome")
        print (self.driver.current_context)

if __name__ == '__main__':
    #GetDriver().close_appium_port()
    driver=GetDriver().get_driver()
    driver.implicitly_wait(20)
    m=MobileOperating(driver)
    def test_long():
        '''测试长按'''
        time.sleep(5)
        driver.find_element_by_id("com.cmic.college:id/tvContact").click()
        driver.find_element_by_id("com.cmic.college:id/tv_manage").click()
        elm=driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[@resource-id='com.cmic.college:id/rv_content']/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]")
        time.sleep(2)
        m.long_press_operating(elm)
    # test_long()
    def test_swipe():
        '''测试滑动操作'''
        time.sleep(5)
        m.swipe_down()
        time.sleep(5)
        m.swipe_up()
        # time.sleep(5)
        # m.swipe_left()
        # time.sleep(5)
        # m.swipe_left()
        # time.sleep(5)
        # m.swipe_right()
        # time.sleep(5)
        # m.swipe_right()
    #test_swipe()
    def test_top():
        '''测试多次点击'''
        time.sleep(4)
        driver.find_element_by_id("com.cmic.college:id/tvMe").click()
        driver.find_element_by_id("com.cmic.college:id/setting").click()
        time.sleep(5)
        m.tap_continue(7)
        time.sleep(3)
    #test_top()
    def chongzhi_APP():
        '''测试重置APP'''
        m.reset_app()
    #chongzhi_APP()
    def baocun_tupian():
        '''测试图片保存'''
        path=os.path.join(REPORT_DIR,"picture_save")
        path_new=os.path.join(path,"luo2.png")
        print(path_new)
        m.save_screenshut(path_new)
    #baocun_tupian()
    def test_toast():
        m.airplane_mode()
        time.sleep(4)
        driver.find_element_by_id("com.cmic.college:id/tvMe").click()
        driver.find_element_by_id("com.cmic.college:id/activity_center").click()
        m.toast("网络不可用，请检查网络设置")
    #test_toast()
    def test_H5():
        driver.find_element_by_id("com.cmic.college:id/tvMe").click()
        driver.find_element_by_id("com.cmic.college:id/activity_center").click()
        m.h5_contexts()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]').click()
    test_H5()
    time.sleep(5)
    driver.quit()

