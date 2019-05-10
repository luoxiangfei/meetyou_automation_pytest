# -*- coding: utf-8 -*-
# @Author: 罗湘飞
# @Date  : 2019/3/4/004
import time
from appium import webdriver
from utils.config import Config
from utils.log import logger
from test.suite.start_appium import run,quit_port
from test.suite.get_phone import verify_UUID

class GetDriver(object):
    def __init__(self,phone='LE_X620'):
        self.phone=phone
        self.data = Config('desired_capablities_config.yaml').get(self.phone)
        self.port = self.data.get('port')
        self.host = self.data.get('ip')
        self.uuid = self.data.get('uuid')
        self.appPackage = self.data.get('appPackage')
    def start_appium_port(self):
        '''启动APPIUM服务'''
        run(self.port, self.host)
    def close_appium_port(self):
        '''关闭APPIUM进程'''
        quit_port(self.port)
    def get_driver(self):
        '''获取到driver'''
        verify_UUID(self.uuid)
        desired_caps = {
            'platformName': self.data.get('platformName'),
            'platformVersion': self.data.get('platformVersion'),
            'deviceName': self.data.get('deviceName'),
            'appPackage': self.appPackage,
            'udid' : self.uuid,
            'appActivity': self.data.get('appActivity'),
            'noReset': self.data.get('noReset'),
            'unicodeKeyboard': self.data.get('unicodeKeyboard'),
            'resetKeyboard': self.data.get('resetKeyboard'),
            'automationName': self.data.get('automationName')
        }
        try:
            driver = webdriver.Remote('http://%s:%s/wd/hub' % (self.host, self.port), desired_caps)
            logger.info("【{}】连接【{}】成功".format(self.phone,self.appPackage))
            return driver
        except:
            logger.warning("【{}】连接【{}】异常，重启APPIUM服务再次连接".format(self.phone,self.appPackage))
            self.start_appium_port()
            try:
                driver = webdriver.Remote('http://%s:%s/wd/hub' % (self.host, self.port), desired_caps)
                return driver
            except Exception as e:
                logger.error("手机连接异常，请检查手机连接，{}".format(e))
if __name__ == '__main__':
    a=GetDriver()
    a.get_driver()
