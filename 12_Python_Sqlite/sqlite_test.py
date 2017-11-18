#=coding:utf-8
"""
function:
    create a sqlite database
author:
    lzpdzlzpdz
"""

import sqlite3

def creat_database():
    print 'creat_database'
    
    conn = sqlite3.connect('test.db')
    
    cur = conn.cursor()
    
    cur.execute('''create table if not exists stocks 
    (data text, trans text, symbol text, qty real,price real)
    ''')
    
    cur.execute("insert into stocks values ('2016-01-05','BUY','RHAT',100,35.14)")
    cur.execute("insert into stocks values ('2016-01-05','BUY','BBBB',200,35.14)")
    cur.execute("insert into stocks values ('2017-01-05','BUY','CCCC',300,50)")
    
    rows = conn.execute("select * from stocks")
    for row in rows:
        print row
    
    conn.commit()
    
    conn.close()
    
def load_database():
    print 'load_database'
    
    conn = sqlite3.connect('test.db')
    
    cur = conn.cursor()
    
    rows = conn.execute("select * from stocks")
    for row in rows:
        print row
        
    print "select * from stocks where symbol == 'BBBB' "
    rows = conn.execute("select * from stocks where symbol == 'BBBB' ")
    for row in rows:
        print row
    
    conn.commit()
    
    conn.close()

if __name__ == "__main__":
    print 'Doing...'
    
    #creat_database()
    
    load_database()
    
    print 'Done!'
    
    
    
