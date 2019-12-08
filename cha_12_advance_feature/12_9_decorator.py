# decorator example:
import time
def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

def f1():
    print('This is f1')

def f2():
    print('This is f2')

f = decorator(f1)
f()

decorator(f2)()
# more in-depthdecorator explain in next example.