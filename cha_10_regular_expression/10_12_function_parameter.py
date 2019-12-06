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
print('~'* 20)

s = 'A8C3721D086'
def convert_multi_digits(value):
    matched = value.group()
    #print(matched)
    # print(matched.find('0')==0)
    if matched.find('0') == 0:
        if int(matched) == 0:
            return '0'
        else: 
            return '0'+'2'
    elif int(matched) > 9:
        return '2'
    else:
        return '1'

r = re.sub('\d+',convert_multi_digits, s)# every digit will be apple convert()
print(r)#A1C2D2