#generalize set
# \d digit, \D not digit
# \w (word char) digit + alphabet \W not word char
# \s blank character \S: not blank character

import re
a = 'python 11\t11\njava&678\rphp__'
w = re.findall('\w', a)#[A-Za-z0-9]
print(w)
print('~'*20)

w_2 = re.findall('[A-Za-z0-9_]', a)
print(w_2)
print('~'*40)

not_w = re.findall('\W', a)#[A-Za-z0-9]
print(not_w)
print('~'*30)

blank = re.findall('\s', a)#[]
print(blank)
print('~'*20)

not_blank = re.findall('\S', a)#[]
print(not_blank)
print('~'*40)