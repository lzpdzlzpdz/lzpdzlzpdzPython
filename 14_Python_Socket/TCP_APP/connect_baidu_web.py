#coding:utf-8

'''
客户端编程,五部曲：
1.创建 socket
2.连接到远程服务器
3.发送数据
4.接收数据
5.关闭 socket

转载至：
https://www.cnblogs.com/hazir/p/python_socket_programming.html
Python socket – network programming tutorial
'''
import socket


#handling errors in python socket programs
 
import socket   #for sockets
import sys  #for exit

'''
1.创建 socket
使用Python中的socket模块的socket函数，创建一个socket
'''
try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();
 
print '1.Socket Created'

'''
2.连接服务器
socket 使用 (IP地址，协议，端口号) 来标识一个进程，
那么我们要想和服务器进行通信，就需要知道它的 IP地址以及端口号。
'''
#Python 提供了一个函数 socket.gethostbyname来获得远程主机的 IP 地址：
host = 'www.baidu.com'
port = 80
 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
     
print 'Ip address of ' + host + ' is ' + remote_ip


#现在我们知道了服务器的 IP 地址，就可以使用连接函数 connect 连接到该 IP 的某个特定的端口上了，
#下面例子连接到 80 端口上（是 HTTP 服务的默认端口）：

#Connect to remote server
s.connect((remote_ip , port))
 
print '2. Socket Connected to ' + host + ' on ip ' + remote_ip

'''
3.发送数据
上面说明连接到 www.baidu.com 已经成功了，接下面我们可以向服务器发送一些数据，
例如发送字符串GET / HTTP/1.1\r\n\r\n，这是一个 HTTP 请求网页内容的命令。
'''
#Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"
 
try :
    #Set the whole string
    s.sendall(message)
except socket.error:
    #Send failed
    print 'Send failed'
    sys.exit()
 
print '3.Message send successfully'

'''
4.接收数据
函数 recv 可以用来接收 socket 的数据：
'''
reply = s.recv(4096)
print '4.rev data:\n%s' % reply


'''
5.关闭 socket
当我们不想再次请求服务器数据时，可以将该 socket 关闭，结束这次通信：
'''
s.close()


