from enum import Enum

class VIP(Enum): 
    YELLOW = 1 
    YELLOW_ALIAS = 1
    BLACK = 3 
    RED = 4 

print(VIP.YELLOW_ALIAS)# VIP.YELLOW    note:  not VIP.YELLOW_ALIAS
print('~')

for v in VIP:
    print(v)# not gonna print alias
# VIP.YELLOW
# VIP.BLACK
# VIP.RED

for v in VIP.__members__.items():
    print(v)
# ('YELLOW', <VIP.YELLOW: 1>)
# ('YELLOW_ALIAS', <VIP.YELLOW: 1>)
# ('BLACK', <VIP.BLACK: 3>)
# ('RED', <VIP.RED: 4>)

for v in VIP.__members__:
    print(v)
# YELLOW
# YELLOW_ALIAS
# BLACK
# RED