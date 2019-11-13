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

