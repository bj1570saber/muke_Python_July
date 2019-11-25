
a = ('a', 'b', 'c')
b = ['a', 'b', 'c']
# if ther are many parameters. you can put them in a tuple or list.
def demo(param):
    print(param)
    print(type(param))

demo(a)#('a', 'b', 'c')
         #<class 'tuple'>
print('~'*20)

# another way:
def demo_1(*param):
    print(param)
    print(type(param))

demo_1(a)# it will print: 2D tuple:(('a', 'b', 'c'),)
         #<class 'tuple'>
print('~'*20)
# a fix:
demo_1(*a)#('a', 'b', 'c') #<class 'tuple'>
demo_1(*b)#('a', 'b', 'c') #<class 'tuple'>


