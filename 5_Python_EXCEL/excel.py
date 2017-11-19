#=coding:utf-8
"""
function:
    modify a excel file which exist
author:
    lzpdzlzpdz
issue:
1. 可以在原有的excel文件上修改吗
答：可以，只要输出的excel的文件名称和输入的一样就行

2. 可以读取一个excel文件，再创建一个新的吗
答：可以只要输出的excel名称和输入的不一样就行。

3. 可以输入中文字符吗
答：可以，只要在中文字符串前面加u即可

4. xlrd行和列从0开始吗
答：是的。

5. python的u'字符串"（字符编码）：字符串前有u，什么含义？
答：表示字符串以unicode格式存储

6. 如何将中文str字符串，前面加个u呢？
答：在str对象后面添加newcell.decode("utf-8")，将str对象解码为unicode对象
"""
import xlrd
import xlwt
from xlutils.copy import copy



def modify_excel(old_excel_name,new_excel_name):
    print 'modify_old_excel = %s' % old_excel_name
    #open excel file which exist
    old_excel = xlrd.open_workbook(old_excel_name,formatting_info=True)
    
    #copy excel
    new_excel = copy(old_excel)
    
    #get the first sheet object
    ws = new_excel.get_sheet(0)
    
    #write data
    #ws.write(1, 1, '第二行，第二列')  
    ws.write(3,0,'jiangsu')
    ws.write(3,1,'nanjing')
    ws.write(3,2,'1')
    
    #write data
    ws.write(4,0,u'广东')
    ws.write(4,1,u'广州')
    ws.write(4,2,'1')
    

    
    #save excel
    new_excel.save(new_excel_name)
    print 'save new excel = %s' % new_excel_name

'''
插入一列，内容是前面制定两列的内容相加
'''
def modify_excel_add_new_col(old_excel_name,new_excel_name):
    print 'modify_excel_add_new_col = %s' % old_excel_name
    #open excel file which exist
    old_excel = xlrd.open_workbook(old_excel_name,formatting_info=True)
    
    #copy excel
    new_excel = copy(old_excel)
    
    #get the first sheet object
    new_ws = new_excel.get_sheet(0)
    
    #write data
    '''
            省份    省会    几线城市     省份 省会 几线城市
            福建    福州    2     福建 福州 2.0
            浙江    杭州    1     浙江 杭州 1.0
     jiangsu    nanjing    1     jiangsu nanjing 1
            广东    广州    1     广东 广州 1

    '''
    old_ws  = old_excel.sheet_by_index(0)
    print 'old_excel,rows = %s,cols = %s' % (old_ws.nrows,old_ws.ncols)
    for row in range(0,old_ws.nrows):
        newcell = ''
        for col in range (0,old_ws.ncols):
            newcell = newcell + ' ' + str(old_ws.cell(row,col).value)
            
        print 'newcell = %s' % newcell.decode("utf-8")
        new_ws.write(row,old_ws.ncols,newcell.decode("utf-8"))

    #save excel
    new_excel.save(new_excel_name)
    print 'save new excel = %s' % new_excel_name

if __name__ == "__main__":
    print 'Doing...'
    
    old_excel_name = "test.xls"
    new_excel_name = 'test.xls'
    #modify_excel(old_excel_name,new_excel_name)
    
    old_excel_name = "test.xls"
    new_excel_name = 'test_new.xls'
    modify_excel_add_new_col(old_excel_name,new_excel_name)
    print 'Done!'
    