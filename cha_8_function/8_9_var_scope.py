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
    e = 50
    # python does not have block scope. For loop is a block scope
    for i in range(0,9):
        a = 'a'
        e += 1
    print(e)#59
    print(a)# a

demo_1()

print('~' * 20)
f = 1
def func1():
    f = 2
    def func2():
        #f = 3
        print(f)
    func2()
    print(f)
func1()
print(f)


