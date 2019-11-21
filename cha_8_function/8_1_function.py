#rount to 2 decimal place.
a = 3.1415926
print(a*1000//1)
z = a * 1000//1/1000
print(z)# 3.141

#funciton:
print(round(a,3))# 3.142

# Fix algorithm:
a = 3.1415926
z = (a * 1000 + 0.5)//1/1000 #round up by +0.5
print(z)# 3.142

'''
main purpose of funcion:
functional
encapsulation
avoid writing  duplicate codes
increase readability
'''