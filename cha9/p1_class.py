# Object Oriented -> meaningful
# class => Object Oriented
# class is a reflection of real world elements.
# Basic function of class：encapsulation
# class encapsulates data(fields) and actions(functions) of same kind of objects.

class Student():
    # fields
    name = ''
    age = 0
    # functions
    def __init__(self): #constructor
        print('student')
        # return None # only return None (default or explicit).

    # def __init__(self, name, age):
    #     self.__init__()
    #     self.name = name
    #     self.age = age

    def introduce(self):
        print('name: ' + self.name)
        print('age: '+ str(self.age))
    
    def do_homework(self):
        print("do_homework")

#test:
student1 = Student()
student1.introduce()
student1.do_homework()

a = student1.__init__()#return default None to a
print(type(a))# <class 'NoneType'>
print(a)# None