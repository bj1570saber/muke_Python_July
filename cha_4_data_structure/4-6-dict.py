# key limits: immutable value(int,str,tuple)
d_1 = {(1,2):'a', 2:'b'}
print(d_1[(1,2)])#a
print('~'*20)

d = {'a':{1:2, 3:4}, 'Bob':60, 'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(type(d))# <class 'dict'>

print(d)# {'a': {1: 2, 3: 4}, 'Bob': 75, 'Michael': 95, 'Tracy': 85}
# 'Bob':60 was overrided 
print('~'*20)

# add value:
d['Saber'] = 'fate'
print(d)#{'a': {1: 2, 3: 4}, 'Bob': 75, 'Michael': 95, 
        # 'Tracy': 85, 'Saber': 'fate'}

# delet a value:
d.pop('Saber')

# update value    
d['Bob'] = 3.14
print(d['Bob']) # 3.14
print('~')

print(d)#{'a': {1: 2, 3: 4}, 'Bob': 3.14, 'Michael': 95, 'Tracy': 85}
print(d.setdefault('add','new'))#new
print(d)#{'a': {1: 2, 3: 4}, 'Bob': 3.14, 'Michael': 95, 'Tracy': 85, 'add': 'new'}
print(d.setdefault('add','another'))#new
print(d)
print('~')

# search in dict:
if 'Bob' in d: # 'in' keyword prevent access not exist key-value pair
    print(d['Bob'])# 3.14  d[key] search in dict
if not('Jerry' in d): 
    print('No Jerry')
print('~'*20)

# dict.get()
print(d.get('Jerry'))# output: None 
# print(d['Jerry'])# KeyError: 'Jerry'

#customize return message:
print(d.get('Jerry', 'not here %d' %666))# not here 666
print('~'*20)

