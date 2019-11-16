#loop print:
#range make a list of number.
for x in range(0,11,2):# start point, end point(not include), interval,
    print(x, end = ' | ')# 0 | 2 | 4 | 6 | 8 | 10 |
print()

for x in range(11,0, -2):# start point, end point(not include), vector,
    print(x, end = ' | ')# 11 | 9 | 7 | 5 | 3 | 1 |
print()

a = [1,2,3,4,5,6]
for x in range(0,len(a)):
    print(a[x], end = ', ')# 1, 2, 3, 4, 5, 6,
print()

a = [1,2,3,4,5,6]
for x in range(len(a)-1, -1, -1): # reverse order
    print(a[x], end = ', ')# 6, 5, 4, 3, 2, 1, 
print()

for x in range(0,len(a),2):
    print(a[x], end = ', ')# 1, 3, 5, 
print()

#slice
b = a[0: len(a): 2]
print(b)#[1, 3, 5]
