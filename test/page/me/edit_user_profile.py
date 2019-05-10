"""
编辑个人信息
"""
from appium.webdriver.common.mobileby import MobileBy

from test.page import BasePage
from test.page.common.home_view import HomeView
from test.page.me.me_view import MeView
from test.page.me.show_user_profile import ShowUserProfileView
from utils.data import Data
from test.suite.driver import GetDriver

data = Data('me_user_profile.yaml')


class EditUserProfileView(BasePage):
    activity = 'com.cmicc.module_aboutme.ui.activity.UserProfileEditActivity'

    # 返回
    back_btn = (MobileBy.ID, 'com.chinasofti.rcs:id/left_back')
    # 保存
    save = (MobileBy.ID, 'com.chinasofti.rcs:id/tv_save')
    # 姓名
    profile_name = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("姓名")')
    # 姓名编辑框
    edit_profile_name = (MobileBy.ID, 'com.chinasofti.rcs:id/edit_contact_name')
    # 电话
    phone = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("电话")')
    # 电话编辑框
    edit_phone = (MobileBy.ID, 'com.chinasofti.rcs:id/phone')
    # 公司
    company = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("公司")')
    # 公司编辑框
    edit_company = (MobileBy.ID, 'com.chinasofti.rcs:id/edit_contact_company')
    # 职位
    position = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("职位")')
    # 职位输入框
    edit_position = (MobileBy.ID, 'com.chinasofti.rcs:id/edit_contact_job')

    def back(self):
        self.logger.info('返回[查看个人信息]页面')
        return self.click_ele('返回', self.back_btn, self.activity)

    def check_save(self):
        self.logger.info('检查[保存]按钮')
        return self.check_ele_text(self.activity, self.save, '保存')

    def check_profile_name_title(self):
        self.logger.info('检查[姓名]标题')
        return self.check_ele_text(self.activity, self.profile_name, '姓名')

    def check_phone_title(self):
        self.logger.info('检查[电话]标题')
        return self.check_ele_text(self.activity, self.phone, '电话')

    def check_company_title(self):
        self.logger.info('检查[公司]标题')
        return self.check_ele_text(self.activity, self.company, '公司')

    def check_position_title(self):
        self.logger.info('检查[职位]标题')
        return self.check_ele_text(self.activity, self.company, '职位')

    def check_edit_profile_name_before(self):
        self.logger.info('检查修改前[姓名]编辑框')
        if not data.get('profile_name').get('before') == '未设置':
            profile_name = data.get('profile_name').get('before')
        else:
            profile_name = '输入姓名'
        return self.check_ele_text(self.activity, self.edit_profile_name, profile_name)

    def check_edit_profile_name_after(self):
        self.logger.info('检查修改后[姓名]编辑框')
        if not data.get('profile_name').get('after') == '未设置':
            profile_name = data.get('profile_name').get('before')
        else:
            profile_name = '输入姓名'
        return self.check_ele_text(self.activity, self.edit_profile_name, profile_name)

    def check_edit_phone_before(self):
        self.logger.info('检查修改前[电话]编辑框')
        if not data.get('phone').get('before') == '未设置':
            phone = data.get('phone').get('before')
        else:
            phone = '输入电话'
        return self.check_ele_text(self.activity, self.edit_profile_name, phone)

    def check_edit_phone_after(self):
        self.logger.info('检查修改后[电话]编辑框')
        if not data.get('phone').get('after') == '未设置':
            phone = data.get('phone').get('after')
        else:
            phone = '输入电话'
        return self.check_ele_text(self.activity, self.edit_profile_name, phone)

    def check_edit_company_before(self):
        self.logger.info('检查修改前[公司]编辑框')
        if not data.get('company').get('before') == '未设置':
            company = data.get('company').get('before')
        else:
            company = '输入公司'
        return self.check_ele_text(self.activity, self.edit_profile_name, company)

    def check_edit_company_after(self):
        self.logger.info('检查修改后[公司]编辑框')
        if not data.get('company').get('after') == '未设置':
            company = data.get('company').get('after')
        else:
            company = '输入公司'
        return self.check_ele_text(self.activity, self.edit_profile_name, company)

    def check_edit_position_before(self):
        self.logger.info('检查修改前[职位]编辑框')
        if not data.get('position').get('before') == '未设置':
            position = data.get('position').get('before')
        else:
            position = '输入职位'
        return self.check_ele_text(self.activity, self.edit_profile_name, position)

    def check_edit_position_after(self):
        self.logger.info('检查修改后[职位]编辑框')
        if not data.get('position').get('after') == '未设置':
            position = data.get('position').get('after')
        else:
            position = '输入公司'
        return self.check_ele_text(self.activity, self.edit_profile_name, position)

    def input_profile_name(self):
        profile_name = data.get('profile_name').get('after')
        if not profile_name == '未设置':
            self.logger.info('输入姓名')
            return self.send_key_ele('姓名输入框', self.edit_profile_name, profile_name,self.activity)
        else:
            self.logger.info('数据为未设置, 只做清空，不做输入')
            return True

    def input_edit_phone(self):
        phone = data.get('phone').get('after')
        if not phone == '未设置':
            self.logger.info('输入电话')
            return self.send_key_ele('电话输入框', self.edit_profile_name, phone,self.activity)
        else:
            self.logger.info('数据为未设置, 只做清空，不做输入')
            return True

    def input_edit_company(self):
        company = data.get('company').get('after')
        if not company == '未设置':
            self.logger.info('输入公司')
            return self.send_key_ele('公司输入框', self.edit_profile_name, company,self.activity)
        else:
            self.logger.info('数据为未设置, 只做清空，不做输入')
            return True

    def input_edit_position(self):
        position = data.get('position').get('after')
        if not position == '未设置':
            self.logger.info('输入职位')
            return self.send_key_ele('职位输入框', self.edit_profile_name, position,self.activity)
        else:
            self.logger.info('数据为未设置, 只做清空，不做输入')
            return True

    def click_save(self):
        self.logger.info('点击[保存]按钮')
        return self.click_ele('保存', self.save, self.activity)


if __name__ == '__main__':
    dr = GetDriver('phone1')
    driver=dr.get_driver()
    HomeView(driver).click_me_tab()
    MeView(driver).click_user_profile()
    ShowUserProfileView(driver).click_edit()
    EditUserProfileView(driver).check_profile_name_title()