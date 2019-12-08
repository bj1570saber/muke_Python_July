from functools import reduce

list_x =[1,2,3,4,5,6,7,8]
r = reduce(lambda x,y : x+y, list_x)
print(r)# 36

# travel in 2D
p = [(1,3), (2,-2), (-2,3)] # movements
r = reduce(lambda x,y: (x[0]+y[0],x[1]+y[1]), p)
print(r)#(1, 4)

list_x =['1','2','3','4','5','6','7','8']
r = reduce(lambda x ,y : x+y, list_x, 'Initial parameter: ')
#last parameter can be initial parameter.

print(r)# Initial parameter: 12345678