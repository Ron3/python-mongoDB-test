#coding=utf-8
"""
Create On 2019-12-18

@author: Ron2
"""

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

import time
import random
import pymongo
from bptest import conf
from bptest import common



class TestRead(object):
    """
    测试MongoDB的读取
    """
    def __init__(self):
        self.client = common.createDBConnection_defaultDB()
        self.db = self.client[conf.USER_DB_NAME]
        self.collection = self.db[conf.USER_DB_BP_USER_COLLECTION]
        self.maxId = ""

        self.phoneNum = 13000000000
        self.peopleNum = 100000000000000000


    def start(self):
        """
        开始测试
        :return:
        """
        # 测试修改修改名字
        # ar = []
        # beginTime = time.time()
        # for x in range(1000):
        #     peopleId = self.peopleNum + random.randint(12000, 91000)
        #     peopleId = str(peopleId)
        #     dic = self.collection.find_one({"peopleId": peopleId})
        #     ar.append(dic.get("peopleId"))
        #
        #     # print("dic==>", dic)
        # print("costTime ==> ", time.time() - beginTime)
        #
        # print(ar)

        # ar = []
        # beginTime = time.time()
        # for x in range(1):
        #     peopleId = self.peopleNum + random.randint(12000, 91000)
        #     peopleId = str(peopleId)
        #     dic = self.collection.find_one({"peopleId": peopleId})
        #     ar.append(dic.get("peopleId"))
        #     # self.collection.find_one_and_update(filter={"peopleId": peopleId}, update={"name": "化工局"})
        #
        #     # self.collection.find_one_and_replace()
        #
        #     # print("dic==>", dic)
        # print("costTime ==> ", time.time() - beginTime)
        #
        # print(ar)

        peopleId = str(self.peopleNum+1)
        a = self.collection.find_one_and_update(filter={"peopleId": peopleId}, update={'$set': {"name": "化工局"}})
        print("a ==> ", a, type(a))

        a = self.collection.find_one({"peopleId": peopleId})
        print("a ==> ", a, type(a))

        # countNum = 0
        # result = self.collection.find().limit(5)
        # result.count()
        # for dic in result:
        #     countNum += 1
        #
        # print("countNum ==> ", countNum)







if __name__ == "__main__":
    t = TestRead()
    t.start()




