from enum import Enum

class VIP(Enum): 
    YELLOW = 1 
    GREEN = 2 
    BLACK = 3 
    RED = 4 

result = VIP.GREEN == VIP.YELLOW
print(result)#False

result = VIP.GREEN == VIP.GREEN
print(result)#True

result = VIP.GREEN == 2
print(result)#False

# result = VIP.GREEN > VIP.YELLOW
# print(result)#TypeError: '>' not supported between instances of 'VIP' and 'VIP'
print('~')
result = VIP.GREEN is VIP.GREEN
print(result)#True


class VIPQ(Enum): 
    YELLOW = 1 
    GREEN = 2 
    BLACK = 3 
    RED = 4 

result = VIP.GREEN == VIPQ.GREEN
print(result)#False