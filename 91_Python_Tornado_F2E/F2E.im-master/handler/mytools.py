#!/usr/bin/env python
# coding=utf-8
#
# Copyright 2012 F2E.im
# Do have a faith in what you're doing.
# Make your life a story worth telling.

import uuid
import hashlib
from PIL import Image
import StringIO
import time
import json
import re
import urllib2
import tornado.web
import lib.jsonp

from base import *
from lib.variables import *
import datetime
import  webspider
import  markdown
from lib.variables import gen_random





class EntryModule(tornado.web.UIModule):
    def render(self, entry):
        return self.render_string("mytools/simpleblog/markdownview.html", entry=entry)

class MytoolsMainHandler(BaseHandler):
    def get(self, topic_id, template_variables = {}):
        print 'MytoolsMainHandler\n'

        user_info = self.current_user
        page = int(self.get_argument("p", "1"))
        user_info = self.get_current_user()


        template_variables["user_info"] = user_info
        if (user_info):
            template_variables["user_info"]["counter"] = {
                "topics": self.topic_model.get_user_all_topics_count(user_info["uid"]),
                "replies": self.reply_model.get_user_all_replies_count(user_info["uid"]),
                "favorites": self.favorite_model.get_user_favorite_count(user_info["uid"]),
            }
        
        template_variables["gen_random"] = gen_random

        print template_variables
        print 'hello'
        self.render('mytools/mytools_main.html', **template_variables)


class PoemPageShowHandler(BaseHandler):
     def post(self,  template_variables = {}):
         print 'PoemPageHandler\n'

         user_info = self.current_user
         page = int(self.get_argument("p", "1"))
         user_info = self.get_current_user()
         template_variables["user_info"] = user_info
         if(user_info):
             template_variables["user_info"]["counter"] = {
                 "topics": self.topic_model.get_user_all_topics_count(user_info["uid"]),
                 "replies": self.reply_model.get_user_all_replies_count(user_info["uid"]),
                 "favorites": self.favorite_model.get_user_favorite_count(user_info["uid"]),
             }

         template_variables["gen_random"] = gen_random

         noun1 = self.get_argument('noun1')
         noun2 = self.get_argument('noun2')
         verb = self.get_argument('verb')
         noun3 = self.get_argument('noun3')
         self.render('mytools/poem/poem_out.html', roads=noun1, wood=noun2, made=verb,
         difference=noun3, **template_variables)


class PoemPageCreateHandler(BaseHandler):
    def get(self, template_variables = {}):
        print 'PoemPageCreateHandler\n'

        user_info = self.current_user
        page = int(self.get_argument("p", "1"))
        user_info = self.get_current_user()
        template_variables["user_info"] = user_info
        if (user_info):
            template_variables["user_info"]["counter"] = {
                "topics": self.topic_model.get_user_all_topics_count(user_info["uid"]),
                "replies": self.reply_model.get_user_all_replies_count(user_info["uid"]),
                "favorites": self.favorite_model.get_user_favorite_count(user_info["uid"]),
            }

        template_variables["gen_random"] = gen_random

        self.render('/mytools/poem/poem_in.html', **template_variables)


class CreateSimpleBlogHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, node_slug=None, template_variables={}):
        print 'CreateSimpleBlogHandler get'
        user_info = self.current_user
        template_variables["user_info"] = user_info
        template_variables["user_info"]["counter"] = {
            "topics": self.topic_model.get_user_all_topics_count(user_info["uid"]),
            "replies": self.reply_model.get_user_all_replies_count(user_info["uid"]),
            "favorites": self.favorite_model.get_user_favorite_count(user_info["uid"]),
        }

        template_variables["notifications_count"] = self.notification_model.get_user_unread_notification_count(
            user_info["uid"])
        template_variables["gen_random"] = gen_random
        template_variables["node_slug"] = node_slug
        template_variables["active_page"] = "topic"
        self.render("mytools/simpleblog/createblog.html", **template_variables)



    @tornado.web.authenticated
    def post(self, node_slug=None, template_variables={}):
        print 'CreateHandler post'
        id = self.get_argument("id", None)
        title = self.get_argument("title")
        text = self.get_argument("markdown")
        #markdown to html
        html = markdown.markdown(text)
        curenttime = datetime.datetime.now()
        print 'curenttime',curenttime
        slug = str(curenttime)

        self.simpleblogdb.execute(
            "INSERT INTO entries (author_id,title,slug,markdown,html,"
            "published) VALUES (%s,%s,%s,%s,%s,UTC_TIMESTAMP())",
            self.current_user["uid"], title, slug, text, html)
        #self.redirect("mytools/simpleblog/bloglistview.html" + slug)
        self.redirect("/b/viewbloglist")
class ViewSimpleBlogListHandler(BaseHandler):
    def get(self, node_slug=None, template_variables={}):
        entries = self.simpleblogdb.query("SELECT * FROM entries ORDER BY published "
                                "DESC")

        template_variables["gen_random"] = gen_random
        self.render("mytools/simpleblog/bloglistview.html", entries=entries, **template_variables)


class ViemSimpleBlogEntryHandler(BaseHandler):
    def get(self, node_slug=None, template_variables={}):
        print 'ViemSimpleBlogEntryHandler11111'
        entry = self.simpleblogdb.get("SELECT * FROM entries WHERE slug = %s", node_slug)
        if not entry: raise tornado.web.HTTPError(404)

        template_variables["gen_random"] = gen_random

        print 'entry'
        print  entry
        self.render("mytools/simpleblog/blogentryview.html", entry=entry, **template_variables)


