#=coding:utf-8
"""
function:
    create a sqlite database
author:
    lzpdzlzpdz
"""
import sqlite3


def load_database():
    print 'load_database'
    
    conn = sqlite3.connect('ChinaGdp_csv.db')
    
    cur = conn.cursor()
    
    
    rows = conn.execute("select * from gpd5")
    for row in rows:
        print str(row).decode('unicode-escape')
    
    conn.commit()
    
    conn.close()

if __name__ == "__main__":
    print 'Doing...'
    
    
    load_database()
    
    print 'Done!'
    
    
    
