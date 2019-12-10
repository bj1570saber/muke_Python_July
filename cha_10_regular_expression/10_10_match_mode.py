import re
language= 'PythonC#\nJavaPHP'

r = re.findall('c#', language, re.I)
print(r)#['C#'] I  IGNORECASE  Perform case-insensitive matching.

r = re.findall('c#.{1}', language, re.I)
print(r)#[] . match all character except \n

r = re.findall('c#.{1}', language, re.I | re.S)
print(r)#['C#\n']   re.S allow '.' to match \n
# S  DOTALL "." matches any character at all, including the newline.