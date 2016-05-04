#coding=utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import pymongo , pdb , os

from models import get_coll

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler) ,
            (r"/user_address_list", UserAddressListHandler) ,

        ] 
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers,**settings)

class IndexHandler(tornado.web.RequestHandler) :
    def get(self) :
        self.render(
            "index.html",
            page_title = "user address",
            header_text = "用户地址列表",
        )

class UserAddressListHandler(tornado.web.RequestHandler):
    def get(self):
        pdb.set_trace()
        result = {}
        result["success"] = 1
        result["return_code"] = "success"
        result["data"] = {}

        coll = get_coll("user","UserAddress")
        
        user_address_list = []
        temp_user_address_list = []
        [ temp_user_address_list.append(address) for address in coll.find() ]
        for address in temp_user_address_list :
            del address["user_id"]

        [ user_address_list.append(address) for address in temp_user_address_list ]
        result["data"]["user_address_list"] = user_address_list

        self.write({"result": result})

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    print "\nserver start ! \n"
    tornado.ioloop.IOLoop.instance().start()