print('-1:', type(-1))# -1: <class 'int'>
n = 2
print('n: ', type(n))# n:  <class 'int'>
m = 3.14
print('m: ', type(m))# m:  <class 'float'>
print('1.111: ',type(1.111))#1.111:  <class 'float'>
print('~')
print('1+1 =', 1+1, type(1+1))# 1+1 = 2 <class 'int'>
print('1+1.0 =', 1+1.0, type(1+1.0))# 1+1.0 = 2.0 <class 'float'>
print('~~~')
print('2-1 =', 2-1, type(2-1))# 2-1 = 1 <class 'int'>
print('2-1.0 =', 2-1.0, type(2-1.0))# 2-1.0 = 1.0 <class 'float'>
print('~~~~~')
print('1*1 =', 1*1, type(1*1))# 1*1 = 1 <class 'int'>
print('1*1.0 =', 1*1.0, type(1*1.0))# 1*1.0 = 1.0 <class 'float'>
print('~'*20)
# / operator output:
print('/ operator output: ')
print('3/2 = ', 3/2)# 3/2 =  1.5
print('3/2 : %s' %type(3/2))#3/2 : <class 'float'>
print('~')
print('3/1 = ', 3/1)# 3/1 =  3.0
print('3/1 : ', type(3/1))#3/1 : <class 'float'>
print('~~~~')
print('3.0/2 = ',3.0/2)#3.0/2 =  1.5
print('3.0/2 : ',type(3.0/2))#3.0/2 :  <class 'float'>
# / laways get float type accurate result. No matter apply on int or float.

print('~'*20)
# // operator output: int
print('// operator output: int')
print('1//1 = ', 1//1)# 1//1 =  1
print('1//1 : ', type(1//1))#1//1 :  <class 'int'>
print('~')
print('3//2 = ',3//2) # 3//2 =  1
print('3//2 : ',type(3//2))#3//2 :  <class 'int'>
print('~')
print('4.0//2 = ', 4.0//2) # 4.0//2 =  2.0
print('4.0//2 : ', type(4.0//2))# 4.0//2 :  <class 'float'>
print('~')
print('4//2.0 = ', 4//2.0) # 4//2.0 =  2.0
print('4//2.0 : ', type(4//2.0))# 4//2.0 :  <class 'float'>
# int -> int type result; float -> float type result;
print('~'*20)

# modulo %
print('10 % 3 = ', 10 % 3)# 10 % 3 =  1
print(type(10 % 3))# <class 'int'>

# Assign value to a variable is connecting them together.
# Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）。
