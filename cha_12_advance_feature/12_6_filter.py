
list_x =[1,0,3,4,0,6,0,8]
r = filter(lambda x: True if x != 0 else False, list_x)# filter out 0
# lambda expression must return T or F, T will stay, F will remove.
print(list(r))#[1, 3, 4, 6, 8]

r = filter(lambda x: x, list_x)# filter out 0
# 0: False other int are True
print(list(r))#[1, 3, 4, 6, 8]

# filter out lower case:
list_l = ['A','a','b','B','C','c']
l = filter(lambda x: True if x.isupper() else False, list_l)
print(list(l))#['A', 'B', 'C']

#imperative programming
# for loop; if else

#functional programming
# map,reduce,filter,  lambda