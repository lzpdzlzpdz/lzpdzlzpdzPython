import time
import datetime
import  types

curenttime = datetime.datetime.now()
print curenttime
print type(curenttime)

curenttime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
print curenttime
print type(curenttime)

curenttime = datetime.datetime.now().strftime("%Y %m %d %H %M %S")
print curenttime
print type(curenttime)

curenttime = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
print curenttime
print type(curenttime)


curenttime = datetime.datetime.now().strftime("%H-%M-%S")
print curenttime
print type(curenttime)

#2.  news_wordcloud_20171211215119
#![wordcloud](./static/NewsImg/news_wordcloud_20171211215119.png)
curenttime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
savefig_path = '/static/NewsImg/news_wordcloud_%s.png' % curenttime
print savefig_path

savefig_path_link = '![wordcloud](%s)' % savefig_path
print savefig_path_link

