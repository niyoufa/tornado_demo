#coding=utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.web
import base64
import socket


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(('localhost', 8888))
        s.send('hello\n')
        data = s.recv(4096)
        self.write(data)
        self.finish()

if __name__ == "__main__":
    app = tornado.web.Application(
        handlers = [
            (r"/", MainHandler)
        ]
    )

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(10001)
    print "server sync start!"
    tornado.ioloop.IOLoop.instance().start()