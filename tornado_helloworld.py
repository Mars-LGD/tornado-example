#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/28 11:39
# @Author  : lichenxiao

import tornado.ioloop
import tornado.web
import json


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world")

class QueryNumberHandler(tornado.web.RequestHandler):

    def get(self,number):
        print self.request.arguments
        if not self.request.arguments.has_key('number'):
            res = {}
        else:
            res = {}
            res['number'] = self.request.arguments['number']
            if len(res['number']) == 1 and self.request.arguments['number'] == ['10086']:
                res['number'] = res['number'][0]
                res['tag'] = '中国移动客服'
        self.write(json.dumps(res))

def make_app():
    return tornado.web.Application([(r"/", MainHandler),
                                    (r"/query_number?(.*)",QueryNumberHandler)])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
