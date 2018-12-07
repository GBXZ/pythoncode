from multiprocessing import Process
import os


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process', os.getppid())
    print('process id:', os.getpid())


def f(name):
    print('Hello %s' % name)
    print(os.getpid())


def q(name):
    print('Hello %s' % name)
    print(os.getpid())


if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('xiaoming',))
    d = Process(target=q, args=('xiaohu', ))
    p.start()
    d.start()
    d.join()
    p.join()