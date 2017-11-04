#=coding:utf-8
"""
function:write file
author:lzpdzlzpdz

description:
写文本文件
output = open('data', 'w')
写二进制文件
output = open('data', 'wb')
追加写文件
output = open('data', 'w+')
url:
https://docs.python.org/2/tutorial/inputoutput.html#methods-of-file-objects
"""


print 'Do it...'
f = open('result.txt', 'w+')
try:
    f.write('hello\n')
    f.write('welcome\n')
    f.write('to\n')
    f.write('python world')
finally:
    f.close()

print 'OK!'

