#coding=utf-8

import pymongo , pdb

def get_coll(db_name , coll_name) :
    client = pymongo.MongoClient()
    return client[db_name][coll_name]

def init_user_address_list() :
    coll = get_coll("user","UserAddress")
    user_address_info_list = [
        dict(
            user_id = 1 ,
            province = "江苏" ,
            city = "南京" ,
            area = "六合区" ,
            address = "金牛湖村" ,
            is_default_flag = True ,
            add_time = "2016-05-04 17:45:50" ,
        ) ,
        dict(
            user_id = 2 ,
            province = "江苏" ,
            city = "无锡" ,
            area = "XX区" ,
            address = "XXX村" ,
            is_default_flag = True ,
            add_time = "2016-05-04 17:45:50" ,
        ) ,
        dict(
            user_id = 3 ,
            province = "江苏" ,
            city = "镇江" ,
            area = "XX区" ,
            address = "XXX村" ,
            is_default_flag = True ,
            add_time = "2016-05-04 17:45:50" ,
        ) ,

    ]
    for address in user_address_info_list :
        if not coll.find({"user_id":address["user_id"]}).count() :
            coll.insert(address)

    user_address_list = []
    [ user_address_list.append(address) for address in coll.find() ]
    print user_address_list

if __name__ == "__main__" :
    init_user_address_list()