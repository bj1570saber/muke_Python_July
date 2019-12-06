import re
a = 'PythonPythonPythonJSPythonPython'
#
r = re.findall('(Python){3}', a)#'PythonPythonPython'
print(r)#['Python']

#
r = re.findall('(Python){4}', a)
print(r)#[]

#
r = re.findall('(Python){3}(JS)(Python)', a)
print(r)#[('Python', 'JS', 'Python')]

