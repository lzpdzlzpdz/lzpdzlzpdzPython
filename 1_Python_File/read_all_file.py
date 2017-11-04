#=coding:utf-8
"""
function:
    read all files from dir
author:
    lzpdzlzpdz
description:
    print dir(os)
    print dir(os.path)
    'os.listdir'
    'os.path.join'
    'os.path.isfile'
    'os.path.splitext'
url:
    https://docs.python.org/2/tutorial/inputoutput.html#methods-of-file-objects
"""
import os

gfilelist = []
def get_files_from_dir(dir,type):
    for file in os.listdir(dir):
        filepath = os.path.join(dir,file)
        if os.path.isfile(filepath):
            #print os.path.splitext(filepath)[1]
            if os.path.splitext(filepath)[1] == type:
                gfilelist.append(filepath)
        else:
            get_files_from_dir(filepath,type)

if __name__ == '__main__':
    print 'staring find each file in dir:'
    dir = 'C:\Python27\Lib\sqlite3'
    type = '.py'
    print dir,type
    get_files_from_dir(dir,type)
    
    for file in gfilelist:
        print file
        
    print 'Done!'

