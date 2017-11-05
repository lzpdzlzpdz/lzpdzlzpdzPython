#=coding:utf-8
"""
function:
    qt tool:regex
author:
    lzpdzlzpdz
issue:
1. 显示中文
from PyQt4 import QtGui, QtCore
s = QtCore.QString(u'中文').toLocal8Bit()
u = unicode(s,'gbk','ignore')
print u
输出结果是：
> 中文

url:
https://docs.python.org/2/library/re.html
"""

from __future__ import division
import sys
from PyQt4 import QtCore, QtGui, uic

import regex_fun

g_regex_description = u"""模式    描述
\w    匹配字母数字及下划线
\s    匹配任意空白字符，等价于 [\\t\\n\\r\\f].
\d    匹配任意数字，等价于 [0-9].
^    匹配字符串的开头
$    匹配字符串的末尾。
.    匹配任意字符，除了换行符。
[...]    若[abc]，则匹配 'a'，'b'或'c'
[^...]   若[^abc]，则匹配除了a,b,c之外的字符。
(xxx) 匹配括号内的表达式，也表示一个组
*    匹配0个或多个的表达式。
+    匹配1个或多个的表达式。
?    匹配0个或1个由前面正则表达式定义的片段
a|b  匹配a或b
"""


qtCreatorFile = "regex_template.ui" # Input your Qt template.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        self.fun_qt_description()
        self.pushButton_findall.clicked.connect(self.fun_qt_findall)
        self.pushButton_sub.clicked.connect(self.fun_qt_sub)
    def fun_qt_description(self):
        regex_description_s = QtCore.QString(g_regex_description).toLocal8Bit()
        regex_description_s_u = unicode(regex_description_s,'gbk','ignore')
        self.regexdescription.setText(regex_description_s_u)
    
    def fun_qt_findall(self):
        inputstr = str(self.inputstr.toPlainText())
        findall_str = str(self.findallstr.toPlainText())
        
        findall_result_string = regex_fun.fun_findall(inputstr,findall_str)
        
        self.findalloutputstr.setText("我的"+str(findall_result_string))

    def fun_qt_sub(self):
        inputstr = str(self.inputstr.toPlainText())
        findall_pattern = str(self.findallstr.toPlainText())
        rep_str = str(self.substr.toPlainText())
        
        sub_result_string = regex_fun.fun_sub(inputstr,findall_pattern,rep_str)
        
        self.suboutputstr.setText(str(sub_result_string))
        
     
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    
    
    
    