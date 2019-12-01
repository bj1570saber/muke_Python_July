class Student():
    name = 'None'
    age = 0
    
    def __init__(self,name1, age1):
        self.name = name1 
        self.age = age1
        print('constructor of '+ self.name)
        #print(name) # Error, can not access class field.
        print(Student.age) # need a Class Name like this.
        print(self.__class__)# output: <class '__main__.Student'>
        # This is another way to access Class field:
        print(self.__class__.name) # output: None

    def do_homework(self):
        print(self.name +" is doing homework.")
student1 = Student("Jerry", 20)
# output:
# constructor of Jerry
# 0
# <class '__main__.Student'>
# None
