#list comprehension
### List -> List,Set,Dict,
a = [1,2,3,4,5,6]
b = [ i*i for i in a] 
c = [ i**3 for i in a]
print(b)#[1, 4, 9, 16, 25, 36]
print(c)#[1, 8, 27, 64, 125, 216]

# restriction of output
d = [i**2 for i in a if i >= 5] # map() can not simplify like this.
print(d)#[25, 36]

set_i = {j**2 for j in a} # NOTE this reference a
print(set_i)#{1, 4, 36, 9, 16, 25}

dict_i = {i:i**2 for i in a}
print(dict_i)#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

tuple_i = tuple(i**2 for i in a)# must explicit convert to tuple. ()is parenthesis
print(tuple_i)#(1, 4, 9, 16, 25, 36)

e = list(map(lambda x: x**2, a))
print(e)#[1, 4, 9, 16, 25, 36]
print('~')

###Set -> Set, List, Dict
f = {1,2,3,4,5,6}
g = [i**2 for i in f] # a list result.
print(g)#[1, 4, 9, 16, 25, 36]
# although f is a set, but result depends on g's type.

h = {i**2 for i in f} # a set result.
print(h)#{1, 4, 36, 9, 16, 25}

k = {i:i**2 for i in f}
print(k)#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

### Dict -> 
l ={1:1, 2:2, 3:3, 4:4, 5:5, 6:6}