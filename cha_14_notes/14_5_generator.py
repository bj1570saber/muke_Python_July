# generator 生成器 -> a function
# print 0-10000

# n = [i for i in range(0,10001)]# n is a list consume memory.
# print(n)

# def gen(max): # A print function. Did not save all numbers.
#     n = 0
#     while n <= max:
#         print(n)
#         n+=1

# gen(10000)

# this is a generator:
def gen(max): # Did not save all numbers in memory, It's Saving a algorithm.
    n = 0
    while n <= max:
        n+=1
        yield n # it will pause at here in the first loop
    # Every time program call next(g), 
    # it will come back and excute next loop cycle.

g = gen(10000)
print(g)#<generator object gen at 0x1025752e0>
print(next(g))#1
print(next(g))#2
print(next(g))#3
print('~')

n = (i for i in range(0,10001)) 
# change to parentheses. n is a generator now.
print(n) #<generator object <genexpr> at 0x10393c2e0>