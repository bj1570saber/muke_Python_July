d = {'a':{1:2, 3:4}, 'Bob':60, 'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(type(d))#<type 'dict'>

print(d)#{'a': {1: 2, 3: 4}, 'Bob': 75, 'Michael': 95, 'Tracy': 85}
#'Bob':60 was overrided 
print('~'*20)
if 'Bob' in d: # 'in' keyword prevent access not exist key-value pair
    print(d['Bob'])#75  d[key] search in dict
if not('Jerry' in d): 
    print('No Jerry')
print('~'*20)

#key limits: immutable value(int,str,tuple)
d_1 = {(1,2):'a', 2:'b'}
print(d_1[(1,2)])#a
print('~'*20)

# dict.get()
print(d.get('Jerry'))#output: None

#customize return message:
print(d.get('Jerry', 'not here %d' %666))# not here 666 #get() fail message
print('~'*20)

# update value    
d['Bob'] = 3.14
print(d['Bob']) # 3.14

d.setdefault('add','new')
# Delete a value:
d.pop('Michael')
print(d)# {'a': {1: 2, 3: 4}, 'Bob': 3.14, 'Tracy': 85, 'add': 'new'}
