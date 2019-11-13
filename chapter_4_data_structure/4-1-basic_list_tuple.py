#List example:
students= ['Jerry','Tom','Adm',10, True]
print('students[0]:%s' %(students[0]))
print('students[-1]:%s' %(students[-1]))
print('students[-2]:%s' %(students[-2]))
students.append('Jack')#append
print('students[-2]:%s' %(students[-2]))
print(students)
students.insert(1, 'Bob')#insert
print(students)
students.pop()#pop
print(students)
students.pop(0)
print('length: %d' %len(students))
print(students)
students.insert(2,['asp', 'php'])
print(students)
print(students[2][1])

#Tuple Example: can not change after create.
tuple_1 = (1,2,'string',True)
print(tuple_1) # (1, 2, 'string', True)
# tuple_1[2] = 10 # can not assign
print(tuple_1[2]) # string
print(tuple_1[-1]) # True

tuple_2 = (1) # a variable
print(tuple_2)# output 1
tuple_2 = (1,)# one element tuple
print(tuple_2)# output: (1,)
tuple_3 = () # empty tuple
print(tuple_3)

