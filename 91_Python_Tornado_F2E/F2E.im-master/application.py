#!/usr/bin/env python
# coding=utf-8
#
# Copyright 2012 F2E.im
# Do have a faith in what you're doing.
# Make your life a story worth telling.

# cat /etc/mime.types
# application/octet-stream    crx
'''
url:
http://tornado-zh-cn.readthedocs.io/zh_CN/latest/#
'''

import sys
reload(sys)
sys.setdefaultencoding("utf8")

import os.path
import re
import memcache
import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import handler.base
import handler.user
import handler.topic
import handler.page
import handler.notification
import handler.mytools



from tornado.options import define, options
from lib.loader import Loader
from lib.session import Session, SessionManager
from jinja2 import Environment, FileSystemLoader
from app.NewsSpider.NewsSpider import *

define("port", default = 3333, help = "run on the given port", type = int)
define("mysql_host", default = "localhost", help = "community database host")
define("mysql_database", default = "f2e", help = "community database name")
define("mysql_user", default = "root", help = "community database user")
define("mysql_password", default = "password", help = "community database password")

class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            blog_title = u"PyUp Community",
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies = False,
            cookie_secret = "cookie_secret_code",
            login_url = "/login",
            autoescape = None,
            jinja2 = Environment(loader = FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")), trim_blocks = True),
            reserved = ["user", "topic", "home", "setting", "forgot", "login", "logout", "register", "admin"],
            debug = True,
            ui_modules={"Entry": handler.mytools.EntryModule},
        )

        handlers = [
            (r"/", handler.topic.IndexHandler),
            (r"/t/(\d+)", handler.topic.ViewHandler),
            (r"/t/create", handler.topic.CreateHandler),
            (r"/t/create/(.*)", handler.topic.CreateHandler),
            (r"/t/edit/(.*)", handler.topic.EditHandler),
            (r"/reply/edit/(.*)", handler.topic.ReplyEditHandler),
            (r"/node/(.*)", handler.topic.NodeTopicsHandler),
            (r"/u/(.*)/topics", handler.topic.UserTopicsHandler),
            (r"/u/(.*)/replies", handler.topic.UserRepliesHandler),
            (r"/u/(.*)/favorites", handler.topic.UserFavoritesHandler),
            (r"/u/(.*)", handler.topic.ProfileHandler),
            (r"/vote", handler.topic.VoteHandler),
            (r"/favorite", handler.topic.FavoriteHandler),
            (r"/unfavorite", handler.topic.CancelFavoriteHandler),
            (r"/notifications", handler.notification.ListHandler),
            (r"/members", handler.topic.MembersHandler),
            (r"/setting", handler.user.SettingHandler),
            (r"/setting/avatar", handler.user.SettingAvatarHandler),
            (r"/setting/avatar/gravatar", handler.user.SettingAvatarFromGravatarHandler),
            (r"/setting/password", handler.user.SettingPasswordHandler),
            (r"/forgot", handler.user.ForgotPasswordHandler),
            (r"/login", handler.user.LoginHandler),
            (r"/logout", handler.user.LogoutHandler),
            (r"/register", handler.user.RegisterHandler),

            #start of tools

            (r"/mytools/mytools_main/(.*)", handler.mytools.MytoolsMainHandler),
            (r"/mytools/poem/poem_in", handler.mytools.PoemPageCreateHandler),
            (r"/mytools/poem/poem_out", handler.mytools.PoemPageShowHandler),
            (r"/b/createblog/(.*)", handler.mytools.CreateSimpleBlogHandler),
            (r"/b/viewbloglist", handler.mytools.ViewSimpleBlogListHandler),
            (r"/b/simplebloglistview/([^/]+)", handler.mytools.ViemSimpleBlogEntryHandler),
            #end of tools

            (r"/(favicon\.ico)", tornado.web.StaticFileHandler, dict(path = settings["static_path"])),
            (r"/(sitemap.*$)", tornado.web.StaticFileHandler, dict(path = settings["static_path"])),
            (r"/(bdsitemap\.txt)", tornado.web.StaticFileHandler, dict(path = settings["static_path"])),
            (r"/(.*)", handler.topic.ProfileHandler),
        ]

        tornado.web.Application.__init__(self, handlers, **settings)

        # Have one global connection to the blog DB across all handlers
        self.db = torndb.Connection(
            host = options.mysql_host, database = options.mysql_database,
            user = options.mysql_user, password = options.mysql_password
        )

        # create  one new global connection to the simpleblog DB across all handlers
        self.simpleblogdb = torndb.Connection(
            host=options.mysql_host, database= 'blog',
            user=options.mysql_user, password=options.mysql_password)

        # Have one global loader for loading models and handles
        self.loader = Loader(self.db)

        # Have one global model for db query
        self.user_model = self.loader.use("user.model")
        self.topic_model = self.loader.use("topic.model")
        self.reply_model = self.loader.use("reply.model")
        self.plane_model = self.loader.use("plane.model")
        self.node_model = self.loader.use("node.model")
        self.notification_model = self.loader.use("notification.model")
        self.vote_model = self.loader.use("vote.model")
        self.favorite_model = self.loader.use("favorite.model")

        # Have one global session controller
        self.session_manager = SessionManager(settings["cookie_secret"], ["127.0.0.1:11211"], 0)

        # Have one global memcache controller
        self.mc = memcache.Client(["127.0.0.1:11211"])


def main():
    app = Application()
    #tornado server
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    print '127.0.0.1:%s'%options.port
    http_server.listen(options.port)

    #timer

    tornado.ioloop.PeriodicCallback(f10s , 1*1000).start()  # start scheduler

    #while(1)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()

