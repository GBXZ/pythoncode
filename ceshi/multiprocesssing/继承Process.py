#  _*_coding:utf8 _*_

import multiprocessing
import time
import os


class ClockProcess(multiprocessing.Process):
    def __init__(self, name):
        super(ClockProcess, self).__init__()   # 继承Process的__init__方法功能
        self.name = name

    def run(self):  # 多进程也是Process run方法中执行，所以重写run方法即可
        while 1:
            time.sleep(3)
            print('hi, %s i am start process at %s' % (self.name, time.ctime()))
            print(os.getpid())


if __name__ == '__main__':
    print(os.getppid())
    P = ClockProcess('Jhno')
    Q = ClockProcess('Yao')
    Q.start()
    P.start()
    P.join()
    Q.join()
