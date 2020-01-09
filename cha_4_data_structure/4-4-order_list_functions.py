# [] get value by index:
print('[]')
str_1 = '0123456789'
list_1= [0,1,2,3,4,5,6,7,8,9]
tuple_1=('0','1','2','3','4','5','6','7','8','9')

print(str_1[0]) # 0
print(list_1[0]) # 0
print(tuple_1[0]) # 0

# Slice
print('\nSlice:')
print(str_1[:3])#012    start from index 0 to 3(exclusive)
print(str_1[2:])#23456789
print(str_1[-3:])#789
print()
print(str_1[1:4])#123
print(str_1[-5:-2])#567
print()

print(list_1[1:])#[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_1[2:])#[2, 3, 4, 5, 6, 7, 8, 9]
print(list_1[-3:])#[7, 8, 9]
print()
print(list_1[1:4])#[1, 2, 3]
print(list_1[-4:-2])#[6, 7]
print()

print(tuple_1[1:])#('1', '2', '3', '4', '5', '6', '7', '8', '9')
print(tuple_1[2:])#('2', '3', '4', '5', '6', '7', '8', '9')
print(tuple_1[-3:])#('7', '8', '9')
print()
print(tuple_1[1:4])#('1', '2', '3')
print(tuple_1[-4:-2])#('6', '7')

print('\nComplexed slice:') 
# [start index, stop index, interval vector] vector has direction!!!!!!!!!!!!

# from index 1 to 8, take a element every 2 element.
print(str_1[1:8:2])#1357

# from index 1 to 8, pick a element every 3 elements.
print(str_1[1:8:3])#147
print()

# all negative number:

# from index -1 to -8, pick a element every two elements.
print(str_1[-1:-8:-2]) # 9753 direction from right to left

# from index -1 to -8, pick a element every three elements.
print(str_1[-1:-8:-3]) # 963
#https://blog.csdn.net/xiaofeiyu321/article/details/82941765

#in
print("\n'in' function:")
#list_1= [1,2,3,4,5,6]
print(2 in list_1) # True
print(3 not in list_1) # False

#len()
print("\n'len()' function:")
print(len(list_1)) # 10

#max()
print("\n'max()' function:")
print(max(list_1)) # 9
print(max(tuple_1)) # 9
print(max(str_1)) # 9 ASC II 

#min()
print("\n'min()' function:")
print(min(list_1)) # 0
print(min(tuple_1)) # 0
print(min(str_1)) # 0

#ord()
print("\nord(), return ASC II order:")
print(ord('r'))#114
print(ord('H'))#72
print(ord(' '))#32


# develop a trim() funciton by slice:
# 练习:利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    if s[:1] == ' ':
        return trim(s[1:])
    elif s[-1:] == ' ':
        return trim(s[:-1])
    else:
        return s

new = trim('     love     ')
print(new)

astr = ''
print(astr[-1:-3])   #it's ok, no error
