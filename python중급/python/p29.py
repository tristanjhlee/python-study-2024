# delete & update

from libs.db.mdba import getConn
'''
def delete_a(name):
    conn = getConn()
    cur = conn.cursor()
    cur.execute('delete from sj where name = %s', (name,))
    conn.commit()
    conn.close()
'''
def update_a(name, kor_score):
    conn = getConn()
    cur = conn.cursor()
    cur.execute('update sj set kor = %s where name = %s', (kor_score, name))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    #delete_a('Ron')
    update_a('James', 100)