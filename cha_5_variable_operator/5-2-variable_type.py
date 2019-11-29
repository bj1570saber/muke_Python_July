#print = 1  #error, so do not use system function name as variable

'''
声明一个值类型变量，编译器会在栈上分配一个空间，这个空间对应着该值类型变量，
空间里存储的就是该变量的值。引用类型的实例分配在堆上，新建一个引用类型实例，
得到的变量值对应的是该实例的内存分配地址，这就像您的银行账号一样。
'''

#http://net-informations.com/faq/general/valuetype-referencetype.htm
#值类型-Value type：int, str, tuple,
'''
A Value Type stores its contents in memory allocated on the stack. 
A single space in memory is allocated to store the value and 
that variable directly holds a value. If you assign it to another variable, 
the value is copied directly and both variables work independently.
(copy by value)
'''

#https://blog.csdn.net/qq_28632639/article/details/86689278
# int, str, tuple (immutable)

# str: copy by reference
str_1 = 'Hello'
str_2 = str_1
print(id(str_1))#4328531248
print(id(str_2))#4328531248
str_1 = 'h'
print(id(str_1))#4328244976
print(id(str_2))#4328531248
# str_1[0] = 'h' #'str' object does not support index assignment
print('~'*20)

# int: copy by reference
a = 1
print(id(a))#4398733968  id() can get variable's address 
b = a
print(id(b))#4398733968
a = 3
print(id(a))#4398734032
print(b) #1
print('~'*20)

# 
print(hex(id(a)))
print(oct(id(a)))
print(bin(id(a)))
print(int(id(a)))#4398734032
print(id(a))#4398734032
print('~'*20)

# tuple : copy by reference
tuple_1 = (1,2,3,[4,5,6]) # immutable
print(id(tuple_1))# 4306553488
print(tuple_1[3][0])#4
tuple_1[3][0]=9 #update inner list value
print(id(tuple_1))# 4306553488 # address did not change
print(tuple_1)#(1, 2, 3, [9, 5, 6])  inner list can be changed
tuple_2 = tuple_1
print(id(tuple_2))# 4306553488
tuple_1 = (6,7,8)
print(id(tuple_1))# 4315806848
print(id(tuple_2))# 4306553488
print('~'*20)

# set: copy by reference
set_1 = {1,2,3}
set_2 = set_1
print(id(set_1))#4465583264
print(id(set_2))#4465583264

set_1 = {4,5,6}
print(id(set_1))#4306830272 #
print(id(set_2))#4465583264
print('~'*20)

# list: copy be reference
list_1 = [1,2,3]
list_2 = list_1
print(id(list_1))#4386051904
print(id(list_2))#4386051904
list_1 = [4,5,6]
print(id(list_1))#4460576512 #
print(id(list_2))#4386051904
print('~'* 20)

# dict:
dict_1 = {1:'a', 2:'b', 3:'c'}
dict_2 = dict_1
print(id(dict_1))#4386810112
print(id(dict_2))#4386810112
dict_1 = {4:'d', 5:'e', 6:'f'}
print(id(dict_1))#4476816000
print(id(dict_2))#4386810112

#引用类型-Reference Types
#list, set, dict (mutable  )
'''
Reference Types are used by a reference which holds a reference (address) 
to the object but not the object itself. Because reference types represent 
the address of the variable rather than the data itself, assigning 
a reference variable to another doesn't copy the data. Instead it creates 
a second copy of the reference, which refers to the same location of the heap
as the original value. Reference Type variables are stored in a different 
area of memory called the heap.

'''