#String comparison: compare indivitual by order. 
print('abce'<'abd')
#List comparison: compare indivitual by order. 
print([1,2,3,5]<[1,2,4])
#Tuple comparison: compare indivitual by order. 
print((1,2,3,5)<(1,2,4))
print(1==1)#True
print()

#logical operator
print(1 and 1)#1
print('a' and 'b')#b
print(0 or 1)#1
print(not 1)#False
print(not'')#True 
print(not 0)#True
print(not '0')#False 
print(not [])#True
print(not ())#True
print(not{})#True 
print()
# or:return the return the first True value
print([1] or [])#[1]
print([] or [1])#[1]
print([] or 0)#0
print(1 and 0)#0
print(0 and 1)#0
print(1 and 2)#2
print(2 and 1)#1
#return the first value that can decide the boolean equision.
print()

# and: return the first True value
print('a' and 'b')#
print('' and 'b')#print nothing

# if 1<2
#     print('1')
# else
#     print('b')
