# -*- coding: utf-8 -*-
# @Author: 罗湘飞
# @Date  : 2019/3/4/004


import os
from utils.log import logger
def getDeviceName():
    """获取手机唯一标识"""
    deviceName=os.popen("adb shell getprop ro.boot.serialno")
    return deviceName.read().replace('\n', '')
def getVersion():
    """获取手机系统版本"""
    version=os.popen("adb shell getprop ro.build.version.release")
    return version.read().replace('\n', '')
def getUUID():
    uuid_list=[]
    cmd="adb devices"
    result = os.popen(cmd).readlines()
    result.remove(result[0])
    result.pop()
    for i in result:
        # print(i.replace())
        str1=i.find("\t")
        uuid_list.append(i[0:str1])
    return uuid_list
def verify_UUID(uuid):
    if uuid in getUUID():
        logger.info('【{}】设备连接正常'.format(uuid))
    else:
        logger.error('【{}】设备不存在'.format(uuid))

if __name__ == '__main__':
    verify_UUID("LE67A06290097275")