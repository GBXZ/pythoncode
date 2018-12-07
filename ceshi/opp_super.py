
def decorater(func):
    def output():
        print('i am output')
        func()
    return output


@decorater
class MyClass(object):
    pass


if __name__ == '__main__':
    a = MyClass()


