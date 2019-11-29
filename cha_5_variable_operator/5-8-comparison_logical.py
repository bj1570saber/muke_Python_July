#String comparison: compare indivitual by order. 
print('abce'<'abd') # True
#List comparison: compare indivitual by order. 
print([1,2,3,5]<[1,2,4]) # True
#Tuple comparison: compare indivitual by order. 
print((1,2,3,5)<(1,2,4)) # True
print(1==1)#True
print('~' * 20)

#logical operator
print(1 and 1)#1
print('a' and 'b')#b
print(0 or 1)#1
print(not 1)#False
print(not'')#True 
print(not 0)#True
print(not '0')#False !!!
print(not [])#True
print(not ())#True
print(not{})#True 
print('~'*20)

# or:return the return the first True value
print([1] or [])#[1]
print([] or [1])#[1]
print([] or 0)#0
print(1 and 0)#0
print(0 and 1)#0
print(1 and 2)#2
print(2 and 1)#1
#return the first value that can decide the boolean equision.
print('~'*20)

# and: return the first True value
print('a' and 'b')# b
print('' and 'b')#print nothing

#demo
if None or 2:
    print('1')
else:
    print('b')
