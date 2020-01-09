names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
print(20 * '~')

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum += x
print(sum) # 55
print(20 * '~')

sum = 0
for x in range(101): # 0...100
    sum += x
print(sum) # 5050
print(20 * '~')

# for else
print('for else:', end = ' ')
a = [[1,2,3,4],('a','b','c','d')]
for x in a:
    for y in x:
        print(y, end=' ')
else:#run after for loop.
    print('\n'+'~'*20)
# for else: 1 2 3 4 a b c d 

# break 
print('break:', end = ' ')
b = [1,2,3,4,5,6,7]
for x in b:
    if x == 4:
        break
    print(x, end=' ')
else:# Not run after break.
    print('After break.')
# break: 1 2 3 
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
# continue: 1 2 3 X
# 5 6 7 After continue.