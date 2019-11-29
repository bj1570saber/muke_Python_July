# 面向对象
# 有意义的面向对象
# 类 = 面向对象
# 类最基本的作用：封装

# Object Oriented -> meaningful
# class => Object Oriented
# class is a reflection of real world elements.
# Basic function of class：encapsulation
# class encapsulates data(fields) and actions(functions) of same kind of objects.

class Student():
    name = '$'
    age = 0

    def print_file(self):
        print('name: ' + self.name)
        print('age: '+ str(self.age))

#test:
student = Student()# default constructor
student.print_file()# print class default variable values
#name: 
#age: 0 

