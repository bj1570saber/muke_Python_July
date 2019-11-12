d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
if 'Bob' in d: # 'in' keyword prevent access not exist key-value pair
    print(d['Bob'])
if not('Jerry' in d):
    print('No Jerry')

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

##################
# Set
s = set([1, 1, 2, 2, 3, 3])
print(s) # output: {1, 2, 3} duplicated will be removed.

s.add('string') # add()
print(s)# {1, 2, 3, 'string'}

s.remove(1)
print(s)# {2, 3, 'string'}

# &
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2) # {2, 3}
# |
print(s1 | s2) # {1, 2, 3, 4}

# s.add([1,2,3]) # error, list can be changed, can not add to set.
print(s)

# Mutable Object: list, set, dict
a = ['c', 'b', 'a']
print(a)
a.sort()
print(a)

# Immutable Object: String, digit
b = 'abc'
c = b.replace('a', 'A') # create a new variable, not really replace.
print(b)
print(c)
