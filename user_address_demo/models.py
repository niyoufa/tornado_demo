#coding=utf-8

import pdb
import pymongo
import settings
import sys_types

class DB_CONST :
    DB_NAME = "db_name"
    COLL_NAME = "coll_name"
    COLL_TYPE = "coll_type"

class Collections :

    # MongoDB文档配置
    __COLLECTIONS = dict(
        UserAddress = dict(coll_name="UserAddress",db_name="user",coll_type=sys_types.CollectionType.UserAddress) ,
    )

    @classmethod
    def get_db_name(cls,table_name) :
        if cls.__COLLECTIONS.has_key(table_name):
            db_name = cls.__COLLECTIONS[table_name][DB_CONST.DB_NAME]
        else :
            db_name = ""
        return db_name

    @classmethod
    def get_coll_name(cls,table_name) :
        if cls.__COLLECTIONS.has_key(table_name):
            coll_name = cls.__COLLECTIONS[table_name][DB_CONST.COLL_NAME]
        else :
            coll_name = ""
        return coll_name

def get_client(host=settings.HOST,port=settings.PORT,**kwargs) :
    client = pymongo.MongoClient(host=host,port=port)
    return client

def get_address(client=None):
    if client :
        address = client.address
    else :
        client = get_client()
        address = client.address
    return address

def get_db_names(client=None):
    if client :
        db_names = client.database_names()
    else :
        client = get_client()
        db_names = client.database_names()
    return db_names

def get_database(db_name,**kwargs) :
    client = get_client()
    db = client.get_database(db_name)
    return db

def drop_db(db_name,client=None) :
    if client == None :
        client = get_client()
    client.drop_database(db_name)
    print db_name + " dropped!"

def get_coll_names(db_name) :
    db = get_database(db_name)
    coll_names = db.collection_names(include_system_collections=False)
    return coll_names

def get_coll(table_name) :
    db_name = Collections.get_db_name(table_name)
    coll_name = Collections.get_coll_name(table_name)
    if db_name and coll_name :
        client = get_client()
        coll = client[db_name][coll_name]
    else :
        coll = None
        print u"集合不存在!"
    return coll

def get_coll_db_name(table_name) :
    db_name = Collections.get_db_name(table_name)
    return db_name

def drop_coll(table_name) :
    db_name = Collections.get_db_name(table_name)
    if db_name == "" :
        print u"集合不存在!"
    else :
        try :
            db = get_database(db_name)
        except Exception ,e :
            print u"查询数据库失败" + str(e)
            return
        db.drop_collection(table_name)
        print table_name + " dropped!"



def init_user_address_list(table_name) :
    coll = get_coll(table_name)

    user_address_info_list = [
        dict(
            user_id = 1 ,
            province = u"江苏" ,
            city = u"南京" ,
            area = u"六合区" ,
            address = u"金牛湖村" ,
            is_default_flag = False ,
            add_time = u"2016-05-04 17:45:50" ,
        ) ,
        dict(
            user_id = 1 ,
            province = u"江苏" ,
            city = u"南京" ,
            area = u"六合区" ,
            address = u"金牛湖街道" ,
            is_default_flag = False ,
            add_time = u"2016-05-04 17:45:50" ,
        ) ,
        dict(
            user_id = 2 ,
            province = "江苏" ,
            city = u"无锡" ,
            area = u"XX区" ,
            address = u"XXX村" ,
            is_default_flag = False ,
            add_time = u"2016-05-04 17:45:50" ,
        ) ,
        dict(
            user_id = 3 ,
            province = u"江苏" ,
            city = u"镇江" ,
            area = u"XX区" ,
            address = u"XXX村" ,
            is_default_flag = False ,
            add_time = u"2016-05-04 17:45:50" ,
        ) ,

    ]

    count = 0
    for address in user_address_info_list :
        flag = False
        if not coll.find({"user_id":address["user_id"] , "address":address["address"]}).count() :
            coll.insert(address)
            print address
            flag = True
            count += 1
    if flag == False :
        print u"没有新增数据！"
    else :
        print u"新增 %s 条数据\n"%(count)

if __name__ == "__main__" :
    # UserAddress 用户地址表
    init_user_address_list("UserAddress")