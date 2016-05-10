#coding=utf-8
import os , sys , pdb
import platform

if platform.system() == "Linux":
    sys.path.append("/home/nyf/develop/dhui/tornado_demo")
else:
    sys.path.append("E:\\develop\\tornado_demo")
import user_address_demo

BASE_DIR = os.path.dirname(os.path.join(user_address_demo.__file__,"user_address_demo.settings"))

SERVER_HOST = "localhost"
SERVER_PORT = 8000

MONGODB_HOST = "localhost"
MONGODB_PORT = 27017

HOST = "localhost"
PORT = 27018