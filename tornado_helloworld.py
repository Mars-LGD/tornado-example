#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/28 11:39
# @Author  : lichenxiao

import tornado.ioloop
from tornado.web import RequestHandler
import json
from config import db_conf
from lib.db import MySQLDBUtils


class MainHandler(RequestHandler):
    def get(self):
        self.write("hello world")


class QueryNumberHandler(RequestHandler):
    def get(self):
        number = self.get_argument('number', None)
        res = {}
        if number:
            data = MySQLDBUtils(db_conf).query("select * from tbl_number_box86 where number=%s", [number],
                                               ret_type='one')
            res['number'] = number
            res['tag'] = data['tag']
        self.write(json.dumps(res))


def make_app():
    return tornado.web.Application([(r"/", MainHandler),
                                    (r"/query_number", QueryNumberHandler)])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
