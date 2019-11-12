names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum += x
print(sum)

sum = 0
for x in range(101): # 0...100
    sum += x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print(name)

# break:
num = 0
while num < 100:
    if(num >= 10):
        break
    num += 1
    print(num)
print('End.')

# continue
# print Odd number only (1-10)
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num)
print('End.')