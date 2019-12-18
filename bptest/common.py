#coding=utf-8
"""
Create On 2019-12-18

@author: Ron2
"""


import pymongo
from . import conf

def createDBConnection() -> (pymongo.mongo_client or None):
    """
    创建数据库连接
    :return:
    """

    uri = "mongodb://{username}:{password}@{host}:{port}/{db_name}?authMechanism=MONGODB-CR".format(username=conf.DB_USER,
                                                                                                    password=conf.DB_PORT,
                                                                                                    host=conf.DB_HOST,
                                                                                                    port=conf.DB_PORT,
                                                                                                    db_name=conf.DB_NAME)
    return pymongo.MongoClient(uri)






