from libs.db.mdba import getConn

def insert_a():
    conn = getConn()
    cur = conn.cursor()
    ins_query = 'insert into sj values (%s, %s, %s, %s)'
    cur.execute(ins_query, ('James', 70, 80, 90 ))
    conn.commit()
    conn.close()

# using executemany

def insert_b():
    conn = getConn()
    cur = conn.cursor()
    ins_query = 'insert into sj values (%s, %s, %s, %s)'
    li = [('Jake', 45, 93, 29), ('Ron', 63, 99, 100), ('Alex', 93, 49, 82)]
    cur.executemany(ins_query, li)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    insert_a()
    insert_b()
