# -*- coding: utf-8 -*-
# @Author: 罗湘飞
# @Time  : 2019/4/30 0030 15:50

import unittest
class UnittestPage(unittest.TestCase):
    def setUp(self):
        print("kaishi")
    def tearDown(self):
        print("sdfsdf")
    def test_1(self):
        try:
            self.assertTrue(0)
            print('成功')
        except:
            print('失败')
if __name__ == '__main__':
    UnittestPage().test_1()