from libs.db.mdba import getConn

def select_a(name):
    conn = getConn()
    cur = conn.cursor()
    cur.execute('select * from sj where name like %s', (name,))
    rs = cur.fetchall() # if we print rs: [('Ron', 63, 99, 100)]
    disp(rs)
    conn.close()

def disp(rs):
    print('name: ', rs[0][0])

    tot = rs[0][1] + rs[0][2] + rs[0][3]
    print('tot: ', tot)

    avg = int(tot / 3)
    print('avg: ', avg)

if __name__ == '__main__':
    select_a('Jake')