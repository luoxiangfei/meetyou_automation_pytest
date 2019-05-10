#!/usr/bin/env python 
# encoding: utf-8 
#@contact: 罗湘飞
#@time: 2019/4/21 16:06

import subprocess
import socket
import os
import time
from utils.log import logger
from utils.config import LOG_DIR
def start_appium(host,port):
    '''启动APPIUM服务'''
    time_str = time.strftime("%Y%m%d")
    port_new=str(port+1)
    cmd='start /b appium -a {host} -p {port} -bp {port_new}'.format(host=host,port=port,port_new=port_new)
    #subprocess.Popen(cmd, shell=True, stdout=open(LOG_DIR+'/start_appium_log/' + str(port) + '.log', 'a'), stderr=subprocess.STDOUT)
    subprocess.Popen(cmd, shell=True, stdout=open('{}/start_appium_log/{}----{}.log'.format(LOG_DIR,time_str,str(port)), 'a'), stderr=subprocess.STDOUT)
    logger.info("appium服务{}，端口{}启动成功".format(host,port))

def check_port(host, port):
    """检测指定的端口是否被占用"""
    #创建socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.shutdown(2)
    except OSError:
        logger.info('port %s不存在，可以使用 ' %port)
        return True
    else:
        logger.error('port %s 已经存在' % port)
        return False
def quit_port(port):
    '''关闭当前端口'''
    cmd_new = "netstat -aon | findstr %s"%port
    result = os.popen(cmd_new).read()
    if str(port) and "LISTENING" in result:
        result1 = str(result).replace(' ','')
        str1=result1.find("LISTENING")+len("LISTENING")
        str3=result1.find("\n")
        str2=result1[str1:str3].replace('\n','')
        cmd_kill = 'taskkill -f -pid %s' % str2
        os.popen(cmd_kill)
        logger.info("{}端口下的进程{}关闭成功".format(port,str2))

    else:
        logger.error("没有该端口下的进程")



def run(port,host="127.0.0.1"):
    '''启动APPIUMsever'''
    if check_port(host,port):
        time.sleep(1)
        start_appium(host,port)
    else:
        quit_port(port)
        time.sleep(1)
        start_appium(host,port)

if __name__ == '__main__':
    port=4723
    run(port)
    time.sleep(3)
    quit_port(4723)
