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

    uri = "mongodb://{username}:{password}@{host}:{port}/?authSource={db_name}&authMechanism=SCRAM-SHA-256".format(username=conf.DB_USER,
                                                                                                    password=conf.DB_PWD,
                                                                                                    host=conf.DB_HOST,
                                                                                                    port=conf.DB_PORT,
                                                                                                    db_name=conf.DB_NAME)
    return pymongo.MongoClient(uri)






