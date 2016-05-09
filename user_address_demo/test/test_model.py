#coding=utf-8

import sys , os
BASE_DIR = "E:\\develop\\tornado_demo\\user_address_demo"
sys.path.append(BASE_DIR)

import settings
import model.user_address as UserAddress

if __name__ == "__main__" :
    UserAddress.UserAddressModel.init_test_data()

