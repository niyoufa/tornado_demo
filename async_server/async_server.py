#coding=utf-8

import tornado.httpserver
import tornado.web
import socket
from tornado import ioloop
from tornado import gen
from tornado.concurrent import Future


class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        data = yield self.get_data()
        self.write(data)
        self.finish()

    def get_data(self):
        future = Future()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 8888))
        s.send('hello\n')

        def handle_data(sock, event):
            io_loop = ioloop.IOLoop.current()
            io_loop.remove_handler(sock)
            data = sock.recv(1024)
            future.set_result(data)

        io_loop = ioloop.IOLoop.current()
        io_loop.add_handler(s, handle_data, io_loop.READ)

        return future


if __name__ == "__main__":
    app = tornado.web.Application(
        handlers=[
            (r"/", MainHandler)
        ]
    )

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(10002)
    print "server async start!"
    tornado.ioloop.IOLoop.instance().start()