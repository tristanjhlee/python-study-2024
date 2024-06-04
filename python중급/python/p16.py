#insert in DB (2ways)

import sqlite3
from libs.db.dba import getConn

def insert_b():
    conn = getConn()
    cur = conn.cursor()
    cur.execute('''
    insert into test values ('Eric', 80, 90, 100)
    ''')
    conn.commit()
    conn.close()

def insert_c():
    conn = getConn()
    cur = conn.cursor()
    ins_sql = 'insert into test values (?, ?, ?, ?)'
    cur.execute(ins_sql, ('John', 77, 88, 99))
    conn.commit()
    conn.close()

def insert_d():
    conn = getConn()
    cur = conn.cursor()
    ins_sql = 'insert into test values (?, ?, ?, ?)'
    li = [('Joe', 71, 82, 93), ('Jack', 74, 85, 96), ('Paul', 73, 82, 91)]
    cur.executemany(ins_sql, li)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    #insert_b()
    #insert_c() #쿼리문을 먼저 만들어놓는 방법
    insert_d() #쿼리문을 먼저 만들어놓고 여러 data를 넣는 방법 (executemany)
