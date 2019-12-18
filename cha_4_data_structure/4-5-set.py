# No order group
set_1 = {1,1,2,2,3,3,4,4,5,5,6,6}
#print(set_1[2]) #error
#print(set_1[1:3]) #error

print(set_1)#{1, 2, 3, 4, 5, 6} remove duplicated items
set_2 = {3,4,8}
print(set_1 - set_2)#remove set_2 elements.{1, 2, 5, 6}
print(set_1)#{1, 2, 3, 4, 5, 6} above code does not change set_1
print(set_1 & set_2)# {3,4} find out intersection.
print(set_1 | set_2)# {1, 2, 3, 4, 5, 6, 8} union

print('\nCreate a empty Set:')
print(type({}))#<class 'dict'>
set_3 = set([1,2,3])
print('set_3: ',set_3)
set_3 = set() # create an empty set.
print('set_3: ',set_3)#set()
print(type(set()))#<class 'set'>

# Insert an element
set_3.add(1)
set_3.add('1')
set_3.add(2)
print(set_3)
set_3.add(1)# set_3 already contains 1, no changes.

# Delete an element
set_3.remove('1')
print(set_3)
set_3.pop() # Remove and return an arbitrary set element. 
            # Raises KeyError if the set is empty.

# Search an element
print(3 in set_1)#True
print(3 not in set_1)#False
