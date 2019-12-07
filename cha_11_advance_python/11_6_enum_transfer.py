from enum import Enum, IntEnum, unique

class VIP(Enum): 
    YELLOW = 1 
    YELLOW_ALIAS = 1
    BLACK = 3 
    RED = 4 

a = 1 # suppost I got 1 as value from database.
# looking for the key of enum:
print(VIP(a))# VIP.YELLOW
print('~')
@unique# decorater：all value must be unique.
class VIPI(IntEnum): # IntEnum parent class force child class's enum value are integer.
    YELLOW = 1 
   #YELLOW_ALIAS = 'str' # ValueError: invalid literal for int() with base 10: 'str'
    BLACK = 3 
    #RED = 3
    #ValueError: duplicate values found in <enum 'VIPI'>: RED -> BLACK

for v in VIPI:
    print(v)

