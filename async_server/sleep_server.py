#coding=utf-8

from tornado.tcpserver import TCPServer
from tornado import ioloop
from tornado import gen
from tornado.concurrent import Future


def sleep(duration):
    f = Future()
    ioloop.IOLoop.current().call_later(duration, lambda: f.set_result(None))
    return f


def handle_excep(future):
    if future.exception() is not None:
        print future.exc_info()


class EchoServer(TCPServer):
    def handle_stream(self, stream, address):
        f = self._handle_stream(stream, address)
        f.add_done_callback(handle_excep)

    @gen.coroutine
    def _handle_stream(self, stream, address):
        data = yield stream.read_until('\n')
        yield sleep(2)
        yield stream.write(data)
        stream.close()


server = EchoServer()
server.listen(8888)
print "server start!"
ioloop.IOLoop.instance().start()