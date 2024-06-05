import threading
from datetime import datetime

class thread1(threading.Thread): #print datetime
    def run(self) -> None:
        for i in range(1000):
            now = datetime.now()
            print(now)

class thread2(threading.Thread): #print no 0-10000
    def run(self) -> None:
        for i in range(10000):
            print(i)

t1 = thread1()
t1.start()
t2 = thread2()
t2.daemon = True # if thread1 done, thread2 done
t2.start()

