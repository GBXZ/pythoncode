# _*_coding:utf-8_*_

from multiprocessing import Process, queues, Queue
import time
import random
import os


def consumer(q, name):
    while True:
        res = q.get()
        time.sleep(random.randint(1, 3))
        print("\033[43m %s 吃%s\033[0m" % (name, res))


def producer(q, name, food):
    for i in range(3):
        time.sleep(random.randint(1, 3))
        res = "%s %s" % (food, i)
        q.put(res)
        print("\033[45m %s 生产了 %s\033[0m" % (name, res))


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=producer, args=(q, 'egon', '包子'))
    c1 = Process(target=consumer, args=(q, 'yaoming'))
    p1.start()
    c1.start()


