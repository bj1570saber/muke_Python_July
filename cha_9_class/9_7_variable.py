class Student():
    name = 'None'
    age = 0
    
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
        print('constructor of '+ self.name)
        print(name)
        print(age)
        
student1 = Student("Jerry", 20)
print(student1.__dict__)#{'name': 'Jerry', 'age': 20}
# search variable path:
# object.variable -> class.variable -> ancestor class variable

print(Student.__dict__)# print class variables
'''
{'__module__': '__main__', 'name': '', 'age': 0, 
'__init__': <function Student.__init__ at 0x1080ef700>, 
'__dict__': <attribute '__dict__' of 'Student' objects>, 
'__weakref__': <attribute '__weakref__' of 'Student' objects>, 
'__doc__': None}
'''