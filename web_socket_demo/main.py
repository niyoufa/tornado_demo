#coding=utf-8
# hello.py
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
            (r"/", IndexHandler),
            (r"/send", WebSocketHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class IndexHandler(tornado.web.RequestHandler) :
    def get(self) :
        self.render("index.html")

class WebSocketHandler(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    def open(self):
        self.write_message("build a connect")

    def on_close(self):
        self.write_message("close connect")

    def on_message(self,message):
        self.write_message("receive message :%s"%message)
        self.write_to_client()

    @tornado.web.asynchronous
    @tornado.gen.engine
    def write_to_client(self):    
        client = tornado.httpclient.AsyncHTTPClient()
        result = yield tornado.gen.Task(client.fetch,"https://www.baidu.com")
        self.write_message("write to client : %s"%result)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    print "server start !"
    tornado.ioloop.IOLoop.instance().start()

