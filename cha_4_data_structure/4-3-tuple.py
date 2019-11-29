#Tuple Example: can not change after create.
print('Tuple example:')
tuple_1 = (1,2,'string',True)
print(type(tuple_1))#<class 'tuple'>
print(type((1)))#<class 'int'>
print(type((1,)))#<class 'tuple'>

print(tuple_1) # (1, 2, 'string', True)
# tuple_1[2] = 10 # can not assign
print(tuple_1[2]) # string
print(tuple_1[-1]) # True
print(tuple_1[0:3]) # (1, 2, 'string')
print((1,2,'string',True)[1])#2
print()

tuple_2 = (1) # a variable
print(tuple_2)# output:1
tuple_2 = (1,)# one element tuple
print(tuple_2)# output:(1,)
tuple_3 = () # empty tuple
print(tuple_3)# output:()
print(type(()))#<class 'tuple'>
print()

tuple_4 = (6,7,8)
print(tuple_1+tuple_4)
print(tuple_4 * 3)

print(list(tuple_1))
print(tuple([1,2]))