# for else
a = [[1,2,3,4],('a','b','c','d')]
for x in a:
    for y in x:
        print(y, end=' ')
else:#run after for loop.
    print()

# break 
b = [1,2,3,4,5,6,7]
for x in b:
    if x == 4:
        break
    print(x)
else:# Not run after break.
    print('After break.')
print()

# continue
for x in b:
    if x == 4:
        continue
    print(x)
else:# run after continue 
    print('After continue.')
print()