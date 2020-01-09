# https://www.liaoxuefeng.com/wiki/1016959663602400/1017261630425888
a = ('a', 'b', 'c')
b = ['a', 'b', 'c']
# if ther are many parameters. you can put them in a tuple or list.
def demo(param):
    print(param)
    print(type(param))

demo(a) #('a', 'b', 'c') #<class 'tuple'>
demo(b) #['a', 'b', 'c'] #<class 'list'>
print('~'*20)

# another way:
def demo_1(*param):
    print(param)
    print(type(param))

demo_1(a)# it will print: 2D tuple:(('a', 'b', 'c'),)
         # <class 'tuple'>
print('~'*20)
# a fix:
demo_1(*a)#('a', 'b', 'c') #<class 'tuple'>
demo_1(*b)#('a', 'b', 'c') #<class 'tuple'>
print('~'*20)

# * function -> make a list or derefference a list
# different type parameter's order：必须参数，默认参数，可变参数
def demo_2(param1, param2=2, *param):
    print(param1)
    print(param2)
    print(param)
    
demo_2('a',1,2,3,4,'param')
# a
# 1
# (2, 3, 4, 'param')
print('~'*20)

def demo_3(param1, *param, param2=2):
    print(param1)
    print(param2)
    print(param)

demo_3('a',1,2,3,4,'param')
# interpreter will automatically move param2's default value 
# to the second place of the parameter list.

# a
# 2 
# (1, 2, 3, 4, 'param')

# demo_2 and demo_3 are too complicate. 
# Even not stable in different version of python.

# Keep parameter simple for other programer to use.