#List example:
students= ['Jerry','Tom','Adm',10, True]
print(students)
print('students[0]:%s' %(students[0])) # Jerry
print('students[-1]:%s' %(students[-1]))#True
print('students[-2]:%s' %(students[-2]))#10
students.append('Jack')#append()
print('students[-2]:%s' %(students[-2]))#True
print(students)# ['Jerry', 'Tom', 'Adm', 10, True, 'Jack']
students.insert(1, 'Bob')#insert()
print(students)#['Jerry', 'Bob', 'Tom', 'Adm', 10, True, 'Jack']
students.pop()#pop
print(students)#['Jerry', 'Bob', 'Tom', 'Adm', 10, True]
students.pop(0)
print(students)#['Bob', 'Tom', 'Adm', 10, True]
print('length: %d' %len(students))#5
students.insert(2,['asp', 'php'])
print(students)#['Bob', 'Tom', ['asp', 'php'], 'Adm', 10, True]
print(students[2][1])#php

sentence = 'I love Python.'
print(sentence[0])#I
print(sentence[-3:])#on.
a = 'a'
b = 'b'
a = a + b 
print(a)#ab
print(a*3)

students= ['Jerry','Tom','Adm',10, True]
print(students[0])#Jerry    this is a element
print(students[-1:])#[True] this is a list
c = ['c']
d = ['d']
c = c + d
print(c)#['c', 'd']
print(d)#['d']
print(d*3)#['d', 'd', 'd']


#Tuple Example: can not change after create.
print('\nTuple example:')
tuple_1 = (1,2,'string',True)
print(tuple_1) # (1, 2, 'string', True)
# tuple_1[2] = 10 # can not assign
print(tuple_1[2]) # string
print(tuple_1[-1]) # True

tuple_2 = (1) # a variable
print(tuple_2)# output:1
tuple_2 = (1,)# one element tuple
print(tuple_2)# output:(1,)
tuple_3 = () # empty tuple
print(tuple_3)# output:()

