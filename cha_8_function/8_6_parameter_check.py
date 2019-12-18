//https://www.liaoxuefeng.com/wiki/1016959663602400/1017106984190464
import math
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def quadratic(a, b, c):
    if not (isinstance(a, int) and isinstance(a, int) and isinstance(a, int)):
    #if not (a is int) and (b is int) and (c is int): # both work
        raise TypeError("wrong input.")
    x = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
    y = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
    return x, y

a,b = quadratic(2, 3, 1)
print(a)
print(b)

