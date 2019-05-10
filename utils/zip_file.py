# -*- coding: utf-8 -*-
# @Author: 罗湘飞
# @Time  : 2019/5/9 0009 16:58
import os
from utils.log import logger
import zipfile

from utils.log import logger
import zipfile
def zip_file(zip_dir,zip_name,way="w"):
    '''压缩文件,单个文件'''
    try:
        z = zipfile.ZipFile(zip_name, way, zipfile.ZIP_STORED)  # 打包，zipfile.ZIP_STORED是默认参数
        z.write(zip_dir)
        logger.info('添加压缩文件{}成功'.format(zip_name))
    except Exception as e:
        logger.error('添加压缩文件{}错误，{}'.format(zip_name,e))
def zip_files(zip_dir,zip_name,way="w"):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    try:
        zip = zipfile.ZipFile(zip_name,"w",zipfile.ZIP_DEFLATED)
        for path,dirnames,filenames in os.walk(zip_dir):
            # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
            fpath = path.replace(zip_dir,'')
            for filename in filenames:
                zip.write(os.path.join(path,filename),os.path.join(fpath,filename))
        zip.close()
        logger.info('添加压缩文件{}成功'.format(zip_name))
    except Exception as e:
        logger.error('添加压缩文件{}错误，{}'.format(zip_name, e))


if __name__ == '__main__':
    zip_file('e:\\luo_java',"luo.zip")