#coding=utf-8
"""
Create On 2019-12-18

@author: Ron2
"""

import sys, os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

import pymongo
from bptest import conf
from bptest import common


class TestRead(object):
    """
    测试MongoDB的读取
    """
    def __init__(self):
        self.client = common.createDBConnection()
        self.db = self.client[conf.DB_NAME]
        self.col = self.db["rontest"]


    def start(self):
        """
        开始测试
        :return:
        """
        self.col.find()




if __name__ == "__main__":
    t = TestRead()
    t.start()




