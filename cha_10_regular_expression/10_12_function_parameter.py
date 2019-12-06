import re
s = 'A8C3721D86'
# if num >= 6 replace by 9;
# else replace by 0;
def convert(value):
    matched = value.group()
    if int(matched) >= 6:
        return '9'
    else:
        return '0'
    
r = re.sub('\d',convert, s)# every digit will be apple convert()
print(r)#A9C0900D99