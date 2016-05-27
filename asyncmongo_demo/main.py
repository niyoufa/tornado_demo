#coding=utf-8
import os, pdb
import asyncmongo
import tornado.web
import tornado.httpserver
import tornado.ioloop

class Handler(tornado.web.RequestHandler):
    @property
    def db(self):
        if not hasattr(self, '_db'):
            self._db = asyncmongo.Client(pool_id="",host='127.0.0.1', port=27017,dbname="user")
        return self._db

    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        pdb.set_trace()
        # result = yield tornado.gen.Task(self.db.UserAddress.find,{'user_id': 1})
        self.db.UserAddress.find(callback=self._on_response)

    def _on_response(self, response, error):
        if error:
            raise tornado.web.HTTPError(500)
        self.write(response)

class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            debug=True,
        )

        tornado.web.Application.__init__(self,
        [
            (r"/",Handler),
        ],
        **settings)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8889)
    print "\nserver start ! \n"
    tornado.ioloop.IOLoop.instance().start()