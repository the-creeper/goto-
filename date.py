import time

def date():
    t = time.localtime()
    print(str(t.tm_year) + '/' + str(t.tm_mon) + '/' + str(t.tm_mday))
