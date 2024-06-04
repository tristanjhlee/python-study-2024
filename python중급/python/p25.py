from libs.db.mdba import getConn

def create_table():
     conn = getConn()
     cur = conn.cursor()
     cur.execute('''
     create table sj(
     name varchar(20),
     kor int,
     eng int,
     mat int)     
     ''')
     conn.commit()
     conn.close()

if __name__ == '__main__':
    create_table()
