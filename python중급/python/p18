import sqlite3
from libs.db.dba import getConn

def update_a():
    conn = getConn()
    cur = conn.cursor()
    up_sql = 'update test set name = ? where name = ?'
    cur.execute(up_sql, ('Ethan', 'Eric'))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    update_a()
