#coding=utf-8
import os , sys , pdb
import platform

sys.path.append(os.path.dirname(os.getcwd()))
import user_address_demo

BASE_DIR = os.path.dirname(user_address_demo.__file__)

SERVER_HOST = "localhost"
SERVER_PORT = 8000

MONGODB_HOST = "localhost"
MONGODB_PORT = 27017

HOST = "localhost"
PORT = 27018