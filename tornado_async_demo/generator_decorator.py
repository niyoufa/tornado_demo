# -*- coding: utf-8 -*-

import tornado.ioloop
from tornado.httpclient import AsyncHTTPClient
import functools , time

def task(func, url):
    return functools.partial(func, url)

def callback(gen):
    try:
        # gen.send(response)
        gen.send("sleep 2 sec")
    except StopIteration:
        pass

def sync(func):
    def wrapper():
        gen = func()
        f = gen.next()
        f(functools.partial(callback, gen))
    return wrapper

@sync
def fetch():
    # response = yield task(AsyncHTTPClient().fetch, 'https://www.baidu.com')
    response = yield task(tornado.ioloop.IOLoop.instance().add_timeout, time.time() + 2)
    print '1'
    print response
    print '2'

fetch()
print '3'

#启动事件循环，配合非阻塞的HTTP Server 工作
tornado.ioloop.IOLoop.instance().start()