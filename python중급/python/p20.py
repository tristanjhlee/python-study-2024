#DB 활용 (전화번호부)

import sqlite3
from libs.db.dba import getConn

class Db:
    conn = getConn('/Users/JunehyukLee/Desktop/python 중급 test/phon.db')
    cur = conn.cursor()

    def createtable(self):
        Db.cur.execute('create table tell(name text,no text)')

    def insert(self):
        self.name = input('name: ')
        self.no = input('no: ')
        self.sql = 'insert into tell values (?,?)'
        Db.cur.execute(self.sql, (self.name, self.no))

    def select(self):
        self.sql = 'select * from tell'
        Db.cur.execute(self.sql)
        rs = Db.cur.fetchall()
        print('View Data')
        for k,v in rs:
            print(k, v)

    def delete(self):
        self.name = input('name: ')
        self.sql = 'delete from tell where name = ?'
        Db.cur.execute(self.sql, (self.name,))

    def update(self):
        self.name = input('name: ')
        self.no = input('no: ')
        self.sql = 'update tell set no = ? where name = ?'
        Db.cur.execute(self.sql, (self.no, self.name))

def main():
    d = Db()
    while True:
        n = input('a. Create table 1.Insert 2. Select (View) 3. Delete 4. Update 0. Quit')

        if n == 'a':
            d.createtable()

        if n == '1':
            d.insert()

        if n == '2':
            d.select()

        if n == '3':
            d.delete()

        if n == '4':
            d.update()

        if n == '0':
            d.conn.commit()
            d.conn.close()
            break

    print('Quit')

if __name__ == '__main__':
    main()