# contacts creator

from libs.db.mdba import getConn

class Db:
    conn = getConn()
    cur = conn.cursor()

    def create_table (self):
        Db.cur.execute('create table contact(name text, no text)')

    def insert (self):
        self.name = input('name: ')
        self.no = input('no: ')
        self.sql = 'insert into contact values (%s, %s)'
        Db.cur.execute(self.sql, (self.name, self.no))
        Db.conn.commit()

    def select (self):
        self.sql = 'select * from contact'
        Db.cur.execute(self.sql)
        rs = Db.cur.fetchall()
        for k, v in rs:
            print (k, v)

    def delete (self):
        self.name = input('name: ')
        self.sql = 'delete from contact where name = %s'
        Db.cur.execute(self.sql, (self.name,))
        Db.conn.commit()

    def update (self):
        self.name = input('name: ')
        self.no = input('no: ')
        self.sql = 'update contact set no = %s where name = %s'
        Db.cur.execute(self.sql, (self.no, self.name))
        Db.conn.commit()

def main():
    d = Db()
    while True:
        n = input('a.create table 1.insert 2.select 3.delete 4.update 0.quit: ')

        if n == 'a':
            d.create_table()

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

    print('done')

if __name__ == '__main__':
    main ()