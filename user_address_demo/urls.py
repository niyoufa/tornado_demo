    #coding=utf-8

import tornado.web
import handlers as UserAddressHandlers
import os

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", UserAddressHandlers.IndexHandler) ,
            (r"/api/address/list", UserAddressHandlers.UserAddressListHandler) ,
            (r"/api/address/default", UserAddressHandlers.UserAddressDefaultHandler) ,
            (r"/api/address", UserAddressHandlers.UserAddressHandler) ,
        ] 
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers,**settings)