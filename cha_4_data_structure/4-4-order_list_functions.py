#[] 
print('[]')
str_1 = 'Hello World'
list_1= [1,2,3,4,5,6]
tuple_1=('a','b','c','d')

print(str_1[0])
print(list_1[0])
print(tuple_1[0])

#Slice
print('\nSlice:')
print(str_1[1:])#ello World
print(str_1[2:])#llo World
print(str_1[-3:])#rld
print()
print(str_1[1:4])#ell
print(str_1[-5:-2])#Wor
print()
#list_1= [1,2,3,4,5,6]
print(list_1[1:])#[2, 3, 4, 5, 6]
print(list_1[2:])#[3, 4, 5, 6]
print(list_1[-3:])#[4, 5, 6]
print()
print(list_1[1:4])#[2, 3, 4]
print(list_1[-4:-2])#[3, 4]
print()
#tuple_1=('a','b','c','d')
print(tuple_1[1:])#('b', 'c', 'd')
print(tuple_1[2:])#('c', 'd')
print(tuple_1[-3:])#('b', 'c', 'd')
print()
print(tuple_1[1:4])#('b', 'c', 'd')
print(tuple_1[-4:-2])#('a', 'b')

print('\nComplexed slice:')
# [start index, stop index, interval vector] vector has direction!!!!!!!!!!!!
# str_1 = 'Hello World'
# from index 1 to 8, pick first elements every two elements interval.
print(str_1[1:8:2])#el o
# from index 1 to 8, pick first elements every three elements interval.
print(str_1[1:8:3])#eoo
print()
# from index -1 to -8, pick last elements every two elements interval.
print(str_1[-1:-8:-2])#drWo
# from index -1 to -8, pick last elements every three elements interval.
print(str_1[-1:-8:-3])#doo
#https://blog.csdn.net/xiaofeiyu321/article/details/82941765

#in
print("\n'in' function:")
#list_1= [1,2,3,4,5,6]
print(2 in list_1)#True
print(3 not in list_1)#False

print("\n'len()' function:")
print(len(list_1))#6

str_2 = 'HelloWorld'
print("\n'max()' function:")
print(max(list_1))#6
print(max(tuple_1))#d
print(max(str_2))#r ASC II 

print("\n'min()' function:")
print(min(list_1))#1
print(min(tuple_1))#a
print(min(str_2))#H

print("\nord(), return ASC II order:")
print(ord('r'))#114
print(ord('H'))#72
print(ord(' '))#32
