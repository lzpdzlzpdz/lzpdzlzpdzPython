#=coding:utf-8
"""
function:
    read all files from dir by ini
author:
    lzpdzlzpdz
description:
    To get interpolation, you will need to use a ConfigParser:
    
    import ConfigParser
    iniFileUrl="conf.ini"
    conf=ConfigParser.ConfigParser() #生成conf对象
    conf.read(iniFileUrl)   #读取ini配置文件
    def readConfigFile():

    sections:配置文件中[]中的类型值
    options:每组中的键
    items:键-值的列表形式

    # 获取每组类型中的section类型值
    sections = conf.sections()  # 获取所有sections
    print "---conf.ini文件中的section内容有：", sections
        
    # 获取指定section的所有键值对
    print "---group_a的所有键-值为：", conf.items("group_a")
        
    # 获取指定section的所有键值option
    print "---group_a的所有键为：", conf.options("group_a")
    print "---group_b的所有键为：", conf.options("group_b")
        
    # 获取指定section，option读取具体值value
    print "---group_a组的a_key1值为：", conf.get("group_a", "a_key1")  
    print "---group_b组的b_key1值为(取整数类型)：", conf.getint("group_b", "b_key1") 

url:
    https://docs.python.org/2/tutorial/inputoutput.html#methods-of-file-objects
    https://docs.python.org/2/library/configparser.html?highlight=configparser
    https://docs.python.org/2/library/os.html
    https://docs.python.org/2/library/os.path.html
"""
 
import ConfigParser
import os, sys

def get_filepath_from_ini():
    
    cf = ConfigParser.ConfigParser()
    try:
        cf.read("read_all_file_from_ini.ini")
        
        filepath = cf.get("filepath", "filepath1")
        filetype = cf.get("filetype", "filetype1")
        print 'ini info:%s %s\n' %(filepath,filetype)
    except:
        filepath = ""
        filetype = ""
    return filepath,filetype

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
    filepath,filetype = get_filepath_from_ini()
    if not os.path.isdir(filepath):
        print 'input filepath err!'
        sys.exit()
    
    get_files_from_dir(filepath, filetype)
    
    for file in gfilelist:
        print file
        
    print 'Done!'