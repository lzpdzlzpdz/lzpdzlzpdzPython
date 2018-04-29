# =coding:utf-8
"""
function:
    python: how to use decorator, how to calculate the running time of a function
author:
    lzpdzlzpdz
description:
url:
    https://docs.python.org/2/tutorial/inputoutput.html#methods-of-file-objects
"""

import time

def deco(func):
    start_time = time.time()
    func()
    end_time = time.time()
    msecs = (end_time - start_time)*1000
    print 'running time:',msecs


def myfunc():
    print 'start myfunc'
    time.sleep(1)
    print 'end myfunc'


'''
装饰器函数：必须定义一个嵌套函数，并且返回里层函数名，不能带括号().
不然将会引发错误“TypeError: 'NoneType' object is not callable”
'''
def deco_new(func):
    def wrap():
        start_time = time.time()
        func()
        end_time = time.time()
        msecs = (end_time - start_time)*1000
        print 'running time:',msecs
    return wrap

'''
添加装饰器：其实”@deco”的本质就是”myfunc = deco(myfunc)”
装饰器理解：当我们调用一个被装饰器装饰的时，其实是先调用装饰器函数，再调用这个函数
装饰器作用：减少编写重复代码。
'''
@deco_new
def myfunc_new():
    print 'start myfunc_new'
    time.sleep(1)
    print 'end myfunc_new'

@deco_new
def myfunc_new_new():
    print 'start myfunc_new_new'
    time.sleep(1)
    print 'end myfunc_new_new'


if __name__ == '__main__':
    print 'staring find each file in dir:'

    '''
    如何计算一个函数的运行时间：
    '''
    #1. method1
    #deco(myfunc)

    '''
    但是，上面的做法method1有一个问题，就是所有的”myfunc”调用处都要改为”deco(myfunc)”。
    有没有，更简洁的方法？
    答：使用python装饰器
    '''
    #2. method2
    myfunc_new()

    myfunc_new_new()
    print 'Done!'

