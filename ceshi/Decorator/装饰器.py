# _*_ encoding:utf8 _*_
# 装饰器

loggin_state = False


def loggin(func):

    def inner():
        global loggin_state
        username = input('输入你的用户名：')
        password = input('输入你的密码：')
        if username == 'abc' and password == '123':
            loggin_state = True
        else:
            print('输入错误')
        if loggin_state == True:
            func()
    return inner


@loggin
def japan():
    print('日本专区')


japan()



