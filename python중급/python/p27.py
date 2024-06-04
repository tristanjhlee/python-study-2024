from libs.db.mdba import getConn

def select_a():
    conn = getConn()
    cur = conn.cursor()
    cur.execute('select * from sj')
    rs = cur.fetchall()
    for i in rs:
        print(i)
    conn.close()

if __name__ == '__main__':
    select_a()