#coding=utf-8
"""
Create On 2019-12-18

@author: Ron2
"""

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

import traceback


from bptest import common
from bptest import conf


class TestWrite(object):
    """
    写入测试
    """
    def __init__(self):
        """
        """
        self.client = common.createDBConnection()
        self.db = self.client[conf.DB_NAME]
        self.maxId = 0



    def _ReadMaxId(self):
        """
        读取最大的Id
        :return:
        """
        try:
            cur = self.db.find({"_id": 0})
            doc = cur[0]
            print(doc)
            return 0
        except:
            traceback.print_exc()
            return 0


    def start(self):
        """
        :return:
        """
        self.maxId = self._ReadMaxId()
        print ("self.maxId ==> ", self.maxId)







if __name__=="__main__":
    t = TestWrite()
    t.start()


