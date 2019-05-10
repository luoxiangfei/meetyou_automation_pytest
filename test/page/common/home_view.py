"""
主界面
"""
from appium.webdriver.common.mobileby import MobileBy
from test.page import BasePage
from test.suite.driver import GetDriver


class HomeView(BasePage):
    activity = 'com.cmcc.cmrcs.android.ui.activities.HomeActivity'
    # 通讯录tab
    address_list = (MobileBy.ID, 'com.cmic.college:id/tvContact')
    # 密友tab
    meetyou = (MobileBy.ID, 'com.cmic.college:id/tvContact')
    # 合家欢
    contact = (MobileBy.ID, 'com.cmic.college:id/dynamic_tab')
    # 我tab
    me = (MobileBy.ID, 'com.cmic.college:id/tvMe')
    #登录进入，权限申请【允许】
    permission_allow = (MobileBy.ID, 'com.android.packageinstaller:id/permission_allow_button')
    #登录进入，权限申请【拒绝】
    permission_deny = (MobileBy.ID, 'com.android.packageinstaller:id/permission_deny_button')

    def click_me_tab(self):
        return self.click_ele('我', self.me, self.activity)

    def click_address_list_tab(self):
        return self.click_ele('通讯录', self.address_list, self.activity)

    def click_workbench_tab(self):
        return self.click_ele('密友tab', self.meetyou, self.activity)

    def click_contact_tab(self):
        return self.click_ele('合家欢', self.contact, self.activity)


if __name__ == '__main__':
    driver = GetDriver("phone1").get_driver()
    h=HomeView(driver).click_me_tab()
    print(h)