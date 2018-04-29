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

def consumer( ):
    r = ''
    while True:
        n = yield r
        if not n:
            print ("not n..")
            return
        print ('1[CONSUMER] Consuming %s...' % n)
        r= '200 OK'

def produce(result_list):
    f = result_list.send(None)
    print('2[PRODUCER] Consumer first return: %s' % f)
    n = 0
    while n < 2:
        n = n + 1
        print('2[PRODUCER] Producing %s...' % n)
        r = result_list.send(n)
        print('2[PRODUCER] Consumer return: %s' % r)

    result_list.close()



if __name__ == '__main__':
    print 'doing:'

    result_list = consumer()

    produce(result_list)

    print 'Done!'