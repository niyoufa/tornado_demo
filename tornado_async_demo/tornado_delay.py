#coding=utf-8
import time
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler

import pdb , os

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define , options 
import tornado.websocket
import tornado.gen
import tornado.httpclient

define("port" , default=8000 , help="run on the given port" , type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MyHandler),
            (r"/get", GETHandler),
        ]
        settings = dict(
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class MyHandler(RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        self.write("sleeping .... ")
        self.flush()
        # Do nothing for 5 sec
        # time.sleep(5)
        # 使用 time.sleep 会阻塞其他的请求 ， 而使用 IOLoop.instance().add_timeout的异步方法
        # 不会阻塞其他请求，会将处理添加到时间循环
        yield tornado.gen.Task(IOLoop.instance().add_timeout, time.time() + 3)
        self.write("I'm awake!")
        self.finish()

class GETHandler(RequestHandler):
    def get(self):
        self.write("niyoufa")

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    print "server start !"
    tornado.ioloop.IOLoop.instance().start()