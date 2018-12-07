import threading
from time import ctime


sum = 0
loopsum = 10000000


def addFunc():
    global sum, loopsum
    for i in range(1, loopsum):
        sum += 1


def myMinu():
    global  sum, loopsum
    for i in range(1, loopsum):
        sum -= 1

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