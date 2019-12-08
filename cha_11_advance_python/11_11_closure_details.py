
def f1():
    a = 10
    def f2():
        # print(a) #UnboundLocalError: local variable 'a' referenced before assignment
        a = 20 # declare new variable
        print(a) # 20
    print(a) # 10
    f2() 
    print(a) # 10
# This is not a closure, since it did not return a inner function.
f = f1()
# print(f.__closure__) #AttributeError: 'NoneType' object has no attribute '__closure__'
print('~')

def f1():
    a = 10
    def f2():
        a = 20
    return a
f = f1()
# print(f.__closure__)# AttributeError: 'int' object has no attribute '__closure__'

print('~')

def f1():
    a = 10
    def f2():
        a = 20 # declare a new local variable, closure does not exist.
        return a
    print(a)
    return f2
f = f1()
print(f)#<function f1.<locals>.f2 at 0x1030de700>
print(f())# 20
print(f.__closure__)# None