
def a(self):
    pass
print(type(a))#<class 'function'>
print('~')

def curve_pre_1():
    def curve_1():
        print('curve_1()')
    return curve_1
    
f = curve_pre_1()
f()#curve_1()
print('~')

def curve_pre():
    a = 25
    def curve(x):
        return a * x * x # a = 25 was passed in as parameter
    return curve
    
a = 10 # this a will not effect founction f's a value.
f = curve_pre()
print(f(2)) #100
# 闭包：闭包就是能够读取其他函数内部变量的函数。例如在javascript中，
# 只有函数内部的子函数才能读取局部变量，所以闭包可以理解成“定义在一个函数内部的函数“。
# 在本质上，闭包是将函数内部和函数外部连接起来的桥梁。 闭包 = 函数+环境变量
print(f.__closure__) # The address that closure saved at.
#(<cell at 0x10692cdc0: int object at 0x106831d90>,)
print(f.__closure__[0].cell_contents) # 25