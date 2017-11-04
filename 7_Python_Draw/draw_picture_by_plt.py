#=coding:utf-8
"""
function:
    draw picture from data
author:
    lzpdzlzpdz
issue:
(1)如果matplotlib图例出现中文乱码，则如下处理
    sys.setdefaultencoding('utf-8')
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
         显示的内容前面加u,即表示为u'内容'
"""
import pandas as pd
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

def draw_line_by_list():
    data_every_month = pd.read_csv(r'./datas/data_every_month.txt')
    y = data_every_month['nums'].T.values
    x = range(0,len(y))
    
    plt.figure(figsize=(10, 6))
    plt.plot(x,y,'')  
    plt.xticks((0,20,40,60,80,100,120),('200504','200912','201108','201306','201702','201810',''))
    plt.xlabel(u'年月')
    plt.ylabel(u'XX事件数')
    plt.title(u'每月XX事件数')
    plt.show()

def draw_two_line_by_csv():
    data_every_month = pd.read_csv(r'./datas/data_every_month.txt')
    y = data_every_month['nums'].T.values
    y1=y[79:91]
    y2=y[91:102]
    x1=range(0,len(y1))
    x2=range(0,len(y2))
    
    plt.figure(figsize=(10, 6))
    plt.plot(x1,y1,'',label=u"2017年")
    plt.plot(x2,y2,'',label=u"2018年")
    plt.title(u'2017-2018年月XX事件数')
    plt.legend(loc='upper right')
    plt.xticks((0,2,4,6,8,10),(u'1月',u'3月',u'5月',u'7月',u'9月',u'11月'))
    plt.xlabel(u'月份')
    plt.ylabel(u'XX事件数')
    plt.grid(x1)
    plt.show()

def draw_bar_by_list():
    data_week2017 = [0,1,2,3,4]
    data_week2018 = [1000,3000,6000,4000,2000]
    
    plt.figure(figsize=(10, 6))
    xweek=range(0,len(data_week2017))
    xweek1=[i+0.3 for i in xweek]
    plt.bar(xweek,data_week2017,color='g',width = .3,alpha=0.6,label=u'2017年')
    plt.bar(xweek1,data_week2018,color='r',width = .3,alpha=0.4,label=u'2018年')
    
    plt.xlabel(u'周')
    plt.ylabel(u'XX事件数量')
    plt.title(u'XX事件数周分布')
    plt.legend(loc='upper right')
    plt.xticks(range(0,7),[u'星期日',u'星期一',u'星期二',u'星期三',u'星期四',u'星期五',u'星期六'])
    plt.show()


def draw_bar_by_csv():
    data_week2017 = pd.read_csv(r'./datas/data_week2017.txt')['nums'].T.values
    data_week2018 = pd.read_csv(r'./datas/data_week2018.txt')['nums'].T.values
    
    plt.figure(figsize=(10, 6))
    xweek=range(0,len(data_week2017))
    xweek1=[i+0.3 for i in xweek]
    plt.bar(xweek,data_week2017,color='g',width = .3,alpha=0.6,label=u'2017年')
    plt.bar(xweek1,data_week2018,color='r',width = .3,alpha=0.4,label=u'2018年')
    
    plt.xlabel(u'周')
    plt.ylabel(u'XX事件数量')
    plt.title(u'XX事件数周分布')
    plt.legend(loc='upper right')
    plt.xticks(range(0,7),[u'星期日',u'星期一',u'星期二',u'星期三',u'星期四',u'星期五',u'星期六'])
    plt.show()

if __name__ == '__main__':
    print 'Doing...'
    draw_bar_by_list()
    
    draw_bar_by_csv()
    
    draw_line_by_list()
    
    draw_two_line_by_csv()
    
        
    print 'Done!'


