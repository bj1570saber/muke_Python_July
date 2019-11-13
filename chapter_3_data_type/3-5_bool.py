print(type(True))# <class 'bool'>
print(int(True)) # 1
print(int(False)) # 0 
print()

print(bool(1)) # True
print(bool(1.5)) # True
print(bool(10)) # True
print(bool(-2)) # True
print()

print(bool(0)) # False

print('\nString:')
print(bool('\nabc')) # True
print(bool('')) # False

print('\nList:')
print(bool([1,2,3])) # True
print(bool([]))     # False

print('\nTuple:')
print(bool({1,2,3})) # True
print(bool({}))     # False

print('\nDict:')
print(bool({1:2,3:4})) # True
#print(bool({}))     # False

print('\nNull:')
print(bool(None))