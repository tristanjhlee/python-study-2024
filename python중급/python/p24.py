# (가변인자 전달 - variable argument)

config  = {
    'user': 'root',
    'password': '    ',
    'host': '127.0.0.1',
    'database': 'pydb',
    'port': '3306'
}

'''
def get_Conn(*con): # *con: tuple (1,2,3,4)
    print(con)

get_Conn(1,2,3,4)
'''
'''
def get_Conn(**con): # **con dictionary
    print(con)

get_Conn(a = 1, b = 2, c = 3, d = 4)
'''

def get_Conn(**con):
    print(con)

get_Conn(**config)

