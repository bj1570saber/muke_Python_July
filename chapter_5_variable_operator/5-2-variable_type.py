'''
print = 1
print(1) #error, so do not use system function as variable
'''
'''
声明一个值类型变量，编译器会在栈上分配一个空间，这个空间对应着该值类型变量，
空间里存储的就是该变量的值。引用类型的实例分配在堆上，新建一个引用类型实例，
得到的变量值对应的是该实例的内存分配地址，这就像您的银行账号一样。

'''
#http://net-informations.com/faq/general/valuetype-referencetype.htm
#值类型-Value type：
'''
A Value Type stores its contents in memory allocated on the stack. 
A single space in memory is allocated to store the value and 
that variable directly holds a value. If you assign it to another variable, 
the value is copied directly and both variables work independently.
(copy by value)
'''
# int, str, tuple (immutable)
str_1 = 'Hello'
#str_1[0] = 'h' #'str' object does not support item assignment

print(str_1)
a = 1
print(id(a))#4398733968  id() can get variable's address 
b = a
print(id(b))#4398733968
a = 3
print(id(a))#4398734032
print(b)

print(hex(id(a)))
print(oct(id(a)))
print(bin(id(a)))
print(int(id(a)))#4398734032
print(id(a))#4398734032

tuple_1 = (1,2,3,[4,5,6])
print(tuple_1[3][0])#4
tuple_1[3][0]=9
print(tuple_1)#(1, 2, 3, [9, 5, 6])  inner list can be changed

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