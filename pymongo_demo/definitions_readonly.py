import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import pymongo , pdb

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/(\w+)", WordHandler)]
        client = pymongo.MongoClient()
        db = client.test_database
        self.db = db
        tornado.web.Application.__init__(self, handlers, debug=True)

class WordHandler(tornado.web.RequestHandler):
    def get(self, word):
        coll = self.application.db.example
        word_doc = coll.find_one({"word": word})
        if word_doc:
            del word_doc["_id"]
            self.write(word_doc)
        else:
            self.set_status(404)
            self.write({"error": "word not found"})

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    print "\nserver start ! \n"
    tornado.ioloop.IOLoop.instance().start()