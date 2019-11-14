d = {'a':{1:2, 3:4}, 'Bob':60, 'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(type(d))#<type 'dict'>

print(d)#{'a': {1: 2, 3: 4}, 'Bob': 75, 'Michael': 95, 'Tracy': 85}
#'Bob':60 was overrided 

if 'Bob' in d: # 'in' keyword prevent access not exist key-value pair
    print(d['Bob'])#75  d[key] search in dict
if not('Jerry' in d): 
    print('No Jerry')

#key limits: immutable value(int,str,tuple)
d_1 = {(1,2):'a', 2:'b'}
print(d_1[(1,2)])#a

# dict - get()
print(d.get('Jerry'))#output: None

#customize return message:
print(d.get('Jerry', 'not here %d' %666))# not here 666

# update value    
d['Bob'] = 3.14
print(d['Bob']) # 3.14

# Delete a value:
d.pop('Michael')
print(d)# {'Bob': 3.14, 'Tracy': 85}
