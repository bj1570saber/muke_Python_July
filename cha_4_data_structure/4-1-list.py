#List example:
students= ['Jerry','Tom','Adm',10, True]
print(type(students))#<class 'list'>
print(type((1)))#<class 'int'>
print(type([1]))#<class 'list'>
print(type([1,]))#<class 'list'>

print(students)
print('students[0]:%s' %(students[0])) # Jerry
print('students[-1]:%s' %(students[-1]))#True
print('students[-2]:%s' %(students[-2]))#10

students.append('Jack')#append()
print(students)# ['Jerry', 'Tom', 'Adm', 10, True, 'Jack']
print('students[-2]:%s' %(students[-2]))#True  
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
print(len(students))# 6

sentence = 'I love Python.'
print(sentence[0])#I
print(sentence[-3:])#on.
a = 'a'
b = 'b'
a = a + b 
print(a)#ab
print(a*3)#ababab

students= ['Jerry','Tom','Adm',10, True]
print(students[-1])#True    this is a element
print(students[-1:])#[True] this is a list
c = ['c']
d = ['d']
c = c + d
print(c)#['c', 'd']
print(d)#['d']
print(d*3)#['d', 'd', 'd']

