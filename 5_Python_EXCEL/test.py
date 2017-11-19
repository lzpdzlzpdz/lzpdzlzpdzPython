# -*- coding:utf-8 -*-
'''
1. python默认的编码方式
因为默认情况下，Python采用的是ascii编码方式

1. 顶部的:# -*- coding: utf-8 -*-目前看来有三个作用。
如果代码中有中文注释，就需要此声明
比较高级的编辑器（比如我的emacs），会根据头部声明，将此作为代码文件的格式。
程序会通过头部声明，解码初始化 u”人生苦短”，这样的unicode对象，（所以头部声明和代码的存储格式要一致）
基本设置

2.主动设置defaultencoding。（默认的是ascii）
代码文件的保存格式要与文件头部的# coding:xxx一致
如果是中文，程序内部尽量使用unicode，而不用str


'''
# ： su是一个utf-8格式的字节串
s = "人生苦短"
print type(s)
print s


# ： s被解码为unicode对象，赋给u
u  = s.decode("utf-8")
print type(u)
print u


# ： u被编码为gbk格式的字节串，赋给sg
sg = u.encode("gbk")
print type(sg)

print sg
# 打印sg

