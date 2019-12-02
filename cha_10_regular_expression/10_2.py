import re

a = 'C0Python7C++8C#9Java6Javascript5Python'
# Filter out digits.
digit = re.findall('\d', a)
print(digit)#['0', '7', '8', '9', '6', '5']

no_digit = re.findall('\D', a)
print(no_digit)
#output:
