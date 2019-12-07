# JSON: a light weight data exchange format.(compare to XML)
# Use: 1.Communication language between two or more programming languages.
#      2.Website frontend and backend communication.
#      3.JSON charactor string: JSON format string {"name":"Jerry"}
# Easier to read, parse, efficiency.
import json
json_str = '{"name":"qiyue", "age":18}' # be careful with ' and  "
student = json.loads(json_str)
print(type(student))
print(student)

