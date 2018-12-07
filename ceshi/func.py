# __*__encoding:utf8
# 多线程
import time
from threading import Thread

def func1(*args):
    print('enter func1')
    time.sleep(3)
    print(args)
    print('func1 is done')


def func2(*args):
    print('enter func2')
    time.sleep(5)
    print(args)
    print('func2 is done')


if __name__ == '__main__':
    t1 = Thread(target=func1, args=('小明',))
    t2 = Thread(target=func2, args=('小刚',))
    t1.start()
    t1.join(2)
    t2.start()