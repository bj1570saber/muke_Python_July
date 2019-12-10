import re
a = 'PythonPythonPythonJSPythonPythonPython'
#
r = re.findall('(Python){3}', a)#'PythonPythonPython'
print(r)#['Python', 'Python']

#
r = re.findall('(Python){4}', a)
print(r)#[]

#
r = re.findall('(Python){3}(JS)(Python)', a)
print(r)#[('Python', 'JS', 'Python')]

#
a = 'PythonPythonPython JS PythonPythonPython'
r = re.findall('(Python){3}(JS)(Python)', a)
print(r)#[] did not filter out space.

#
r = re.findall('(Python){3}\s(JS)\s(Python)', a)
print(r)#[('Python', 'JS', 'Python')]  \s - filter out space.