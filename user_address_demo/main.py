#coding=utf-8

import pdb , os

import tornado.httpserver
import tornado.ioloop
import tornado.options

import settings

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(settings.Application())
    http_server.listen(options.port)
    print "\nserver start ! \n"
    tornado.ioloop.IOLoop.instance().start()