# =coding:utf-8
"""
function:
    how to use yield
author:
    lzpdzlzpdz
description:
yield 的作用就是把一个函数变成一个generator，带有 yield 的函数不再是一个普通函数，
Python 解释器会将其视为一个生成器，如调用fab函数， 不会执行该函数，而是返回一个iterable迭代对象！
"""

def fun_eat_fish():
    print 'fun_eat_fish'
    for i in range(5):
        print 'start eat fish'
        print i+1
        print 'finish eat fish'

def fun_yield_eat_meat():
    print 'fun_yield_eat_meat'
    for i in range(5):
        print 'start eat meat'
        yield i+1
        print 'finish eat yield_meat'

if __name__ == '__main__':
    print 'doing:'

    print 'test1:'
    result =  fun_eat_fish()
    print result

    print 'test2:执行一个yield函数，想要执行的不是这个函数，而是返回的那个迭代器'
    result = fun_yield_eat_meat()
    print result
    print 'print the iterator:'
    print list(result)

    print 'Done!'