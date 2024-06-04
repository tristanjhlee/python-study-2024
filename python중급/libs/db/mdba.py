import mysql.connector

config  = {
    'user': 'root',
    'password': '    ',
    'host': '127.0.0.1',
    'database': 'pydb',
    'port': '3306'
}

def getConn():
    conn = mysql.connector.connect(**config)
    return conn