# [a-z]{数量词}
import re
a = 'pythonn1111java678php'
# Python default greedy filter(as long as possible).
r = re.findall('[a-z]{3,6}', a) 
# {number} will allowd to filter length between 3 - 6 words.
print(r)#['python', 'java', 'php']

r = re.findall('[a-z0-3]{3,6}', a) 
# num will allowd to filter length between 3 - 6 words.
print(r)#['python', 'n1111j', 'ava', 'php']
print('~' * 20)

# Force None greedy filter(as short as possible)
r = re.findall('[a-z]{3,6}?', a) # '?' marker to force None greedy.
# num will allowd to filter length between 3 - 6 words.
print(r)#['pyt', 'hon', 'jav', 'php']