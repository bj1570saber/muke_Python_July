class Student():
    sum = 0
    homework_count = 0
    name = 'None'
    age = 0
    
    def __init__(self, name1, age1):
        self.name = name1 
        self.age = age1
        self.__class__.sum += 1 # update class 'sum' variable
        print("Total number of students:" + str(self.__class__.sum))
        print('constructor of '+ self.name)

    def do_homework(self):
        self.__class__.homework_count += 1 # update class 'homework_count' variable
        print("All stuents has finished " + str(self.__class__.homework_count) + " homework.")
    
    @classmethod #装饰器，decorator
    def plus_sum(cls):
        pass

student1 = Student("Jerry", 20)
student2 = Student("Tom", 20)
student3 = Student("Feng", 20)
student1.do_homework()
student1.do_homework()
student2.do_homework()
student2.do_homework()
student2.do_homework()
# output:
# Total number of students:1
# constructor of Jerry
# Total number of students:2
# constructor of Tom
# Total number of students:3
# constructor of Feng
# All stuents has finished 1 homework.
# All stuents has finished 2 homework.
# All stuents has finished 3 homework.
# All stuents has finished 4 homework.
# All stuents has finished 5 homework.