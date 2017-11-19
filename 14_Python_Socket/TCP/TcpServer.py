#-*- coding: utf-8 -*-
'''
ss = socket()          #创建服务器套接字
    ss.bind()              #套接字与地址绑定
    ss.listen()             #监听连接
    inf_loop:             #服务器无限循环
        cs = ss.accepr()   #接受客户端连接
        comm_loop:      #通信循环
            cs.recv()/cs.send()   #对话（接收/发送）
        cs.close()        #关闭客户端套接字
    ss.close()            #关闭服务器套接字（可选）
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from socket import *      #将 socket 属性引入到命名空间
 
HOST = ''          #这是对 bind()方法的标识表示可以使用任何可用的地址
PORT = 21571      #端口号
BUFSIZ = 1024     #缓冲区大小，1kb
ADDR = (HOST,PORT)   #地址？？？？
 
tcpSerSocket = socket(AF_INET,SOCK_STREAM)    #创建 tcp 套接字
tcpSerSocket.bind(ADDR)           #将地址绑定到套接字上
tcpSerSocket.listen(5)            #设置并启动套接字监听
 
while True:        #无限循环，等待客户端连接
    print('waiting for connection...')   
    tcpCliSocket,addr = tcpSerSocket.accept()    #被动接受客户端连接     
    print('...connected from:',addr)
 
    while True:      #对话循环，等待客户端发送消息
        data = tcpCliSocket.recv(BUFSIZ)   #接收客户端消息
        if not data:     #如果消息是空白，跳出对话循环，关闭当前连接
          break
        tcpCliSocket.send(data)   #如果收到消息，将消息原封不动返回客户端
 
    tcpCliSocket.close()
tcpSerSocket.close()