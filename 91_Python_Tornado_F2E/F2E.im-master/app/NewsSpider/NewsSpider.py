# -*- coding: utf-8 -*-
import os
import sys
import urllib2
import requests
import re
from lxml import etree
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

import sys
import markdown
import datetime
import torndb

reload(sys)
sys.setdefaultencoding('utf8')

class SpiderNewsClass(object):
    def __init__(self):
        self.spider_news_db = torndb.Connection(
            host="localhost", database= 'blog',
            user="root", password="password")

    def SaveSpiderNews(self, spider_news_content):
        node_slug = None
        template_variables = {}
        print 'SaveSpiderNews'
        id = None
        title = 'Spider News'
        text = spider_news_content
        #markdown to html
        html = markdown.markdown(text)
        curenttime = datetime.datetime.now()
        print 'curenttime',curenttime
        slug = str(curenttime)


        #save spider data to database:
        self.spider_news_db.execute(
            "INSERT INTO entries (author_id,title,slug,markdown,html,"
            "published) VALUES (%s,%s,%s,%s,%s,UTC_TIMESTAMP())",
            111, title, slug, text, html)
        #self.redirect("mytools/simpleblog/bloglistview.html" + slug)
        #self.redirect("/b/viewbloglist")


    def StringListSave(self, save_path, filename, slist):
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        path = save_path+"/"+filename+".txt"
        with open(path, "w+") as fp:
            for s in slist:
                fp.write("%s\t\t%s\n" % (s[0].encode("utf8"), s[1].encode("utf8")))

    def StringListSaveContent(self,save_path, filename, slist):
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        path = save_path+"/"+filename+".txt"
        with open(path, "w+") as fp:
            for s in slist:
                fp.write("%s\n" % (s[0].encode("utf8")))

        spider_news_content = ''
        for s in slist:
            spider_news_content = spider_news_content + s[0] + '\n'
        self.SaveSpiderNews(spider_news_content)


    def Page_Info(self,myPage):
        '''Regex'''
        mypage_Info = re.findall(r'<div class="titleBar" id=".*?"><h2>(.*?)</h2><div class="more"><a href="(.*?)">.*?</a></div></div>', myPage, re.S)
        return mypage_Info

    def New_Page_Info(self,new_page):
        '''Regex(slowly) or Xpath(fast)'''
        # new_page_Info = re.findall(r'<td class=".*?">.*?<a href="(.*?)\.html".*?>(.*?)</a></td>', new_page, re.S)
        # # new_page_Info = re.findall(r'<td class=".*?">.*?<a href="(.*?)">(.*?)</a></td>', new_page, re.S) # bugs
        # results = []
        # for url, item in new_page_Info:
        #     results.append((item, url+".html"))
        # return results
        dom = etree.HTML(new_page)
        new_items = dom.xpath('//tr/td/a/text()')
        new_urls = dom.xpath('//tr/td/a/@href')
        assert(len(new_items) == len(new_urls))
        return zip(new_items, new_urls)

    def Spider(self,url):
        i = 0
        print "downloading ", url
        myPage = requests.get(url).content.decode("gbk")
        # myPage = urllib2.urlopen(url).read().decode("gbk")
        myPageResults = self.Page_Info(myPage)
        save_path = u"网易新闻抓取"
        filename = str(i)+"_"+u"新闻排行榜"
        self.StringListSave(save_path, filename, myPageResults)
        i += 1
        for item, url in myPageResults:
            if u'科技' not in item:
                print item
                continue
            print "downloading ", url
            new_page = requests.get(url).content.decode("gbk")
            # new_page = urllib2.urlopen(url).read().decode("gbk")
            newPageResults = self.New_Page_Info(new_page)
            filename = str(i)+"_"+item
            self.StringListSaveContent(save_path, filename, newPageResults)
            i += 1

    def create_wordcloud(self):
        print 'create_wordcloud'
        text_from_file_with_apath = open(u'网易新闻抓取/1_科技.txt').read()
        print 'text_from_file_with_apath',text_from_file_with_apath

        wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)
        wl_space_split = " ".join(wordlist_after_jieba)

        #en
        #my_wordcloud = WordCloud().generate(wl_space_split)

        #ch
        wc1 = WordCloud(
            background_color="white",
            width=1000,
            height=860,
            font_path="C:\\Windows\\Fonts\\STFANGSO.ttf",  # 不加这一句显示口字形乱码
            margin=2)
        my_wordcloud = wc1.generate(wl_space_split)

        #save wordcloud to image, upload to my blog
        #plt.imshow(my_wordcloud)
        #plt.axis("off")
        #plt.show()

    def spidermain(self):
        print "start"
        start_url = "http://news.163.com/rank/"
        self.Spider(start_url)

        self.create_wordcloud()
        print "end"

# 每隔10s执行一次f10s
webspider_switch = True
def f10s():
    global webspider_switch
    print '10s ', datetime.datetime.now()

    SpiderObject = SpiderNewsClass()

    if (webspider_switch == True):
        webspider_switch = False
        SpiderObject.spidermain()