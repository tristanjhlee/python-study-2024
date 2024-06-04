#커넥션 생성 코드

import sqlite3

def getConn(dbpath):
    conn = sqlite3.connect(dbpath)
    return conn

