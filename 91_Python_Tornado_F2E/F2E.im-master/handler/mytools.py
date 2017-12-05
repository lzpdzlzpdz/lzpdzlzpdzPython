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
     def post(self, template_variables = {}):
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


class ComposeHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        print 'ComposeHandler,get:'
        id = self.get_argument("id", None)
        entry = None
        if id:
            entry = self.db.get("SELECT * FROM entries WHERE id = %s", int(id))
        self.render("mytools/simpleblog/compose.html", entry=entry)

    @tornado.web.authenticated
    def post(self):
        print 'ComposeHandler,post:'
        id = self.get_argument("id", None)
        title = self.get_argument("title")
        text = self.get_argument("markdown")
        html = markdown.markdown(text)
        if id:
            entry = self.db.get("SELECT * FROM entries WHERE id = %s", int(id))
            if not entry: raise tornado.web.HTTPError(404)
            slug = entry.slug
            self.db.execute(
                "UPDATE entries SET title = %s, markdown = %s, html = %s "
                "WHERE id = %s", title, text, html, int(id))
        else:
            slug = unicodedata.normalize("NFKD", title).encode(
                "ascii", "ignore")
            slug = re.sub(r"[^\w]+", " ", slug)
            slug = "-".join(slug.lower().strip().split())
            if not slug: slug = "entry"
            while True:
                e = self.db.get("SELECT * FROM entries WHERE slug = %s", slug)
                if not e: break
                slug += "-2"
            self.db.execute(
                "INSERT INTO entries (author_id,title,slug,markdown,html,"
                "published) VALUES (%s,%s,%s,%s,%s,UTC_TIMESTAMP())",
                self.current_user.id, title, slug, text, html)
        self.redirect("/entry/" + slug)


#每隔10s执行一次f10s
webspider_switch = True
def f10s():
    global webspider_switch
    print '10s ', datetime.datetime.now()

    if(webspider_switch == True):
        webspider_switch = False
        webspider.webspider_by_tornado()