### Dict -> List, Tuple, Set, Dict
students = {
    'a': 18,
    'b': 19,
    'c': 20
}
#List
di =[key for key, value in students.items()]
print(di)#['a', 'b', 'c']

#Tuple
di =tuple(key for key, value in students.items())# return a generator
print(di)#('a', 'b', 'c')                   Since tuple is immutable,

#Set
di ={key for key, value in students.items()}
print(di)#{'a', 'b', 'c'}

#Dict
di ={ key: value + 5 for key, value in students.items()}
print(di)#{'a': 23, 'b': 24, 'c': 25}