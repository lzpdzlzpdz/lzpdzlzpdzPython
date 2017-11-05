#=coding:utf-8
"""
function:
    regex function
author:
    lzpdzlzpdz
"""
import re

def fun_findall(inputstr,findall_pattern):
    result = re.findall(findall_pattern, inputstr)
    
    return result
    
    
def fun_sub(inputstr,findall_pattern,rep_str):

    result = re.sub(findall_pattern, rep_str, inputstr)
    
    return result