s = input('Score(1-100): ') # s is String
s = int(s)
if s >= 90:
    print('A')
elif s >= 80:
    print('B')
elif s >= 70:
    print('C')
else:
    print('D')

a = [] # False
if a:
    print('if')
else:
    print('else')

#short cut study case:
a = 7
b = 0
#return not False value between a and b
if a:
    print(a)
elif b:
    print(b)

#Better way:
print(a or b)