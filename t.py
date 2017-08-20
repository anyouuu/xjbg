#!/usr/bin/env python2.7
# -*- encoding: utf-8 -*-

import tornado.web
import tornado.httpclient
import time

class MainHandler(tornado.web.RequestHandler):

    second = 0

    @tornado.web.asynchronous
    def get(self, second):
        print 'he want step %s second' % second

        self.second = second
        http = tornado.httpclient.AsyncHTTPClient()
        http.fetch("http://www.baidu.com",
                   callback=self.on_response)

    def sleep_reqs(self):
        time.sleep(int(self.second))
        print 'sleep : %s ' % self.second
        

    def on_response(self, response):
        if response.error:
            raise tornado.web.HTTPError(500)
        self.sleep_reqs()
        self.write("Fetche entries "
                   "from the FriendFeed API")
        self.finish()


def make_app():
    return tornado.web.Application([
        (r"/async/([0-9]+)", MainHandler),
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
