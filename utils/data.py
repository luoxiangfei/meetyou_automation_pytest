"""
读取测试数据
"""

import os
from utils.file_reader import YamlReader
from utils.config import DATA_DIR


class Data:
    def __init__(self, data_f='data.yaml'):
        path = os.path.join(DATA_DIR, data_f)
        self.data = YamlReader(path).data

    def get(self, element, index=0):
        return self.data[index].get(element)


if __name__ == '__main__':
    data = Data('me_user_profile.yaml')
    if not data.get('profile_name').get('before') == '未设置':
        profile_name = data.get('profile_name').get('before')
    else:
        profile_name = '输入姓名'
    print(profile_name)