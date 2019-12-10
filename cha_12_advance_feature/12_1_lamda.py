# lambda expression

def add(x, y):
    return x+y

print(add(1,2))#3

f = lambda x,y: x+y
print(f(1,2))#3
print('~')

# ternary expression 三元表达式
x = 2
y = 1
r = x if x > y else y
print(r)#2
