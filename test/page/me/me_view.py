from appium.webdriver.common.mobileby import MobileBy
from test.page.common.home_view import HomeView
from test.page import BasePage
from test.suite.driver import GetDriver

class MeView(BasePage):
    """
    我页面
    """

    activity = 'com.cmcc.cmrcs.android.ui.activities.HomeActivity'
    # 标题
    title = (MobileBy.ID, 'com.cmic.college:id/tvMe')
    # 个人资料
    user_profile = (MobileBy.ID, 'com.cmic.college:id/my_profile_card_layout')
    # 免流
    free_flow = (MobileBy.ID, 'com.cmic.college:id/ll_freeflow')
    # 签到
    sigin_in = (MobileBy.ID, 'com.cmic.college:id/iv_free_call_clock_in')
    # 看点新闻
    news = (MobileBy.ID, 'com.cmic.college:id/rlNews')
    # 活动中心
    activity_center = (MobileBy.ID, 'com.cmic.college:id/activity_center')
    # 卡券
    coupons = (MobileBy.ID, 'com.cmic.college:id/web_hall_coupons')
    # 网上营业厅
    online_hall = (MobileBy.ID, 'com.cmic.college:id/web_hall_page')
    # 邀请有奖
    invite_prize = (MobileBy.ID, 'com.cmic.college:id/share_app')
    # 帮助与反馈
    feedback = (MobileBy.ID, 'com.cmic.college:id/feedback')
    # 设置
    setting_app = (MobileBy.ID, 'com.cmic.college:id/setting')

    def check_title(self):
        '''检查当前模块是否为我'''
        self.logger.info('检查当前页面title是否为[我]')
        return self.check_ele_text(self.activity, self.title, '我')

    def click_user_profile(self):
        self.logger.info('点击[查看并编辑个人资料]按钮')
        return self.click_ele('查看并编辑个人资料', self.user_profile, self.activity)

    def check_free_flow(self):
        self.logger.info('点击[查看并编辑个人资料]按钮')
        return self.click_ele('查看并编辑个人资料', self.user_profile, self.activity)


if __name__ == '__main__':
    driver = GetDriver().get_driver()
    HomeView(driver).click_me_tab()
    MeView(driver).check_title()


