import time
def decorator(func):
    def wrapper(*args):
        print(time.time())
        func(*args)
    return wrapper

# decorator without parameter
@decorator
def f1():
    print('This is f1.')

# decorator with 1 parameter
@decorator
def f2(func_name):
    print('This is f2, function name: '+ func_name)

# decorator with 2 parameters
@decorator
def f3(func_name_1, func_name_2):
    print('This is f3, function name: '+func_name_1 + ', ' + func_name_2)

f1()
# 1575844153.888789
# This is f1.
f2('test func')
# 1575844153.888835
# This is f2, function name: test func
f3('test func1', 'test func2')
# 1575844153.8888419
# This is f3, function name: test func1, test func2