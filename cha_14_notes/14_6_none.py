# None is not: '', [], 0, False
a = ''
b = False
c = []

print(a == None)#False
print(b == None)#False
print(c == None)#False
print(a is None)#False
print(None)#None 
print(type(None))#<class 'NoneType'>

# If Else Control:
def fun():
    return None

a = fun()
if not a: # better
    print('S')
else:
    print('F')

if a is None: # DO NOT USE
    print('S')
else:
    print('F')

list_a = [None, '', [], False, 0, (), {None}]# {None} -> True
i = 0
while i< len(list_a) and not list_a[i]:
    i += 1
    print(a)
print('End')
    