# -*- coding: utf-8 -*-
# @Author: 罗湘飞
# @time  : 2019/4/29 10:34
import time
from test.page import BasePage
from test.suite.driver import GetDriver
from appium.webdriver.common.mobileby import MobileBy
from test.suite.mobile_operating import MobileOperating
from test.page.common.home_view import HomeView
class AddressList(BasePage):
    activity = 'com.cmcc.cmrcs.android.ui.activities.HomeActivity'              #页面acitvity
    #页面标题

    add_title = (MobileBy.XPATH,"//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLay"
                                "out[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.Re"
                                "lativeLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.suppo"
                                "rt.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/an"
                                "droid.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]")
    add_seek = (MobileBy.ID,'com.cmic.college:id/action_search')                #通讯录页面搜索按钮
    add_news_entrance = (MobileBy.ID,'com.cmic.college:id/action_search')        #通讯录页面消息入口
    add_unlimited_length_title = (MobileBy.ID,'com.cmic.college:id/tv_n')            #通讯录不限时长title
    #add_arrows= (MobileBy.ID,'com.cmic.college:id/iv_arrow')                        #家庭网和联系人箭头（复数）
    add_home_network= (MobileBy.XPATH,'//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.Fra'
                                      'meLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.'
                                      'widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]'
                                      '/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widge'
                                      't.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/an'
                                      'droid.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.'
                                      'widget.RelativeLayout[2]')                        #家庭网
    add_linkman= (MobileBy.ID,'com.cmic.college:id/ll_root')                        #联系人
    def home_network_click(self):
        '''家庭网箭头点击'''
        try:
            self.click(self.add_home_network)
        except:
            self.logger.error("获取元素失败")
    def linkman_click(self):
        '''联系人箭头点击'''
        try:
            self.click(self.add_linkman)
        except:
            self.logger.error("获取元素失败")


if __name__ == '__main__':
    def test():
        driver = GetDriver().get_driver()
        m = MobileOperating(driver)
        try:
            add = AddressList(driver)
            HomeView(driver).click_address_list_tab()
            time.sleep(4)
            add.uiautomator_text_click(add.activity,'13694245189')
            print("OK")
            time.sleep(5)
            driver.quit()
        except:
            print('错误了')
            driver.quit()
    test()



