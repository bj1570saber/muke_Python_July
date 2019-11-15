'''Summary:
1. compare type:
    #can not compare child instance.
    type(a)==type(b)
    type(a)==int
     
    #compare child instance too.
   A better type check: isinstance(a,int):return  T F
   
2. a == b :compare value
3. a is b :compare id()

'''
a = 'Hello'
b = 1.3
t_1 = (int, str, bool)
print(isinstance(a,t_1))#True
print(isinstance(b,t_1))#False
print()
# Member operator
print(1 in [1,2,3])#True
print('a' in 'aim')#True
print(0 not in (1,2,3))#True 
print(0 not in{0,1,2})#False 
print()

# in dict, matc h key
print('a' in {'a':1, 'b':2})#True
print('a' in {1:'a', 2:'b'})#False


# Identity operator
a = 1
b = 1
print(a==b)#True
print(a is b)#True
print('\na = 1.0:')
a = 1.0
print(a==b)#True
print(a is b)#False more accurate
print(id(a))
print(id(b)) 
print('a and b have different address.\n')

c = [1,2]
d = [1,2]
print(c==d)#True
print(c is d)#False
print()
#
e = {1,2,3}
f = {2,3,1}
print(e==f)#True
print(e is f)#False
print()
#
g = (1,2,3)
h = (2,3,1)
print(g==h)#False
print(g is h)#False
