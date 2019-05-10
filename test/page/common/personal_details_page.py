# -*- coding: utf-8 -*-
# @Author: 罗湘飞
# @Time  : 2019/4/29 0029 14:18
import time
from test.page import BasePage
from test.suite.driver import GetDriver
from appium.webdriver.common.mobileby import MobileBy
from test.suite.mobile_operating import MobileOperating
from test.page.common.home_view import HomeView
class PersonalDetailsPage(BasePage):
    activity = 'com.cmcc.cmrcs.android.ui.activities.ContactDetailActivity'             #个人详情页面activity
    left_back_btn=(MobileBy.ID,"com.cmic.college:id/left_back_btn")                     #返回按钮
    right_delect_btn=(MobileBy.ID,"com.cmic.college:id/right_delect_btn")               #好友删除按钮
    video_call_btn=(MobileBy.ID,"com.cmic.college:id/iv_netcall")                       #视频通话
    call_btn=(MobileBy.ID,"com.cmic.college:id/iv_message")                             #电话



