
# -*- coding: utf-8 -*-     
#mysqldb    
import time, MySQLdb    
   
print 'start'  
#连接    
conn=MySQLdb.connect(host="localhost",user="root",passwd="password",db="f2e",charset="utf8")  
cursor = conn.cursor()    

#查询    
n = cursor.execute("select * from favorite")    
print n
for row in cursor.fetchall():    
    print row
    for r in row:    
        print r  
