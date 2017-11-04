#=coding:utf-8
"""
function:read file
author:lzpdzlzpdz

description:
读文本文件
input = open('data', 'r')
读二进制文件
input = open('data', 'rb')
url:
https://docs.python.org/2/tutorial/inputoutput.html#methods-of-file-objects
"""


print 'Do it...'
f = open('result.txt', 'r')
try:
    for line in f:
        print line
finally:
    f.close()

print 'OK!'

