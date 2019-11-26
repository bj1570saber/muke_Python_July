c =  50
def add(x,y):
    c = x + y # local variable
    #return c
    print(c)#3

print(add(1,2))#None
print(c)#50

print('~' * 20)
d = 10 # global variable
def demo():
    d += 1
print(d)

print('~' * 20)
# python allow to access for loop variable
def demo_1():
    c = 50
    # python does not have block scope. For loop is a block scope
    for i in range(0,9):
        a = 'a'
        c += 1
    print(c)#59
    print(a)# a

demo_1()