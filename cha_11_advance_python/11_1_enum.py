from enum import Enum

# Why use enum? :
class VIP(Enum): # Improve readability.
    YELLOW = 1 # different enum has different value.
    GREEN = 2 # variable name call 'key', it's unique.
    BLACK = 3 # key can not reassign new value.
    RED = 4 # Immutable during use, after define.

print(VIP.YELLOW) # VIP.YELLOW  
print(type(VIP.YELLOW)) # <enum 'VIP'>
print('~')
print(VIP.YELLOW.value) # 1
print(VIP.GREEN.name) # GREEN
print('~')
print(type(VIP.GREEN.name)) # <class 'str'>
print(VIP['GREEN'])# VIP.GREEN
print('~')
for v in VIP:
    print(v)