from selenium.webdriver.support.wait import WebDriverWait
from utils import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
#from selenium.webdriver.support import expected_conditions as EC
from utils.log import logger
from test.suite.driver import GetDriver


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.logger = logger
        self.permission_allow_button = (MobileBy.ID, "com.android.packageinstaller:id/permission_allow_button")     # 全局允许权限按钮
        self.permission_deny_button = (MobileBy.ID, "com.android.packageinstaller:id/permission_deny_button")       # 全局拒绝权限按钮
        self.GrantPermissionsActivity = 'com.android.packageinstaller.permission.ui.GrantPermissionsActivity'       # 全局弹窗页面activety

    def find_element(self, loc, timeout=20, poll_frequency=0.1):
        '''元素等待，时间为20秒，刷新频率为0.1秒'''
        element = WebDriverWait(self.driver, timeout, poll_frequency).until(
            EC.presence_of_element_located(loc))
        return element

    def no_element(self,loc):
        '''判断元素是否存在'''
        try:
            self.driver.find_element(loc)
            self.logger.info('元素存在--{}'.format(loc))
            return True
        except:
            self.logger.warning('元素不存在--{}'.format(loc))
            return False

    def send_keys(self, loc, value):
        '''输入操作，自带清空操作'''
        try:
            self.find_element(loc).clear()
            self.find_element(loc).send_keys(value)
            self.logger.info('成功输入: %s' % value)
        except:
            self.logger.error("%s 页面中未能找到 %s 元素" % (self, loc))
            return False

    def click(self, loc):
        '''点击操作，如果元素存在就返回ture，不存在就返回false'''
        try:
            self.find_element(loc).click()
            self.logger.info('点击元素%s' % loc[-1])
            return True
        except:
            self.logger.error('点击元素失败:%s' % loc[-1])
            return False

    def find_elements(self, loc, index, timeout=10, poll_frequency=0.1):
        '''查询元素是否存在，loc为复数，index为值'''
        elements = WebDriverWait(self.driver, timeout, poll_frequency).until(
            EC.presence_of_all_elements_located(*loc))
        return elements[index]

    def wait_activity(self, activity):
        '''等待页面出现，提供页面的activity，等待时间为10秒'''
        if not self.driver.wait_activity(activity, timeout=10):
            self.logger.error('等待页面失败: %s' % activity)
            return False
        self.logger.info('等待页面成功: %s' % activity)
        return True

    # -------------------------------------------------------------------------------------------

    def click_ele(self, ele_name, ele, activity):
        '''点击元素操作，提供元素名称【自定义】，元素值，页面activity'''
        self.logger.info('点击【%s】' % ele_name)
        if not self.wait_activity(activity):
            self.logger.error('等待页面失败!, 未点击【%s】!' % ele_name)
            return False
        if not self.click(ele):
            self.logger.error('点击【%s】失败!' % ele_name)
            return False
        self.logger.info('点击【%s】成功!' % ele_name)
        return True

    def send_key_ele(self, ele_name, ele, text, activity):
        '''在指定元素值上，进行输入操作，提供元素名称【自定义】，元素值，输入的值，页面activity'''
        self.logger.info('在%s输入%s' % (ele_name, text))
        if not self.wait_activity(activity):
            self.logger.error('等待页面失败!, 未在%s输入%s' % (ele_name, text))
            return False
        if not self.send_keys(ele, text):
            self.logger.error('输入失败!')
        self.logger.info('输入成功')
        return True

    def check_ele_text(self, activity, ele, text):
        '''检查 元素名称的text值是否为指定text值，提供页面activity，元素值和text值'''
        self.logger.info('检查元素名称是否为【%s】' % text)
        if not self.wait_activity(activity):
            self.logger.error('等待页面失败!未进行下一步操作')
            return False
        _ele = self.find_element(ele)
        if not _ele.text == text:
            self.logger.error('当前页面元素名称为: 【%s】' % _ele.text)
            return False
        self.logger.info('页面元素【%s】对应text值【%s】正确'%(ele,text))
        return True
    def uiautomator_text_click(self,activity,text_name):
        '''uiautomator text 终极定位，提供当前activity和 界面上可点击text值'''
        self.logger.info('点击【%s】' % text_name)
        if not self.wait_activity(activity):
            self.logger.error('等待页面失败!, 未点击【%s】!' % text_name)
            return False
        if not self.click((MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("%s")'%text_name)):
            self.logger.error('点击【%s】失败!' % text_name)
            return False
        else:
            self.logger.info('点击【%s】成功!' % text_name)
            return True

    def grant_permissions_allow(self):
        '''授予权限允许'''
        self.click(self.permission_allow_button)
    def grant_permissions_deny(self):
        '''授予权限拒绝'''
        self.click(self.permission_deny_button)

if __name__ == '__main__':
    pass

