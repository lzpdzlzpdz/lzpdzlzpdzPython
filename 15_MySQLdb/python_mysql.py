#coding=utf-8
import MySQLdb

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='',
        db ='test',
        )
cur = conn.cursor()

#创建数据表
cur.execute("create table if not exists student(id int ,name varchar(20),class varchar(30),age varchar(10))")

#获得表中有多少条数据
aa=cur.execute("select * from student")
print aa

#打印表中的多少数据
info = cur.fetchmany(aa)
for ii in info:
    print ii

cur.close()
conn.commit()
conn.close()

