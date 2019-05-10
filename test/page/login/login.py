#!/usr/bin/env python 
# encoding: utf-8 
#@contact: 罗湘飞
#@time: 2019/4/25 11:23
from test.page import BasePage
from test.suite.driver import GetDriver
from appium.webdriver.common.mobileby import MobileBy
from test.suite.mobile_operating import MobileOperating
from utils.config import Config
class Login(BasePage):
    '''登录模块页面'''
    activity = "com.cmcc.cmrcs.android.ui.activities.OneKeyLoginActivity"    #一键登录模块activity
    SplashActivity = 'com.cmcc.cmrcs.android.ui.activities.SplashActivity'
    skip_button = (MobileBy.ID,"com.cmic.college:id/skip_btn")          #跳过按钮
    splash_button = (MobileBy.ID,"com.cmic.college:id/splash_btn")      #立即体验按钮
    window_title = (MobileBy.ID,"com.cmic.college:id/title")            #权限弹窗title信息【密友圈】
    window_content = (MobileBy.ID,"com.cmic.college:id/content")        #权限弹窗内容信息
    window_Confirm = (MobileBy.ID,"com.cmic.college:id/btnConfirm")        #权限弹窗确认
    permission_content = (MobileBy.ID,"com.android.packageinstaller:id/le_bottomsheet_default_content")        #权限信息
    call_permission_allow_button = (MobileBy.ID,"com.android.packageinstaller:id/permission_allow_button")      #权限弹窗权限允许按钮
    call_permission_deny_button = (MobileBy.ID,"com.android.packageinstaller:id/permission_deny_button")        #权限弹窗权限拒绝按钮
    login_phone = (MobileBy.ID,"com.cmic.college:id/tv_content")        #登录号码
    one_key_login = (MobileBy.ID,"com.cmic.college:id/one_key_login")        #一键登录
    agreement_checkbox = (MobileBy.ID,"com.cmic.college:id/agreement_checkbox")        #服务协议勾选按钮
    agreement_text = (MobileBy.ID,"com.cmic.college:id/agreement_text")        #服务协议
    privacy_protect_terms = (MobileBy.ID,"com.cmic.college:id/privacy_protect_terms")        #隐私保护政策
    login_tv_title = (MobileBy.ID,"com.cmic.college:id/tvTitle")        #登录弹窗title
    login_tv_button = (MobileBy.ID,"com.cmic.college:id/btnConfirm")        #登录弹窗确定按钮
    tv_error_content = (MobileBy.ID,"com.cmic.college:id/tv_error_content")        #无网络显示

    yaml_data = Config()
    def onekey_login_skip(self):
        '''初始化进入到一键登录页面【跳过】'''
        self.click_ele('跳过',self.skip_button,self.SplashActivity)
        self.click_ele('权限弹窗确认',self.window_Confirm,self.SplashActivity)
        for i in range(3):
            self.grant_permissions_allow()           #权限允许
    def get_phone_num(self,phone_name="LE_X620"):
        phone_number = self.yaml_data.get(phone_name)
        phone_number_1= phone_number['phone_number_1']
        phone_number_2= phone_number['phone_number_2']
        return phone_number_1,phone_number_2
if __name__ == '__main__':
    driver = GetDriver().get_driver()
    m = MobileOperating(driver)
    login = Login(driver)
    A=login.get_phone_num('LE_X620')
    print(A)
    # m.reset_app()
    # login.onekey_login_skip()


