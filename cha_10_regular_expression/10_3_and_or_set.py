import re
s = "abc, acc, adc, aec, afc, ahc"
# '[]' : 或 or
# '()' : 且 and
r = re.findall('a[cf]c', s)# filter out acc or afc
print(r)#['acc', 'afc']

not_r = re.findall('a[^cfd]c', s)# filter out not(acc, afc or adc)
print(not_r)#['abc', 'aec', 'ahc']

cdef_r = re.findall('a[c-f]c', s)# filter out a[cdef]c
print(cdef_r)#['acc', 'adc', 'aec', 'afc']

cdef_r = re.findall('a(cc)', s)# filter out a[cdef]c
print(cdef_r)#['cc']  only retrive string inside ()