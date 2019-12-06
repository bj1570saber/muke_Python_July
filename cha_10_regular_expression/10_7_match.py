
import re
a = 'pyth_pytho0python1pythonn2pythonnnn'

# *: match previous char 'n' 0 or many times
r = re.findall('python*', a)
print(r)# ['pytho', 'python', 'pythonn', 'pythonnnn']
print('~' * 20)

# +: match previous char 'n' 1 or many times
r = re.findall('python+', a)
print(r)# ['python', 'pythonn', 'pythonnnn']
print('~' * 20)

# ?: match previous char 'n' 1 or 0 time
r = re.findall('python?', a)
print(r)#['pytho', 'python', 'python', 'python']
print('~' * 20)

# number: match previous char 'n' 1-3 times OK
r = re.findall('python{1,3}', a) # accept 1-3 times 'n'.
print(r)#['python', 'pythonn', 'pythonnn']
print('~' * 20)

### ?: force None Greedy
# ? match previous char 'n' 1 time only 
r = re.findall('python{1,3}?', a) # as less 'n' as possible.
print(r)#['python', 'python', 'python']