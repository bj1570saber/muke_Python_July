import re
s = "abc, acc, adc, aec, afc, ahc"

r = re.findall('a[cf]c', s)# filter out acc or afc
print(r)

not_r = re.findall('a[^cfd]c', s)# filter out not(acc or afc)
print(not_r)

cdef_r = re.findall('a[c-f]c', s)# filter out a[cdef]c
print(r)
