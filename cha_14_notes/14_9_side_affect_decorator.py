# decorator-> side affect: name will be changed
import time
def decorator(func):
    def p():
        print('Print this first.')

    def wrapper():
        p()
        print(time.time())
        func()
    return wrapper


def f_1():
    '''
    This is f_1() documentation
    '''
    print('This is f_1()')
    print(f_1.__name__)#f_1

f_1()
@decorator
def f_2():
    '''
    This is f_2() documentation
    '''
    print('This is f_2()')
    print(f_2.__name__)# wrapper  -name was changed

f_2()

# print(help(f_1))
# print(help(f_2))

from functools import wraps
def decorator_2(func):
    def p():
        print('Print this first.')
    @wraps(func)
    def wrapper():
        p()
        print(time.time())
        func()
    return wrapper

@decorator_2
def f_3():
    '''
    This is f_3() documentation
    '''
    print('This is f_3()')
    print(f_3.__name__)# f_3

f_3()
