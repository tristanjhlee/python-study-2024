# 파일을 쓸 때는 w, 파일을 읽을 때는 r
'''
f = open('/Users/JuneHyukLee/Desktop/abc.txt', 'w')
for i in range (1,8):
    f.write ('%d번째\n' %i)
f.close()
'''
'''
f = open('/Users/JuneHyukLee/Desktop/abc.txt', 'r')
m = f.readlines()
f.close()
for i in m:
    print(i, end = '')
'''



