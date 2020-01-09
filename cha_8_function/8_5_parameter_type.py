def double_skill_1_combine(skill_1,skill_2):
    return skill_1 * 2 + skill_2

# 1.必须参数(位置参数)positional arguments：
print(double_skill_1_combine(1,2))# 4

# 2.关键字参数 keyword parameter：arguemnts' order doesnt matter.
d = double_skill_1_combine(skill_2 = 2, skill_1 = 1 )
print(d)# 4

# 3. 默认参数 default argument
def print_student_files(name,gender = "male", age = 20, city = "SD"):
    print("My name is " + name)
    print("I am " + str(age) + " years old.")
    print("I'm "+ gender)
    print("I live in " + city)

print_student_files("Jerry", "male", 28, "SD")
# My name is Jerry
# I am 28 years old.
# I'm male
# I live in SD
print('~'*20)

print_student_files("Tom")
# other fields will be fill up with default value.
# My name is Tom
# I am 20 years old.
# I'm male
# I live in SD
print('~'*20)

print_student_files("Jeremy", "female", 25)
# name argument must pass in since no default value. 
# All arguments need to be in order.
# My name is Jeremy
# I am 25 years old.
# I'm female
# I live in SD
print('~'*20)

# if some default arguments need to be pass in unordered - keyword parameter. 
print_student_files("Larry",age = 30)
# default arguments must pass in after regular arguemnts.
# My name is Larry
# I am 30 years old.
# I'm male
# I live in SD

# Default argument follows Non-default argument .
# def func(name, gender = 'male', age):# SyntaxError: 
#                               # non-default argument follows default argument
#     print(name + gender + str(age))
# func('j',25)

def func(name, age, gender = 'male'):
    print(name, age, gender)

func('A',25) #A 25 male

'''
设置默认参数时，有几点要注意：
一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
二是如何设置默认参数。

当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
使用默认参数有什么好处？最大的好处是能降低调用函数的难度。

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
有多个默认参数时，调用的时候，既可以按顺序提供默认参数，比如调用enroll('Bob', 'M', 7)，
    意思是，除了name，gender这两个参数外，最后1个参数应用在参数age上，city参数由于没有提供，
    仍然使用默认值。
也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。比如调用
    enroll('Adam', 'M', city='Tianjin')，意思是，city参数用传进去的值，
    其他默认参数继续使用默认值。

默认参数有个最大的坑，演示如下：
先定义一个函数，传入一个list，添加一个END再返回：

def add_end(L=[]):
    L.append('END')
    return L
当你正常调用时，结果似乎不错：

>>> add_end([1, 2, 3])
[1, 2, 3, 'END']
>>> add_end(['x', 'y', 'z'])
['x', 'y', 'z', 'END']

当你使用默认参数调用时，一开始结果也是对的：
>>> add_end()
['END']
但是，再次调用add_end()时，结果就不对了：
>>> add_end()
['END', 'END']
>>> add_end()
['END', 'END', 'END']

很多初学者很疑惑，默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。
原因解释如下：
Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，
它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，
不再是函数定义时的[]了。

定义默认参数要牢记一点：默认参数必须指向不变对象！

要修改上面的例子，我们可以用None这个不变对象来实现：
def add_end(L= None):
    if L is None:
        L = []
    L.append('END')
    return L

现在，无论调用多少次，都不会有问题：
>>> add_end()
['END']
>>> add_end()
['END']
为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，
这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，
同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。
'''