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
        self.client = common.createDBConnection_defaultDB()
        self.db = self.client[conf.USER_DB_NAME]
        self.collection = self.db[conf.USER_DB_BP_USER_COLLECTION]
        self.maxId = ""


    def _ReadMaxId(self):
        """
        读取最大的Id
        :return:
        """
        maxIdDic = self.collection.find_one({"peopleId": {"$exists": True}}, sort=[("_id", -1)])
        print ("maxIdDic ==> ", maxIdDic)
        peopleId = maxIdDic.get("peopleId")
        return peopleId


    def start(self):
        """
        :return:
        """
        self.maxId = self._ReadMaxId()
        print ("self.maxId ==> ", self.maxId)

        # self.maxId += 1
        # # self.doc.insert({"_id": self.maxId, "title": "Ron"})
        # # self.doc.insert({"_id": 0, "maxId": self.maxId})
        # self.collection.replace_one(filter={"_id": self.maxId}, replacement={"_id": self.maxId, "title": "Ron"})
        self.collection.replace_one(filter={"peopleId": self.maxId}, replacement={"peopleId": self.maxId, "maxId": self.maxId + "0"})









if __name__=="__main__":
    t = TestWrite()
    t.start()


