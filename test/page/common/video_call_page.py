# -*- coding: utf-8 -*-
# @Author: 罗湘飞
# @Time  : 2019/4/29 0029 15:31

import time
from test.page import BasePage
from test.suite.driver import GetDriver
from appium.webdriver.common.mobileby import MobileBy
from test.suite.mobile_operating import MobileOperating
from test.page.common.home_view import HomeView
class VideoCallPage(BasePage):
    activity = "com.chinamobile.app.yuliao_business.ui.activity.VoiceCallActivity"
    video_tv_name = (MobileBy.ID,'com.cmic.college:id/video_tv_name')                #通话对象名称
    video_tv_number = (MobileBy.ID,'com.cmic.college:id/video_tv_number')                #通话对象号码
    #通话过程中文案显示
    video_tv_text = (MobileBy.XPATH,'//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.'
                     'FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.Line'
                     'arLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.Li'
                     'nearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[3]')
    video_iv_term = (MobileBy.ID,'com.cmic.college:id/video_iv_term')                #通话挂断按钮
    ivVideoAnswer = (MobileBy.ID,'com.cmic.college:id/ivVideoAnswer')                #被叫方接通按钮
    ivCancel = (MobileBy.ID,'com.cmic.college:id/ivCancel')                           #被叫方挂断按钮
    tvUserName = (MobileBy.ID,'com.cmic.college:id/tvUserName')                       #被叫查看主叫名称
    tvUserPhone = (MobileBy.ID,'com.cmic.college:id/tvUserPhone')                     #被叫查看主叫号码
    textHint = (MobileBy.ID,'com.cmic.college:id/textHint')                          #被叫查看邀请文案

