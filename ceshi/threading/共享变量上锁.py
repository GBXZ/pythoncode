import threading
from time import ctime


sum = 0
loopsum = 1000000
lock = threading.Lock() #生成锁实例


def addFunc():
    global sum, loopsum, lock
    for i in range(1, loopsum):
        lock.acquire()  # 上锁
        sum += 1
        lock.release() # 释放锁


def myMinu():
    global  sum, loopsum, lock
    for i in range(1, loopsum):
        lock.acquire()
        sum -= 1
        lock.release()

def main():
    print('start main at %s' % ctime())
    t1 = threading.Thread(target=addFunc, args=())
    t2 = threading.Thread(target=myMinu, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('Done main at %s' % ctime())
    print(sum)

if __name__ == '__main__':
    main()