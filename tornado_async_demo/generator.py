# -*- coding: utf-8 -*-

import tornado.ioloop
from tornado.httpclient import AsyncHTTPClient

def callback(response):
    print response.body

def fetch():
    result = yield AsyncHTTPClient().fetch('https://www.baidu.com', callback)
    print result

gen = fetch()
gen.next()
try:
    gen.send('niyoufa')
except StopIteration:
    pass

tornado.ioloop.IOLoop.instance().start()
