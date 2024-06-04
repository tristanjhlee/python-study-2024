#delete eng '<= 85'

import sqlite3
from libs.db.dba import getConn

def delete_a():
    conn = getConn()
    cur = conn.cursor()
    cur.execute('delete from test where eng  <= ?', (85,))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    delete_a()
