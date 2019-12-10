import re
#
qq_1 = '100001'
r = re.findall('\d{4,8}', qq_1)
print(r)#['100001']

#
qq_2 = '100'
r = re.findall('\d{4,8}', qq_2)
print(r)#[]

#
qq_3 = '100000000100'
r = re.findall('\d{4,8}', qq_3)
print(r)#['10000000', '0100']

### Edge Match
# ^ : match from beginning
# $ : match from ending
qq_4 = '1000000001'
r = re.findall('^\d{4,8}', qq_4)
print(r)#['10000000'] accept first 8 digits
r = re.findall('\d{4,8}$', qq_4)
print(r)#['00000001'] accept last 8 digits

#
qq_5 = '1000000001' # total 8*0
r = re.findall('000', qq_5)
print(r)#['000', '000']

print('~')
#
qq_6 = '100000 0001' 
r = re.findall('^000', qq_6)# ^ : match from beginning
print(r)#[] since the string start with '1' no match.

# 4~8
qq_7 = '000000001' 
r = re.findall('^000', qq_7)# ^ : match from beginning
print(r)#['000'] since the string start with '000'

# 4~8
qq_8 = '010000001' 
r = re.findall('^000', qq_8)# ^ : match from beginning
print(r)#[] since the string start with '010'

# 4~8
qq_9 = '010000001' 
r = re.findall('000$', qq_9)# $ : match from ending
print(r)#[] since the string ending with '001'
