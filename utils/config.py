"""
读取配置文件
"""
import os
from utils.file_reader import YamlReader

BASE_DIR = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_DIR = os.path.join(BASE_DIR, 'config')
APK_DIR = os.path.join(BASE_DIR, 'apk')
LOG_DIR = os.path.join(BASE_DIR, 'log')
REPORT_DIR = os.path.join(BASE_DIR, 'report')
DATA_DIR = os.path.join(BASE_DIR, 'data')
TEST_DIT = os.path.join(BASE_DIR, 'test')
#---------------------------------------
CASE_DIT = os.path.join(TEST_DIT, 'case')
REPORT_ORIGINAL_DIR = os.path.join(REPORT_DIR ,'report_original')  # 测试报告原件路径
REPORT_FINAL_DIR = os.path.join(REPORT_DIR ,'report_final')  # 渲染完成后最终报告文件路径


class Config:
    def __init__(self, config='desired_capablities_config.yaml'):
        path = os.path.join(CONFIG_DIR, config)
        self.config = YamlReader(path).data

    def get(self, element, index=0):
        return self.config[index].get(element)
if __name__ == '__main__':
    c=Config("other_config.yaml")
    a=c.get("pc_screencap_path")
    print(a)
