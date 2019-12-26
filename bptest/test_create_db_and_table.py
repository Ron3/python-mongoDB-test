#coding=utf-8
"""
Create On 2019-12-26

@author: Ron2
"""

import pymongo
from bptest import common


class TestCreateDB(object):
    """
    测试创建db
    """
    def __init__(self):
        """
        """
        # 连接顺序 client --> db --> table
        self.client = common.createDBConnection_defaultDB()






    def start(self):
        """
        :return:
        """
        # print(dir(self.db))
        # cur = self.db.list_databases()
        # print(dir(cur), type(cur))
        # print("cur.batch_size ==> ", cur.batch_size)
        # cur.close()

        # print(self.db, type(self.db), dir(self.db))

        for dbName in self.client.list_databases():
            print("dbName 1 ==> ", dbName)

        for dbName in self.client.list_database_names():
            print("dbNam ==> ", dbName)


        userdb = self.client["userdb"]
        print (type(userdb))            # pymongo.database.Database

        table = userdb["bpuser"]
        print(type(table))              # pymongo.collection.Collection



        result = table.insert_one({"_id": "18680528076", "peopleId": "230803197906010037"})

        # result = table.find()
        # for dic in result:
        #     print(dic)


        # # 获取最大值 -1 表示最大, 1表示最小
        # result= table.find({"peopleId": {"$exists": True}}, sort=[("_id", -1)])[0]
        # print(type(result), result)
        #
        #
        # # 尝试获取索引
        #
        # # table.create_index([("peopleId", pymongo.ASCENDING)])
        # table.create_index([("peopleId", pymongo.ASCENDING)], unique=True)
        # index = table.index_information()
        # print("index ==> ", index, type(index))



if __name__=="__main__":
    t = TestCreateDB()
    t.start()




