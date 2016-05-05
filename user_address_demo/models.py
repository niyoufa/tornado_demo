#coding=utf-8

import pymongo , pdb

class Collections :

    __COLLECTIONS = dict(
        UserAddress = dict(coll_name="UserAddress",db_name="user") ,
    )

    @classmethod
    def get_db_name(cls,table_name) :
        return cls.__COLLECTIONS[table_name]["db_name"]

    @classmethod
    def get_coll_name(cls,table_name) :
        return cls.__COLLECTIONS[table_name]["coll_name"]

def get_coll(table_name) :
    db_name = Collections.get_db_name(table_name)
    coll_name = Collections.get_coll_name(table_name)
    client = pymongo.MongoClient()
    coll = client[db_name][coll_name]
    return coll

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