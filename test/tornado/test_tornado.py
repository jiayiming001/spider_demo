#!/usr/bin/env python  
# -*- coding: utf-8  -*-
#time:'2018/4/30 下午 12:52'
#author:'jiayiming'
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World!")

def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
    ])
if __name__ == "__main__" :
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()