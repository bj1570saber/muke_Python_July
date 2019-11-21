def f(a):
    round(a,1)#if no return statement. Default to return None.
print(f(3.14))

def add(a,b):
    return a+b
print(add(2,3))# 5

def recur(a):
    recur(a)
'''
print(recur(1))
[Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded

How to set repeated limits:
'''
import sys
sys.setrecursionlimit(10000)

def print_code(a):
    print(a)

a = add(1,8)
b = print_code('Python')
print(a,b)#9 None   print can contain unlimited parameters.