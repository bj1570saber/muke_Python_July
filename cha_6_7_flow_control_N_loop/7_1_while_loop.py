count = 1
while count < 3:
    print(count)
    count += 1
count = 1
while count < 6:
    print(count)
    count += 1
else:# Just like if-else. else will be invoke when condition == False:
    print('END')

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum) # 2500
print(20 * '~')


# break:
num = 0
while num < 100:
    if(num > 10):
        break
    print(num)
    num += 1
print('End.')
print(20 * '~')

# continue
# print Odd number only (1-10)
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num)
print('End.')
print(20 * '~')