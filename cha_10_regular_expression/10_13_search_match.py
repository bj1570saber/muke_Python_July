import re

s = 'A83C72D1D8E67'
r = re.match('\d', s)# match from first char of String
print(r)#None
r = re.search('\d', s)# return first match char
print(r)#<re.Match object; span=(1, 2), match='8'>
print('~' * 20)

s = '83C72D1D8E67'
r = re.match('\d', s)# match from first char of String
print(r)#<re.Match object; span=(0, 1), match='8'>
r = re.search('\d', s)# return first match char
print(r)#<re.Match object; span=(0, 1), match='8'>
print('~' * 20)

s = '83C72D1D8E67'
r = re.match('\d', s)# match from first char of String
print(r.span())#(0, 1)
r = re.search('\d', s)# return first match char
print(r.group())# 8
# match() and search() only match one time. not for all.

r = re.findall('\d', s)
print(r)#['8', '3', '7', '2', '1', '8', '6', '7']

