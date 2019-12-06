import re
language = 'PythonC#JavaC#PHPC#'
r = re.sub('C#', 'GO', language, 0)
# (4th)parameter count: 0 -> replace all
#                    num -> replace specific max times.
print(r)#PythonGOJavaGOPHPGO
r = re.sub('C#', 'GO', language, 2)
print(r)#PythonGOJavaGOPHPC#

language = language.replace('C#','GO')
print(language)