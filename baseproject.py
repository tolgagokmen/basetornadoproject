#!/usr/bin/env python
# coding=utf-8

import locale
import os.path
import sys

import tornado
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from motor import MotorClient
from tornado.options import define, options

import urls
from modules.book_module import BookModule

# locale.setlocale(locale.LC_ALL, 'tr_TR')
locale.setlocale(locale.LC_ALL)

reload(sys)
sys.setdefaultencoding("utf-8")

define("port", default=8888, help="run on the given port", type=int)
define("default_connection_string",
       default="mongodb://localhost/example",
       help="Mongo Connection String")
define("debug", default=True, help="Debug tornado")
define("autoreload", default=True, help="Autoreload tornado")


def get_settings():
    _settings = dict(
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        ui_modules={"Book": BookModule},
        xsrf_cookies=False,
        cookie_secret="69kfTuTqT/eVky3EAOz6m9WN7yXnFUqMn+qENfzYTDI=",
        login_url="/auth/login",
        debug=options.autoreload,
        autoreload=options.autoreload
        # skipauth=options.skipauth

    )

    return _settings


def make_app(routes, settings):
    app = tornado.web.Application(routes, **settings)
    uri = options.default_connection_string

    client = MotorClient(uri)
    app.db = client.get_default_database()

    return app


def main():
    # tornado.options.parse_config_file('%s.conf' % options.config)
    tornado.options.parse_command_line()

    app = make_app(urls.get_routes(), get_settings())
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)

    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
