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
    def introduce(self):
        print('name: ' + self.name)
        print('age: '+ str(self.age))
    
    def do_homework(self):
        print("do_homework")

#test:
student = Student()
student.introduce()
student.do_homework()

