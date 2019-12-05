import re
# A regular expression, regex or regexp is a sequence of 
# characters that define a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

# example: if string a includes Python-
a = 'C|Python|C++|C#|Java|Javascript|Python'
print(a.index('Python')>1)#True
print('Python' in a)#True
r = re.findall('Python', a)# regular expression
if len(r) > 0:
    print('a includes "python"')
else:
    print('Not includes')
print(r)#['Python', 'Python']
#output:
# True
# True
# str includes "python"
# ['Python', 'Python']