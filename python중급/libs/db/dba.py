#커넥션 생성 코드

import sqlite3

def getConn():
    conn = sqlite3.connect("/Users/JuneHyukLee/Desktop/python 중급 test/abc.db")
    return conn

