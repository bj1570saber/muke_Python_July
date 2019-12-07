from enum import Enum

class VIP(Enum): 
    YELLOW = 1 
    YELLOW_ALIAS = 1
    BLACK = 3 
    RED = 4 

a = 1 # suppost I got 1 as value from database.
# looking for the key of enum:
print(VIP(a))# VIP.YELLOW
