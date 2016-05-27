# -*- coding: utf-8 -*-

import tornado.ioloop
from tornado.httpclient import AsyncHTTPClient
import functools

def fetch():
    response = yield functools.partial(AsyncHTTPClient().fetch, 'http://sohu.com')
    print response

def callback(gen,response):
    try:
        gen.send(response)
    except StopIteration:
        pass

gen = fetch()
f = gen.next()
f(functools.partial(callback, gen))
print "1"

tornado.ioloop.IOLoop.instance().start()

#在 fetch() 中，代码看起来就像是同步结构一样