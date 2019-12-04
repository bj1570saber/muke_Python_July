#数量词
import re
a = 'python1111java678php'

r = re.findall('[a-z]{3,6}', a) 
# num will allowd to filter length between 3 - 6 words.
print(r)

r = re.findall('[a-z0-3]{3,6}', a) 
# num will allowd to filter length between 3 - 6 words.
print(r)