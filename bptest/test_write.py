#coding=utf-8
"""
Create On 2019-12-18

@author: Ron2
"""

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

import traceback
import time
import datetime


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

        self.phoneNum = 13000000000
        self.peopleNum = 100000000000000000



    def _ReadMaxId(self):
        """
        读取最大的Id
        :return:
        """
        maxIdDic = self.collection.find_one({"bpId": {"$exists": True}}, sort=[("bpId", -1)])
        if maxIdDic == None:
            return 0

        print ("maxIdDic ==> ", maxIdDic)
        bpId = maxIdDic.get("bpId")
        return bpId


    def createRegisterJson(self):
        """
        创建一个注册用户
        :return:
        """
        self.phoneNum += 1
        self.peopleNum += 1

        dic = {}
        dic["_id"] = str(self.phoneNum)
        dic["bpId"] = int(time.time() * 1000)
        dic["peopleId"] = str(self.peopleNum)
        dic["name"] = "化以来"
        dic["pwd"] = "ddaskjf1231"
        dic["registerTimestamp"] = int(time.time())
        # dic["registerDate"] = datetime.date.today()
        # dic["registerTime"] = datetime.datetime.now().time()
        dic["registerDate"] = "2019-12-27"
        dic["registerTime"] = "11:36:06"
        dic["idfa"] = "0000-0000-0000-0000"
        dic["gameId"] = 1
        dic["clientId"] = 12
        dic["ip"] = "202.123.123.123"
        dic["device"] = "MI 8 SE"
        dic["accountType"] = 1
        dic["lastLoginTime"] = int(time.time())
        dic["lastPlayerGameId"] = 1
        return dic



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
        # self.collection.replace_one(filter={"peopleId": self.maxId}, replacement={"peopleId": self.maxId, "maxId": self.maxId + "0"})

        # beginTime = time.time()
        # countFail = 0
        # countSuccess = 0
        # for x in range(100000):
        #     if x / 10000 == 0:
        #         print("x ==> ", x)
        #     dic = self.createRegisterJson()
        #     try:
        #         self.collection.insert_one(dic)
        #         countSuccess += 1
        #     except:
        #         # traceback.print_exc()
        #         countFail += 1
        #
        #
        # print("countSuccess ===> ", countSuccess, " countFail ==> ", countFail)
        # print("costTime ==> ", time.time() - beginTime)






if __name__=="__main__":
    t = TestWrite()
    t.start()


