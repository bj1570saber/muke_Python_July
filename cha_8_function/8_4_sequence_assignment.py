a,b,c = 1,2,3
print(a,b,c)#1 2 3

d = 2,4,6
print(type(d))#<class 'tuple'>

a,b,c = d
print(a,b,c)#2 4 6

#e,f = d #ValueError: too many values to unpack (expected 2)
#print(e,f)

a=b=c=1
print(a,b,c)#1 1 1