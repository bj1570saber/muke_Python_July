# JSON: a light weight data exchange format.(compare to XML)
# (JavaScript Object Notation)
# Use: 1.Communication language between two or more programming languages.
#      2.Website frontend and backend communication.
#      3.JSON charactor string: JSON format string {"name":"Jerry"}
# Easier to read, parse, efficiency.
import json
json_str = '{"name":"qiyue", "age":18}' # be careful with ' and  "
student = json.loads(json_str)
print(type(student))#<class 'dict'>
print(student)#{'name': 'qiyue', 'age': 18}  Note: ' '
print(student['name'])#qiyue
print('~' * 20)

json_str = '[{"name":"qiyue", "age":18,"flag": false},{"name":"Tom", "age":20}]'
student = json.loads(json_str)
print(type(student))#<class 'list'>
print(type(student[1]))#<class 'dict'>       # Note: this is 'False', in JSON is 'false'
print(student)#[{'name': 'qiyue', 'age': 18, 'flag': False}, 
              # {'name': 'Tom', 'age': 20}] 
print('~' * 20)
# deserialization：The process of transfer string to specific programming data structure.