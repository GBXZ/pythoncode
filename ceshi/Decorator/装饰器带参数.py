# _*_ encoding:utf8 _*_
# 装饰器

loggin_state = False


def loggin(func):

    def inner(*args,**kwargs):
        global loggin_state
        username = input('输入你的用户名：')
        password = input('输入你的密码：')
        if username == 'abc' and password == '123':
            loggin_state = True
        else:
            print('输入错误')
        if loggin_state == True:
            func(*args,**kwargs)
    return inner


@loggin
def japan(style):
    print('日本专区',style)


japan('a')
