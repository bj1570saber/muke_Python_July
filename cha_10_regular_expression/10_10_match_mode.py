import re
language= 'PythonC#\nJavaPHP'

r = re.findall('c#', language, re.I)
print(r)#['C#']
r = re.findall('c#.{1}', language, re.I)
print(r)#[]
r = re.findall('c#.{1}', language, re.I | re.S)
print(r)#['C#\n']   re.S allow '.' to match \n
