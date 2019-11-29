# for else
print('for else:', end = ' ')
a = [[1,2,3,4],('a','b','c','d')]
for x in a:
    for y in x:
        print(y, end=' ')
else:#run after for loop.
    print('\n'+'~'*20)

# break 
print('break:', end = ' ')
b = [1,2,3,4,5,6,7]
for x in b:
    if x == 4:
        break
    print(x, end=' ')
else:# Not run after break.
    print('After break.')
print('\n'+'~'*20)

# continue
print('continue:', end=' ')
for x in b:
    if x == 4:
        print('X')
        continue
    print(x, end = ' ')
else:# run after continue 
    print('After continue.')
print()

while x in b:
    print(x, end = ' ')