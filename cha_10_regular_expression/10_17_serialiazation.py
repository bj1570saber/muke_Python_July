'''
Deserialiazation data type transfer:
JSON        Python
object      dict
array       list
string      str
number      int
number      float
true        True
false       False
null        None
'''

import json

student = [
            {'name': 'qiyue', 'age': 18, 'flag': False}, 
            {'name': 'Tom', 'age': 20}
          ]

json_str = json.dumps(student)
print(type(json_str))#<class 'str'>
print(json_str)#[{"name": "qiyue", "age": 18, "flag": false}, 
               # {"name": "Tom", "age": 20}]
# NoSQL Database: good to save object data
