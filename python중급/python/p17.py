import sqlite3
from libs.db.dba import getConn

def select_a():
    conn = getConn()
    cur = conn.cursor()
    cur.execute('select * from test')
    print ('print all data')
    rs = cur.fetchall()
    for i in rs:
        print(i)

    conn.close()

def select_b(num, name):
    conn = getConn()
    cur = conn.cursor()
    cur.execute('select * from test where name = ?', (name,))
    print ('print all data')
    rs = cur.fetchmany(num)
    for i in rs:
        print(i)

    conn.close()


if __name__ == '__main__':
    #select_a() #fetchall
    select_b(1, 'Eric') #fetchmany