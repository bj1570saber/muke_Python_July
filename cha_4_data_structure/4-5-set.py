#no order group
set_1 = {1,1,2,2,3,3,4,4,5,5,6,6}
#print(set_1[2]) #error
#print(set_1[1:3]) #error
print(3 in set_1)#True
print(3 not in set_1)#False
print(set_1)#{1, 2, 3, 4, 5, 6} remove duplicated items
set_2 = {3,4,8}
print(set_1 - set_2)#remove set_2 elements.{1, 2, 5, 6}
print(set_1 & set_2)#{3,4} find out intersection.
print(set_1 | set_2)

print('\nCreate a empty Set:')
print(type({}))#<class 'dict'>
set_3 = set() # create an empty set.
print(set_3)#set()
print(type(set()))#<class 'set'>