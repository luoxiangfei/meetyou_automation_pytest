"""
查看个人信息
"""
from appium.webdriver.common.mobileby import MobileBy

from test.page import BasePage
from utils.data import Data


class ShowUserProfileView(BasePage):
    activity = 'com.cmicc.module_aboutme.ui.activity.UserProfileShowActivity'

    # 返回按钮
    back_btn = (MobileBy.ID, 'com.chinasofti.rcs:id/left_back')
    # 编辑
    edit = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("编辑")')
    # 姓名
    profile_name = (MobileBy.ID, 'com.chinasofti.rcs:id/profile_name')
    # 头像(未做检查)
    profile_photo = (MobileBy.ID, 'com.chinasofti.rcs:id/profile_photo')
    # 电话标题
    phone = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("电话")')
    # 电话号码
    phone_num = (MobileBy.ID, 'com.chinasofti.rcs:id/tv_phone_number')
    # 公司标题
    company = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("公司")')
    # 公司名称
    company_value = (MobileBy.ID, 'com.chinasofti.rcs:id/tv_school')
    # 职位标题
    position = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("职位")')
    # 职位名称
    position_value = (MobileBy.ID, 'com.chinasofti.rcs:id/tv_profession')
    # 邮箱标题
    email = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("邮箱")')
    # 邮箱名称
    email_value = (MobileBy.ID, 'com.chinasofti.rcs:id/tv_email')
    # 分享名片
    share_card = (MobileBy.ID, 'com.chinasofti.rcs:id/btn_share_card')

    def back(self):
        self.logger.info('返回[我]页面')
        return self.click_ele('返回', self.back_btn, self.activity)

    def check_value(self, activity, loc, text='', status=None, data_field_name=None):
        if not status:
            return self.check_ele_text(activity, loc, text)
        elif status not in ('after', 'before'):
            self.logger.error('数据状态错误:%s [after, before]')
            return False
        if Data('me_user_profile.yaml').get(data_field_name) is None:
            self.logger.error('取数据时错误: %s' % data_field_name)
            return False
        status_value = Data('me_user_profile.yaml').get(data_field_name).get(status)
        return self.check_ele_text(self.activity, self.profile_name, status_value)

    def check_edit(self):
        self.logger.info('检查[编辑]按钮')
        return self.check_value(self.activity, self.edit, '编辑')

    def check_phone_title(self):
        self.logger.info('检查[电话]标题')
        return self.check_value(self.activity, self.phone, '电话')

    def check_company_title(self):
        self.logger.info('检查[公司]标题')
        return self.check_value(self.activity, self.company, '公司')

    def check_position_title(self):
        self.logger.info('检查[职位]标题')
        return self.check_value(self.activity, self.position, '职位')

    def check_email_title(self):
        self.logger.info('检查[邮箱]标题')
        return self.check_value(self.activity, self.email, '邮箱')

    def check_share_card(self):
        self.logger.info('检查[分享名片]标题')
        return self.check_value(self.activity, self.share_card, '分享名片')

    def check_profile_name_before(self):
        self.logger.info('检查修改前的用户姓名')
        return self.check_value(self.activity, self.profile_name, status='before', data_field_name='profile_name')

    def check_profile_value_after(self):
        self.logger.info('检查修改后的用户姓名')
        return self.check_value(self.activity, self.profile_name, status='after', data_field_name='profile_name')

    def check_phone_num_before(self):
        self.logger.info('检查修改前的电话号码')
        return self.check_value(self.activity, self.phone_num, status='before', data_field_name='phone')

    def check_phone_num_after(self):
        self.logger.info('检查修改后的电话号码')
        return self.check_value(self.activity, self.phone_num, status='after', data_field_name='phone')

    def check_company_value_before(self):
        self.logger.info('检查修改前的公司名称')
        return self.check_value(self.activity, self.company_value, status='before', data_field_name='company')

    def check_company_value_after(self):
        self.logger.info('检查修改后的公司名称')
        return self.check_value(self.activity, self.company_value, status='after', data_field_name='company')

    def check_position_value_before(self):
        self.logger.info('检查修改前的职位名称')
        return self.check_value(self.activity, self.position_value, status='before', data_field_name='position')

    def check_position_value_after(self):
        self.logger.info('检查修改后的职位名称')
        return self.check_value(self.activity, self.position_value, status='after', data_field_name='position')

    def check_email_value_before(self):
        self.logger.info('检查修改前的邮箱地址')
        return self.check_value(self.activity, self.email_value, status='before', data_field_name='email')

    def check_email_value_after(self):
        self.logger.info('检查修改后的邮箱地址')
        return self.check_value(self.activity, self.email_value, status='after', data_field_name='email')

    def click_edit(self):
        self.logger.info('点击[编辑]按钮')
        return self.click_ele('编辑', self.edit, self.activity)

    def click_share_card(self):
        self.logger.info('点击[分享名片]按钮')
        return self.click_ele('分享名片', self.share_card, self.activity)