# generalize set
# \d digit, \D not digit
# \w (word char) digit + alphabet; \W not word char
# \s blank character; \S: not blank character
# . match all char except "\n" next line char
import re
a = 'python 11\t11\njava&678\rphp__'
w = re.findall('\w', a)#[A-Za-z0-9_]
print(w)
# ['p', 'y', 't', 'h', 'o', 'n', '1', '1', '1', 
# '1', 'j', 'a', 'v', 'a', '6', '7', '8', 'p', 
# 'h', 'p', '_', '_']
print('~'*20)

w_2 = re.findall('[A-Za-z0-9_]', a)
print(w_2)
# ['p', 'y', 't', 'h', 'o', 'n', '1', '1', '1', 
# '1', 'j', 'a', 'v', 'a', '6', '7', '8', 'p', 
# 'h', 'p', '_', '_']
print('~'*40)

not_w = re.findall('\W', a)
print(not_w)#[' ', '\t', '\n', '&', '\r']
print('~'*30)

blank = re.findall('\s', a)#[]
print(blank)#[' ', '\t', '\n', '\r']
print('~'*20)

not_blank = re.findall('\S', a)#[]
print(not_blank)
# ['p', 'y', 't', 'h', 'o', 'n', '1', '1', '1', '1', 
# 'j', 'a', 'v', 'a', '&', '6', '7', '8', 'p', 'h', 
# 'p', '_', '_']# includes '&'
print('~'*40)