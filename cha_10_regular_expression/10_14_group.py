import re
s= 'life is short, i use python.life short, use python.'
r = re.search('life(.*)python',s)
print(r.group(0))#life is short, i use python.life short, use python
# group(0) always return original string

print(r.group(1))#is short, i use python.life short, use 
#print(r.group(2)) #error

r = re.findall('life(.*)python',s)
print(r)# [' is short, i use python.life short, use ']

s= 'life is short, i use python, i love python'
r = re.search('life(.*)python(.*)python',s)
print(r.group(0))#life is short, i use python, i love python
print(r.group(1))#is short, i use
print(r.group(2))#, i love 
print('~'*20)
print(r.group(0,1,2))
#('life is short, i use python, i love python', 
# ' is short, i use ', 
# ', i love ')
print('~'*20)
print(r.groups())
#(' is short, i use ', ', i love ')
