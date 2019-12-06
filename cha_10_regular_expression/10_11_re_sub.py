import re
language = 'PythonC#JavaC#PHPC#'
r = re.sub('C#', 'GO', language, 0)
# (4th)parameter count: 0 -> replace all
#                    num -> replace specific max times.
print(r)#PythonGOJavaGOPHPGO
r = re.sub('C#', 'GO', language, 2)
print(r)#PythonGOJavaGOPHPC#

r = language.replace('C#','GO')
print(r)#PythonGOJavaGOPHPGO
print('~'* 20)

def convert(value):
    pass
language = 'PythonC#JavaC#PHPC#'

# pass function convert() as a parameter
r = re.sub('C#', convert, language, 1)
# First 'C#' in string will be pass as parameter to convert(),
# The return value will replace 'C#'. Since pass return None.
# 'C#' was delete.
print(r)#PythonJavaC#PHPC#

r = re.sub('C#', convert, language, 2)
print(r)#PythonJavaPHPC#

def convert_p(value):
    matched = value.group() # String
    print(value)# re.Match boject
    print(matched)
    return '!!' + matched + '!!'
    
r = re.sub('C#', convert_p, language)
print(r)#Python!!C#!!Java!!C#!!PHP!!C#!!
# output:
# <re.Match object; span=(6, 8), match='C#'>
# <re.Match object; span=(12, 14), match='C#'>
# <re.Match object; span=(17, 19), match='C#'>
# Python!!C#!!Java!!C#!!PHP!!C#!!