from enum import Enum
# Improve readability.
class VIP(Enum): 
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

print(VIP.YELLOW) # VIP.YELLOW  
print(type(VIP.YELLOW)) #<enum 'VIP'>
