class Student():
    sum = 0
    name = 'None'
    age = 0
    
    def __init__(self, name1, age1):
        self.name = name1 
        self.age = age1
        print('constructor of '+ self.name)

    @classmethod #装饰器，decorator
    def plus_sum(cls):# cls can be replace by other string
        cls.sum += 1 # cls prepresent Class(in this case: Student)
        print("Total number of students:" + str(cls.sum))

student1 = Student("Jerry", 20)
Student.plus_sum()# invoke class method by Class
student2 = Student("Tom", 20)
student2.plus_sum()# invoke class method by object
student3 = Student("Feng", 20)
Student.plus_sum()
# output:
# constructor of Jerry
# Total number of students:1
# constructor of Tom
# Total number of students:2
# constructor of Feng
# Total number of students:3