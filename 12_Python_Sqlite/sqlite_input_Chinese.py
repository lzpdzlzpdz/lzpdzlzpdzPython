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
    
    conn = sqlite3.connect('Chinagdp.db')
    conn.text_factory = str

    cur = conn.cursor()
    
    cur.execute('''create table if not exists Chinagdp 
    (area text,yeal2015 text)
    ''')
    
    cur.execute("insert into Chinagdp values ('北京','23014.59')")
    cur.execute("insert into Chinagdp values ('上海','16538.19')")

    
    rows = conn.execute("select * from Chinagdp where area=='北京'")
    for row in rows:
        #1.
        print row
        #2.
        print str(row).decode('string_escape')
        #print str(row).decode('utf-8')
        #3.
        for subrow in row:
            print subrow
    
    conn.commit()
    
    conn.close()
    
def load_database():
    print 'load_database'
    
    conn = sqlite3.connect('Chinagdp.db')
    
    cur = conn.cursor()
    
    rows = conn.execute("select * from Chinagdp")
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
    
    creat_database()
    
    #load_database()
    
    print 'Done!'
    
    
    
